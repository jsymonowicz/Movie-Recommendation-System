import spacy
nlp = spacy.load('en_core_web_md')

words = nlp('cat apple monkey banana ')

# Comparing to oneself
for i_1 in words:
    for i_2 in words:
        print(i_1.text, i_2.text, i_1.similarity(i_2))