# ----------- T19 - Natural Language Processing -----------
# This code follows instructions of Practical Task 1 from the
# 'T19 - Natural Language Processing' Dropbox folder of Data Science Bootcamp.

# ----------------------- IMPORTANT -----------------------
# Make sure to have installed spaCy before running this code!

# Import the spaCy library for Natural Language Processing
import spacy
# Loading the English language model provided by spaCy
nlp = spacy.load('en_core_web_sm')

# Providing my two garden path sentences
gardenpathSentences = [
    "The young man the Titanic.",
    "The complex houses married priests and their 50 Russian families."
    ]

# Adding sentences to the gardenpathSentences list:
new_sentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi, 100."
    ]
gardenpathSentences.extend(new_sentences)

# Tokenizing each sentence in gardenpathSentences &  performing named entity recognition (NER)
## Creating new lists to store tokens and NER outcome:
gardenpathSentences_tokens = [] # Tokens
gardenpathSentences_NER = [] # NER
## Iterating over sentences in gardenpathSentences:
for sentence in gardenpathSentences:
    doc = nlp(sentence) # Turning each sentence into class 'spacy.tokens.doc.Doc'
    tokens = [token.orth_ for token in doc] # Tokenization
    gardenpathSentences_tokens.append(tokens) # Storing tokens in gardenpathSentences_tokens
    NER = [(ent.text, ent.label_, ent.label) for ent in doc.ents] # Named entity recognition
    gardenpathSentences_NER.append(NER) # Storing NER outcome in gardenpathSentences_NER

# Examining how spaCy has categorized each sentence
print("Original list:")
print(gardenpathSentences)
print("\nTokenized list:")
print(gardenpathSentences_tokens)
print("\nList with named entity recognition (NER):")
print(gardenpathSentences_NER)

# Labeling entities found and stored in gardenpathSentences_NER
NER_dict = {} # Creating a dictionary for storing NER labels
for sentence in gardenpathSentences_NER: # Entering each analized sentence 
    for ent in sentence: # Entering each entity
        if ent[1] not in NER_dict:  # Checking if entity's label_ is already in the dictionary
            NER_dict[ent[1]] = spacy.explain(ent[1]) # Add label & explanation to dictionary
print("\nDictionary explaining used NER labels:")
print(NER_dict)

'''
Instruction:
    
At the bottom of your file, write a comment about two entities that you looked up.
For each entity answer the following questions:
1. What was the entity and its explanation that you looked up?
2. Did the entity make sense in terms of the word associated with it?

Answers:
    
Sentence 1: "The young man the Titanic."
1. Entity found was 'ORG' for the word 'Titanic'.
* 'ORG' stands for: 'Companies, agencies, institutions, etc.'
2. The ORG entity does not make sense here because
Titanic was not an agency but the specific name of the ship.

Sentence 2: "The complex houses married priests and their 50 Russian families."
1. Entity found was 'NORP' for the word 'Russian'.
* 'NORP' stands for: 'Nationalities or religious or political groups'.
2. The NORP entity makes sense here because
Russians are used to define nationality.
'''