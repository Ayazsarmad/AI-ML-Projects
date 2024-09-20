# -*- coding: utf-8 -*-
"""pythonSet3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FFFlktQ9UPlvRqkXG3LqHnKz_vu0yvXO
"""

from transformers import pipeline

sentiment_analysis = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analysis(text)

    if result[0]['label'] == 'POSITIVE':
        return "this value is: "'Positive'
    elif result[0]['label'] == 'NEGATIVE':
        return "this value is: "'Negative'
    else:
        return 'Neutral'

text1 = "i love pakistan"
print(analyze_sentiment(text1))

text2 = "i hate obesity"
print(analyze_sentiment(text2))

!pip install transformers

from transformers import pipeline

# Function to generate blog post
def generate_blog(text):
    blog_generator = pipeline("text-generation", model="gpt2")

    # Generate text with truncation
    result = blog_generator(
        text,
        max_length=150,
        num_return_sequences=1,
        temperature=0.8,  # Slightly increased temperature for more creativity
        truncation=True
    )

    # Return the generated blog post
    return result[0]['generated_text']

# Example blog topic
topic = "Karachi's vibrant culture and history"
# Generate the blog post
blog_post = generate_blog(topic)

# Print the blog post
print(blog_post)

