import pandas as pd
from random import choice
import requests

def fetch_movies(api_key, num_movies=100):
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc"
    response = requests.get(url)
    movie_data = response.json()
    return movie_data['results'][:num_movies]  # Assuming you want the top `num_movies` movies.


def get_mood():
    print("How are you feeling today?")
    mood = input("Energetic, Emotional, Light-hearted, ...: ").lower()
    return mood


def recommend_movie(movies, mood):
    # Using genres as proxy for mood, you'd need to map moods to their respective genres.
    mood_to_genre = {
        'energetic': 'Action',
        'emotional': 'Drama',
        'light-hearted': 'Comedy',
        # Add more as needed
    }
 
    genre = mood_to_genre.get(mood)
    if not genre:
        print("Sorry, I don't recognize that mood.")
        return

    df = pd.DataFrame(movies)
    suitable_movies = df[df['genre_ids'].apply(lambda x: genre in x)]  # Assuming `genre_ids` is a list.

    if suitable_movies.empty:
        print("Sorry, couldn't find a movie for that mood.")
        return

    movie = choice(suitable_movies.to_dict(orient='records'))
    print(f"How about '{movie['title']}'?")

# Execution:
api_key = "8dd6ebe96aa30b564d6e3902f40c527c"
movies = fetch_movies(api_key)
mood = get_mood()
recommend_movie(movies, mood)
