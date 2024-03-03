import spacy

nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("bananas")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word3.similarity(word4))