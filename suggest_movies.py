import numpy as np
import pandas as pd
import random


def suggest_movies(genre):
    try:
        df = pd.read_csv('movies1.csv')
    except FileNotFoundError:
        print("Error: movies.csv file not found. Please run the scrape_movies.py script first.")
        return

    # Clean up genres and input genre
    df['genre'] = df['genre'].str.strip().str.lower()
    genre = genre.strip().lower()

    # Filter movies by genre
    filtered_movies = df[df['genre'].str.contains(genre, na=False)]

    if filtered_movies.empty:
        print(f"No movies found for the genre: {genre}")
    else:
        # Select a random movie from the filtered list
        random_index = random.randint(0, len(filtered_movies) - 1)
        random_movie = filtered_movies.iloc[random_index]
        print(f"Random movie suggestion for the genre '{genre}':")
        print(f"Title: {random_movie['title']}")
        print(f"Link: {random_movie['link']}")

if __name__ == '__main__':
    genre = input("Enter a movie genre: ").strip()
    suggest_movies(genre)
