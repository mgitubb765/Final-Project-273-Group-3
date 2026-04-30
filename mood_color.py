import logging

def get_mood_color(emotion_frequencies):
    # Log the raw emotion frequencies for debugging
    logging.debug(f"Emotion Frequencies: {emotion_frequencies}")

    if not emotion_frequencies:
        return "Gray", "Mixed / Unclear mood", "⚪"

    # Filters out NRCLex summary values, keep only emotion categories
    filtered = {
        k: v for k, v in emotion_frequencies.items()
        if k not in ["positive", "negative"]
    }

    # Log the filtered emotions for debugging
    logging.debug(f"Filtered Emotions: {filtered}")

    if not filtered:
        return "Gray", "Mixed / Unclear mood", "⚪"

    dominant_emotion = max(filtered, key=filtered.get)

    # Log the dominant emotion for debugging
    logging.debug(f"Dominant Emotion: {dominant_emotion}")

    # Yellow is good mood
    if dominant_emotion in ["joy"]:
        return "Yellow", "Happy / Bright / Energetic", "💛"

    # Purple is excitable
    if dominant_emotion in ["anticipation"]:
        return "Purple", "Excited / Social / High Energy", "💜"

    # Blue is mellow
    if dominant_emotion in ["trust"]:
        return "Blue", "Calm / Safe / Comfortable", "💙"

    # Orange is feeling off
    if dominant_emotion in ["sadness", "disgust"]:
        return "Orange", "Off / Uneasy / Low Energy", "🧡"

    # Red is emotional intensity
    if dominant_emotion in ["anger", "fear"]:
        return "Red", "Overwhelmed / Emotional / Reactive", "❤️"

    return "Green", "Balanced / Neutral", "💚"