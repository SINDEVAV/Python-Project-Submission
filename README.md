# Movie Suggestion App

## Overview

The Movie Suggestion App is a Python project that suggests a random movie based on a user-input genre. The project involves web scraping, data processing with Pandas, and implementing a suggestion system. The data is scraped from Rotten Tomatoes and saved in a CSV file, which is then used to suggest a movie.

## Features

- **Web Scraping**: Uses BeautifulSoup to scrape movie data from Rotten Tomatoes.
- **Data Processing**: Utilizes Pandas to clean and process the scraped data.
- **Random Movie Suggestion**: Suggests a random movie from a user-specified genre.
- **Error Handling**: Ensures smooth execution with proper error handling.

## Requirements

- Python 3.x
- Pandas
- BeautifulSoup4
- Requests
- lxml (optional)

## Installation

    ```

1. **Install the Required Libraries**:
    ```bash
    pip install pandas beautifulsoup4 requests lxml
    ```

## Usage

### Scrape Movies

1. **Run the Scraping Script**:
    ```bash
    python scrape_movies.py
    ```

    This script will scrape movie data from Rotten Tomatoes and save it into a CSV file named `movies.csv`.
	Since, genres could not be scraped from the website, genres are manually added to the 'movies.csv' file through 'merge' function. 

### Suggest a Movie

2. **Run the Suggestion Script**:
    ```bash
    python suggest_movies.py
    ```

    You will be prompted to enter a movie genre. The script will then suggest a random movie from the specified genre.

## Project Structure

- `scrape_movies.py`: Script to scrape movie data from Rotten Tomatoes.
- `suggest_movies.py`: Script to suggest a random movie based on a user-input genre.
- `movies.csv`: CSV file containing the scraped movie data.

## Example

After running `scrape_movies.py`, you can run `suggest_movies.py` and input a genre:

```bash
Enter a movie genre: action
Random movie suggestion for the genre 'action':
Title: Black Panther
Link: https://www.rottentomatoes.com/m/black_panther
