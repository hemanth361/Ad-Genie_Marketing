def analyze(text):
    if "bad" in text.lower():
        return "negative"
    elif "good" in text.lower():
        return "positive"
    return "neutral"