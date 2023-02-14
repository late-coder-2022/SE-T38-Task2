"""
This program uses spaCy language model and similarity method to compare the description of the last movie user watched
against a list of movies and descriptions. Based on the result, the movie with the highest similarity will be proposed
to user.

START
1. Import SpaCy library
2. load english language model 'en_core_web_md' into nlp.
3. Define a function taking the movie description as a parameter to compare with a list of movies; return the movie with
the highest similarity.
END
"""

import spacy

nlp = spacy.load('en_core_web_md')


# This function will compare the parameter with all the movies and return the movie with the highest similarity.
def next_movie(description):
    mov_similarity = 0
    next_mov = ""
    for mov_name, mov_desc in movie_db.items():
        mov_matching = nlp(mov_desc).similarity(description)
        if mov_matching > mov_similarity:
            mov_similarity = mov_matching
            next_mov = mov_name
    return next_mov


watched_mov_desc = nlp("""Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the 
Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.""")

# Open "movies.txt" file, read the movie names and movie descriptions and store them into movie_db dictionary.
with open("movies.txt", "r") as movie_file:
    movie_db = {}
    for movie in movie_file:
        movie_name, movie_desc = movie.strip("\n").split(" :")
        movie_db[movie_name] = movie_desc

# print out the returned result from next_movie function.
print(f"The next watching movie might be {next_movie(watched_mov_desc)}")
