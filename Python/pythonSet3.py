from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analysis(text)
    return result

text1 = "i love pakistan"
print(analyze_sentiment(text1))




