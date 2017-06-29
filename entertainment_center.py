"""Stores details of movies and displays them on a website."""
import fresh_tomatoes

import media


def main():

    """Movies."""
movie_title = "Transformers: The Last Knight"
movie_storyline = "Transformers keep coming back to Earth."
poster_imagePart = "https://upload.wikimedia.org/wikipedia/en/2/26/"
poster_imagePart2 = "Transformers_The_Last_Knight_poster.jpg"
poster_image = poster_imagePart + poster_imagePart2
trailer_youtube = "https://www.youtube.com/watch?v=lQqhfq87FgY"
movie_release_date = "June 21, 2017"

optimus = media.Movie(movie_title, movie_storyline, poster_image,
                      trailer_youtube, movie_release_date)

movie_title = "The Matrix"
movie_storyline = "The world is a simulation and Neo have super powers"
poster_imagePart = "https://upload.wikimedia.org/wikipedia/en/c/c1/"
poster_imagePart2 = "The_Matrix_Poster.jpg"
poster_image = poster_imagePart + poster_imagePart2
trailer_youtube = "https://www.youtube.com/watch?v=vKQi3bBA1y8"
movie_release_date = "March 31, 1999"

matrixx = media.Movie(movie_title, movie_storyline, poster_image,
                      trailer_youtube, movie_release_date)

movie_title = "Wonder Woman (2017 film)"
movie_storyline = "Wonder Woman is a 2017 American superhero film"
poster_imagePart = "https://upload.wikimedia.org/wikipedia/en/e/ed/"
poster_imagePart2 = "Wonder_Woman_%282017_film%29.jpg"
poster_image = poster_imagePart + poster_imagePart2
trailer_youtube = "https://www.youtube.com/watch?v=1Q8fG0TtVAY"
movie_release_date = "June 2, 2017"

tWonder_Woman = media.Movie(movie_title, movie_storyline, poster_image,
                            trailer_youtube, movie_release_date)

# Store the Movie objects in a list.
movies = [optimus, matrixx, tWonder_Woman]

# Open the movie website in the user's browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
