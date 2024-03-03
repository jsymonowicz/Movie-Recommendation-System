Movie Recommendation System
* This code implements a movie recommendation system based on word vector similarity using the spaCy library and the 'en_core_web_md' language model. The function takes a movie description as input and returns the most similar movie title.

Usage
* Clone this repository to your local machine.
* Ensure you have Python and spaCy installed (pip install spacy).
* Download the 'en_core_web_md' language model by running python -m spacy download en_core_web_md.
* Run the program by executing python movie_recommendation.py in your terminal.
  
Input Data
* The input data is stored in the 'movies.txt' file. Each line contains a movie description without a corresponding title. The code treats each line as a movie title ('Movie A', 'Movie B', etc.) for clarity, and associates the provided description with the chosen title as an additional output.
