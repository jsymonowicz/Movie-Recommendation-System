import spacy #This statement should work if you have spaCy installed 
nlp = spacy.load('en_core_web_sm')

# Define word
sample = u"Build, your data science skills to launch an in-demand,valuable career in six months."

doc = nlp(sample)

# Tokenisation------------------------------------------------------------------
[token.orth_ for token in doc]
#print([(kot, kot.orth_, kot.orth) for kot in doc])
#print([token.orth_ for token in doc if not token.is_punct | token.is_space])


for word in doc:
    if word.is_punct == True:
        print(word.orth_ )
    
print('###### Next: ########')

# Let's identify stop words:
for word in doc:
    if word.is_stop == True:
        print(word)
       
# Lemmatisation -------------------------------------------------------------
# Reducing a word to its base form
# Why is this useful? - good for text classification
# avoids word duplication thus allows for modeling a clearer picture of patterns of word usage.
print('########  Lemmatisation  ########')

phrase = "go going went gone"
nlp_practice = nlp(phrase)
print([kot.lemma_ for kot in nlp_practice])


# Named entity recognition -------------------------------------------------------------

# Classifying named entities into pre-defined categories, such as persons, places, dates
# https://spacy.io/usage/linguistic-features#named-entities).

import spacy

#First example - from the link above
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
doc2 = nlp("Apples, oranges, plums.")

for i in doc.ents:
    print(i.text, i.start_char, i.end_char, i.label_)

#.ents - access the identified entities
# .label_ and .label - additional token methods accessed after .ents method
 

wiki_priyanka = """Oragnes are delicious fruits. She is known by her married name Priyanka Chopra Jonas,
is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards.
In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential
people in the world."""

# Get labels and entities and print them
nlp_priyanka = nlp(wiki_priyanka)
#print([(i, i.label_, i.label) for i in nlp_priyanka.ents])

for i in nlp_priyanka.ents:
    print(i, i.label_)
    entity_fac = spacy.explain(i.label_)
    print(f"{i.label_}:{entity_fac}")

# Get an explanation of an entity and print it
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")