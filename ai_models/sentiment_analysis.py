def analyze(text):
    if any(x in text.lower() for x in ["bad", "hate", "worst"]):
        return "negative"
    if any(x in text.lower() for x in ["great", "love", "best"]):
        return "positive"
    return "neutral"