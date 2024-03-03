'''
# ----------- T20 - NLP - Semantic Similarity ------------
# ------------------- Practical Task 1 -------------------
# This code follows steps 1-3 from Practical Task 1 in '14-002 NLP - 
# Semantic Similarity.pdf' from the Dropbox folder.
# ----------------------- IMPORTANT -----------------------
# Make sure to have installed spaCy before running this code!
'''

# Importing spaCy library and 'en_core_web_md' language model
import spacy
nlp = spacy.load('en_core_web_sm')

# ----------- STEP 1 -----------
# Run all the code extracts copied from '14-002 NLP - Semantic Similarity.pdf'

# SIMILARITY WITH SPACY
print("\n-----------Comparing two words-------------")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("BANANA")
print(f"{word1} & {word2}: {word1.similarity(word2)}")
print(f"{word3} & {word2}: {word3.similarity(word2)}")
print(f"{word3} & {word1}: {word3.similarity(word1)}")
print(f"{word3} & {word4}: {word3.similarity(word4)}")

# WORKING WITH VECTORS
print("\n-----------Comparing each word with one another-------------")
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    print(f"Comparing \x1B[4m{token1}\x1B[0m with other words:")
    for token2 in tokens:
        print(f"{token1.text} & {token2.text}: {token1.similarity(token2)}")

# WORKING WITH SENTENCES
print("\n--------Comparing a sentence with other sentences----------")
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
    ]
sentence_to_compare = nlp("Why is my cat on the car")
print(f"The compared sentence is: \x1B[4m{sentence_to_compare}\x1B[0m")
print("Similarities with other sentences are:")
for s in sentences:
    similarity = nlp(s).similarity(sentence_to_compare)
    print(f"{s} - {similarity}")

# ----------- STEP 2 -----------
# Write a note on what you noticed about the similarities between cat,
# monkey and banana and think of an example of your own.

# What I noticed about the similarities between cat, monkey and banana:
'''
Output:
    cat & monkey: 0.5929929614067078
    cat & banana: 0.2235882729291916
    monkey & banana: 0.404150128364563
Conclusions:
    * Cat & monkey are most similar because they are both animals.
    * Monkey & banana are more similar than cat & banana because, unlike cats, monkeys eat bananas.
'''
 
# My own example: comparing a word and its capitalized and plural forms:
print("\n------Similarity varying capitalization and plural--------")
word1 = nlp("banana")
word2 = nlp("bANAna")
word3 = nlp("bananas")
word4 = nlp("BANANA")
print(f"{word1} & {word2}: {word1.similarity(word2)}")
print(f"{word1} & {word3}: {word1.similarity(word3)}")
print(f"{word1} & {word4}: {word1.similarity(word4)}")
print(f"{word3} & {word4}: {word3.similarity(word4)}")
'''
Output:
    banana & bANAna: 0.0 # UserWarning: [W008] Evaluating Doc.similarity based on empty vectors.
    banana & bananas: 0.8712358421094191
    banana & BANANA: 0.043644862651088225
    bananas & BANANA: -0.016033276744078822
My conclusions:
    * Capitalization of letters matters in NLP.
    * SpaCy is bad in recognizing the same word with capitalized letters.
    * For the same word with some letters capitalized the compared vectors are empty (UserWarning: [W008]).
    * Negative similarity is possible, obtained for 'bananas' & 'BANANA'.
    * Checked online: similarity < 0 occurs when the vectors are orthogonal or nearly orthogonal, meaning they point in opposite or very different directions in the vector space.
'''

# ----------- STEP 3 -----------
# Run the example file on with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice may be different from the model 'en_core_web_md'
'''
Comment: From instructions it is not clear where I should write the note so I
am writing it in this file and not in the modified semanticsimilarity_example.py

My note:
    * With ‘en_core_web_sm’ all similarity values are lower by 0.1-0.35 compared to 'en_core_web_md'.
    * With 'sm' I often get UserWarning: [W007] which recognizes limitationg of this model
I also tested changing 'en_core_web_md' to ‘en_core_web_sm’ in this code
The conclusions are:
    *
'''