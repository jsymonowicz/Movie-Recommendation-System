"""
------------------------ Task 22 ------------------------
-------------------- Practical Task 2 -------------------
------ Little Sister’s Vocabulary coding challenge ------
This code solves the challenge posted on:
https://exercism.org/tracks/python/exercises/little-sisters-vocab
"""

print("\n---------- 1. Add a prefix to a word ----------")

# Function inputs a word & returns a new 'un'-prefixed word
## I do not restrict input words, so 'unhappy' becomes ununhappy' etc.
def add_prefix_un(word):
# Ensuring correct str input:
    if not isinstance(word, str):
        raise Exception("Input must be a string.")
    return("un" + word)

# Testing the 'add_prefix_un' function
negation = add_prefix_un("happy")
print(negation)
# Output: unhappy


print("\n------- 2. Add prefixes to word groups --------")

# Function inputs list of words starting with a prefix &
# returns a string with the prefix applied to each word
def make_word_groups(vocab_words):
# Ensuring correct input
    if not isinstance(vocab_words, list):
        raise Exception("Input must be a list.")
    prefix_list = ["en", "pre", "auto", "inter"]
    if vocab_words[0] not in prefix_list:
        raise Exception("The first word in the input list must be a prefix.")
# Adding a prefix
    prefix = vocab_words[0]
    words = vocab_words[1:]
    word_groups = [prefix] + [prefix + word for word in words]
    return(' :: '.join(word_groups))

# Testing the 'make_word_groups' function
vocab_words = ['inter', 'twine', 'connected', 'dependent']
print(make_word_groups(vocab_words))
# Output: inter :: intertwine :: interconnected :: interdependent


print("\n------- 3. Remove a suffix from a word --------")

# Function inputs a word & returns the root word without the 'ness' suffix
def remove_suffix_ness(word):
# Ensuring correct input: str ending with 'ness'
    if not isinstance(word, str):
        raise Exception("Input must be a string.")
    if word[-4:] != "ness":
        raise Exception("Input word must end with 'ness'")
# Removing 'ness'
    return(word[:-4])

# Testing of the 'remove_suffix_ness' function
print(remove_suffix_ness("sadness"))
# Output: sad


print("\n------- 4. Extract and transform a word -------")

# Function inputs a sentence and the index of the adjective to be altered &
# returns the extracted adjective as a verb created by adding the 'en' suffix
def adjective_to_verb(sentence, index):
# Ensuring str input
    if not isinstance(sentence, str):
        raise Exception("Input must be a string.")
# Split the sentence
    splitted = sentence.split(' ')
# Choose the adjective
    adjective = splitted[index]
# Removing punctuation
    punctuation = [".", ",","!",":","?","-", "'"]
    clean_adjective = ""
    for letter in adjective:
        if letter not in punctuation:
            clean_adjective += letter
# Add -en suffix
    clean_adjective += "en"
    return clean_adjective

# Testing of the 'remove_suffix_ness' function
sentence_1 = adjective_to_verb("I'm in the need: to make, that bright.", -1 )
print(sentence_1)
# Output: brighten
sentence_2 = adjective_to_verb("It's got dark as the sun set.", 2)
print(sentence_2)
# Output: darken