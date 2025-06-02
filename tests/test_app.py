def test_sentiment():
    from ai_models.sentiment_analysis import analyze
    assert analyze("I love it!") == "positive"
    assert analyze("This is bad") == "negative"