import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Get yesterday's date
date = datetime.now() - timedelta(days=1)
date_str = date.strftime('%Y%m%d')

# Construct URL for the NBA scoreboard page for yesterday
url = f'https://www.nba.com/scores/{date_str}'

# Send GET request to the URL
response = requests.get(url)

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div that contains the scores
scoreboard = soup.find('div', {'class': 'row scores-cards__container'})

# Get the games
games = scoreboard.find_all('div', {'class': 'card__game'})

# Loop through the games and print the scores
for game in games:
    away_team = game.find('div', {'class': 'card__team-name--away'}).text.strip()
    away_score = game.find('div', {'class': 'card__team-score--away'}).text.strip()
    home_team = game.find('div', {'class': 'card__team-name--home'}).text.strip()
    home_score = game.find('div', {'class': 'card__team-score--home'}).text.strip()

    print(f'{away_team} {away_score} - {home_team} {home_score}')