# MOODRING BOT

Our bot analyzes words in a discord server, and gives them a mood.

## Features

- Reads every message in a server, stores it, and assigns it a mood. 

- Type "!hello" to get a response to the bot to see if it is currently on and analyzing messages. 

- Enter command "!mood" followed by some text to ask the bot to return the mood of whatever text you typed.

- Enter "!weekly" to return the weekly mood of the server, or the most common mood analyzed.

- HOWEVER, the script automatically posts the weekly mood of the server every wednesday at 8 pm. If you'd like to change it go to the following section of the bot.py file:

        if now.weekday() == 2 and now.hour == 8 and now.minute == 0:  # Check if it's 8 PM on Wednesday
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await send_weekly_mood(channel)  # Send the weekly report
            logging.info(f"Weekly mood report sent at {now}")
        else:
            logging.error("Channel not found for weekly mood report.")

    
    and change the 2 to whatever day you'd like, where monday is 0 and Sunday is 6. Change the 8 to whatever hour in the day you'd like, on a 0-23 scale. Then change minute to whatever you'd like, from 0 to 59. 

## Set up

### Requirements

- Python
- Some sort of IDE (Script was originally in VSCode)
- A virtual environment (optional)
- The necessary installations

### Virtual Environment setup

Run the following in your terminal, preferably the integrated one on your IDE, if you have it. 
    
    - First, make sure you're in the correct directory. This is why we reccomend doing it in your integrated terminal.

    python3 -m venv .venv

    - .venv can be whatever name you'd like for your virtual enviroment, but .venv is common practice

    source .venv/bin/activate

    - These commands will have created a virtual environment for you, and now you should have a (.venv) in front of your directory on the command line. 

### Installations

Run the following PIP commands to install the necessary libraries

    pip install discord.py

    pip install python-dotenv
    
- THIS STEP IS EXTREMELY IMPORTANT. If you do not download nrclex and the corpora exactly like this, THE PROGRAM WILL NOT WORK. 

        pip install nrclex==3.0.0

        python -m textblob.download_corpora

### .env

Create your .env file in the same directory as your program. The .env file should contain the following.

    DISCORD_TOKEN="your_token_here"

To get your token, simply go to the develepor portal for discord, create the bot, and copy that token. 

You should also make sure your bot has the necessary permissions to function, being reading and sending messages.

### .gitignore

This is highly encouraged, as not doing this could force your token into the public, and give someone potentially harmful access to your bot. 

make a file called .gitignore, and in it put the following

    .env
    .venv (if you have a virtual environment)

This will keep your github clean of any security risks

## RUNNING THE BOT

Simply run the code. If you've done everything right, then you should be all set with that. 

