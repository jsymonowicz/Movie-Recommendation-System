'''
----------- T21 - Capstone Project - NLP Applications ------------
1. This code performs sentiment analysis on a dataset of product reviews.
2. The analized dataset is:
* name: "1429_1.csv",
* source: https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products,
* renamed as: 'amazon_product_reviews.csv'.
---------------------------- IMPORTANT ----------------------------
The following instalations in cmd are required to run this code:
* python -m spacy download en_core_web_sm
* pip install spacytextblob
* python -m textblob.download_corpora
'''

import spacy
import pandas as pd
from spacytextblob.spacytextblob import SpacyTextBlob

# NLP model for assessing sentiment
nlp_sm = spacy.load('en_core_web_sm')
nlp_sm.add_pipe('spacytextblob')
# NLP model for comparing similarity of sentences
nlp_md = spacy.load('en_core_web_md')


# Function for sentiment analysis of a string
## Input: string (review)
## Output: polarity on a scale -1 (very negative) to  1 (very positive)

def predict_sentiment(review):
    # Ensuring correct input format
    if not isinstance(review, str):
        raise Exception("Input must be a string!")
        
    # Input text cleaning.
    review = review.lower().strip()
    # Processing review text using spaCy.
    doc = nlp_sm(review)

    # Filtering out stop words.
    # Creating a list of tokens without stop words.
    tokens_clean = [word.text for word in doc if not word.is_stop]
    # Connecting token list to form nlp.
    doc_clean = nlp_sm(' '.join(tokens_clean))

    # Assessing review's sentiment polarity.
    polarity = doc_clean._.blob.polarity

    # Output in a form of a number
    return polarity

# Function inputting product review(s) and outputting its sentiment polarity.
def predict_sentiment(reviews):
    # Ensuring correct input format - converting into a list for further analysis
    if isinstance(reviews, list):
        pass
    elif isinstance(reviews, str):
        reviews = [reviews]
    elif isinstance(reviews, pd.Series):
        reviews = reviews.tolist()
    else:
        raise Exception("Input type must be string, list, or Pandas Series!")
    
    # Since we are analizing a list of reviews, output will also be a list
    polarities = []
    
    for review in reviews:
        # Input text cleaning.
        review = str(review)
        review = review.lower().strip()
        # Processing review text using spaCy.
        doc = nlp_sm(review)

        # Filtering out stop words.
        # Creating a list of tokens without stop words.
        tokens_clean = [word.text for word in doc if not word.is_stop]
        # Connecting token list to form nlp.
        doc_clean = nlp_sm(' '.join(tokens_clean))

        # Assessing review's sentiment polarity.
        polarity = doc_clean._.blob.polarity
        polarities.append(polarity)
    # Output in a form of tha number
    return polarities


# Function inputting two reviews and outputting their similarity.
def reviews_similarity(review_1, review_2):
    
    if not (isinstance(review_1, str) and isinstance(review_2, str)):
        raise Exception("Input type must be str!")
    # Process the input reviews using spaCy
    doc1 = nlp_md(review_1)
    doc2 = nlp_md(review_2)

    # Calculate the similarity between the processed reviews
    similarity_score = doc1.similarity(doc2)
    
    return similarity_score

review = 'I love eating bacon'
review_number = 45

# Loading product reviews for sentiment analysis.
df = pd.read_csv("amazon_product_reviews.csv")
reviews_data = df['reviews.text'].dropna()
reviews_data_polarities = predict_sentiment(reviews_data)

# Testing predict_sentiment function by calculating number of positive/negative/neutral reviews
num_negative = 0
num_neutral = 0
num_positive = 0
for polarity in reviews_data_polarities:
    if polarity < 0:
        num_negative += 1
    elif polarity == 0:
        num_neutral += 1  
    #'else' here rather than 'elif' to save computing time
    else:
        num_positive += 1  
      
print(f"Negative: {num_negative}, neutral: {num_neutral}, positive {num_positive}")
# Output: Negative: 1527, neutral: 2788, positive 30344

# Testing reviews_similarity function by comparing two reviews from the database
# Start at 10:53 - 11:00 - 7 min for 34,500 reviewa
#for testing nums of positive, negative etc - start 11:03