'''
----------- T20 - NLP - Semantic Similarity ------------
------------------- Practical Task 2 -------------------
This code provides a movie recommendation system based on the word vector 
similarity of the description of movies. The function takes in the
description as a parameter and returns the most similar movie.
--------------------------------------------------------
In the provided file 'movies.txt' there are no movie titles, only 'Movie A',
'Movie B' etc. Therefore, I treat these as movie titles, and for clarity
I assign a provided description to the chosen title 'Movie x' as an extra output.
----------------------- IMPORTANT -----------------------
Make sure to have installed spaCy before running this code!
'''

# Importing spaCy library and 'en_core_web_md' language model
import spacy
nlp = spacy.load('en_core_web_md')

# Movie recommendation function
## Input: movie description
## Output: title and description of the most similar movie
def movie_recommendation(input_description):
    # List for storing movie titles, descriptions, & similarity scores
    movies = []
    # Reading in 'movies.txt' file containing list of movies to be recommended
    with open('movies.txt', 'r') as file:
        for line in file:
            title, description = line.split(':', 1) # Spliting line into title (before ':') and description (after ':')
            movies.append([title, description]) # Storing title + description

    # Changing input description into nlp object
    input_doc = nlp(input_description)

    # Iterating over movies taken from 'movies.txt'
    for movie in movies:  
        description_doc = nlp(movie[1]) # Processing description into nlp doc
        similarity_score = input_doc.similarity(description_doc) # Calculating similarity
        movie.insert(2,similarity_score) # Adding similarity_score to movies list

    # Finding the highest similarity score in the list of movies
    highest_similarity = max(movies, key=lambda x: x[2])

    # Printing out title and description of the movie with the highest similarity score
    best_title = highest_similarity[0]
    best_description = highest_similarity[1]
    return(f"Title: {best_title}\nDescription: {best_description}")

# Testing the movie_recommendation function:
test_movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
most_similar_movie = movie_recommendation(test_movie_description)
print("The recommended movie is:\n", most_similar_movie)

'''
Output:
The recommended movie is:
 Title: Movie C 
Description: A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.
'''
# Checking github pull request