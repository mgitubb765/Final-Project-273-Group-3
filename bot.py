import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import json
import logging
from datetime import datetime, timedelta
from nrclex import NRCLex
from mood_color import get_mood_color
import asyncio

# -----------------------------
# Setup
# -----------------------------
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1496274134492250124  # Channel ID where you want to send the report
FILE_NAME = "messages.json"

# -----------------------------
# Logging setup for easier debugging
# -----------------------------
logging.basicConfig(filename='bot.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# -----------------------------
# Bot setup
# -----------------------------
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# -----------------------------
# Emotion analysis
# -----------------------------
def get_emotions(text):
    analysis = NRCLex(text)
    return {
        "raw": analysis.raw_emotion_scores,
        "freq": analysis.affect_frequencies,
        "top": analysis.top_emotions
    }

# -----------------------------
# Save messages to JSON
# -----------------------------
def save_message(message):
    with open(FILE_NAME, "r") as f:
        data = json.load(f)

    emotions = get_emotions(message.content)

    data.append({
        "user": str(message.author),
        "content": message.content,
        "channel": str(message.channel),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "emotions": emotions
    })

    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# -----------------------------
# Read messages
# -----------------------------
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Save the message as usual
    save_message(message)

    logging.info(f"Saved: {message.author} -> {message.content}")

    text = ""  

    # Handles mood command
    if message.content.startswith("!mood"):
        text = message.content.replace("!mood", "").strip()

        if not text:
            await message.channel.send("Type something after !mood")
            return

    if text:  
        emotions = get_emotions(text)
        logging.debug(f"Emotions from NRCLex: {emotions}")  # Log the emotions detected by NRCLex

        # Converts the emotion score to color, mood, and emoji color
        color, mood_text, emoji = get_mood_color(emotions["raw"])

        # Sends response back to Discord
        await message.channel.send(f"{emoji} Mood: **{mood_text}** ({color})")

    # Ensure the bot can process other commands (unchanged)
    await bot.process_commands(message)  # This ensures commands like !hello or others still work.

# -----------------------------
# Weekly mood report function
# -----------------------------
async def send_weekly_mood(channel):
    """Function to send the weekly mood report."""
    with open(FILE_NAME, "r") as f:
        messages = json.load(f)

    one_week_ago = datetime.now() - timedelta(days=7)

    # Filter messages from the last week
    weekly_messages = [msg for msg in messages if datetime.strptime(msg["time"], "%Y-%m-%d %H:%M:%S") >= one_week_ago]

    if not weekly_messages:
        await channel.send("No messages found for the past week.")
        return

    combined_emotions = {}

    # Aggregate emotions from the last week's messages
    for msg in weekly_messages:
        for emotion, score in msg["emotions"]["raw"].items():
            combined_emotions[emotion] = combined_emotions.get(emotion, 0) + score

    # Get the mood color, mood text, and emoji
    color, mood_text, emoji = get_mood_color(combined_emotions)

    # Send the weekly mood report to the channel
    await channel.send(
        f"**Weekly Server Mood Report**\n\n"
        f"Messages analyzed: {len(weekly_messages)}\n"
        f"{emoji} Overall Mood: **{mood_text}** ({color})"
    )

# -----------------------------
# Task: Send weekly report every Wednesday at 9:30 PM
# -----------------------------
@tasks.loop(minutes=1)  # Checks every minute instead of once every 24 hours
async def weekly_report_task():
    """This task runs every minute and checks if today is Wednesday at 8 PM."""
    now = datetime.now()
    
    if now.weekday() == 2 and now.hour == 8 and now.minute == 0:  # Check if it's 8 PM on Wednesday
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await send_weekly_mood(channel)  # Send the weekly report
            logging.info(f"Weekly mood report sent at {now}")
        else:
            logging.error("Channel not found for weekly mood report.")

# -----------------------------
# Bot event when it starts
# -----------------------------
@bot.event
async def on_ready():
    """Triggered when the bot has successfully logged in."""
    logging.info(f"{bot.user} is online!")
    # Start the periodic task (this checks if it's Wednesday at 9:30 PM every day)
    weekly_report_task.start()

# -----------------------------
# Commands for the bot
# -----------------------------
@bot.command()
async def hello(ctx):
    """Simple hello command."""
    await ctx.send("Hello! MoodRing is working and saving messages!")

@bot.command()
async def weekly(ctx):
    """Command to manually trigger the weekly mood report."""
    await send_weekly_mood(ctx.channel)

# -----------------------------
# Run the bot
# -----------------------------
if __name__ == "__main__":
    bot.run(TOKEN)