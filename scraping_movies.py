!pip install requests beautifulsoup4 

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_movies():
    url = 'https://editorial.rottentomatoes.com/guide/essential-movies-to-watch-now/'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception('Failed to load page')
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []
    for movie_section in soup.find_all('div', class_='article_movie_title'):
        movie_title = movie_section.a.text.strip()
        movie_link = movie_section.a['href']
        # Accessing the individual movie page to scrape genre
        movie_response = requests.get(movie_link)
        movie_soup = BeautifulSoup(movie_response.text, 'html.parser')
        genre = 'Unknown'
        try:
            # Search for genre in different possible locations
            genre_tags = movie_soup.find_all('span', class_='genre')
            if genre_tags:
                genre = ', '.join([tag.text.strip() for tag in genre_tags])
            else:
                # Try to find genre in a different location
                details_section = movie_soup.find('ul', class_='content-meta info')
                if details_section:
                    genre_tag = details_section.find('li', class_='meta-row clearfix')
                    if genre_tag:
                        genre = genre_tag.text.strip().replace('Genre:', '')
        except AttributeError:
            pass
        movies.append({
            'title': movie_title,
            'link': movie_link,
            'genre': genre
        })
    # Save the data to a CSV file
    df = pd.DataFrame(movies)
    df.to_csv('movies.csv', index=False)
    print("Data has been scraped and saved to movies.csv")

if __name__ == '__main__':
    scrape_movies()

a = pd.read_csv('movies.csv')
a.drop('genre', axis=1, inplace=True)

g = pd.read_csv('Genre.csv')

movies1 = a.merge(g) 
print(movies1)