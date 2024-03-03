import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_sm')

sample = u"Build your data science skills to launch an in-demand,valuable career in six months."

doc = nlp(sample)

for word in doc:
    if word.is_stop == True:
        print(word)