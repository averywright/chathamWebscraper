import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.baseball-reference.com/teams/ATL/batteam.shtml#yby_team_bat'
page = requests.get(url)
soup = bs(page.content, 'html.parser')
script = soup.find('tbody')
x = script.findAll('data-stat= \"runs_per_game\"')
print(x)

