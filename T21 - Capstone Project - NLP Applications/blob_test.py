# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:13:12 2024

@author: Iwona
"""

# the following installations are required
# python -m textblob.download_corpora
# python -m spacy download en_core_web_sm

import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

text = 'I had a really horrible day. It was the worst day ever! But every now and then I have a really good day that makes me happy.'
doc = nlp(text)
fact1 = doc._.blob.polarity                            # Polarity: -0.125
sentiment = doc._.blob.sentiment
fact2 = doc._.blob.subjectivity                        # Subjectivity: 0.9
fact3 = doc._.blob.sentiment_assessments.assessments   # Assessments: [(['really', 'horrible'], -1.0, 1.0, None), (['worst', '!'], -1.0, 1.0, None), (['really', 'good'], 0.7, 0.6000000000000001, None), (['happy'], 0.8, 1.0, None)]
fact4 = doc._.blob.ngrams()                            # [WordList(['

print(fact1)
print(sentiment)