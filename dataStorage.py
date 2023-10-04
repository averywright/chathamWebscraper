from bs4 import BeautifulSoup
import requests
import numpy as np
import random
import math
import time
import pandas as pd
from io import StringIO
import time
from datetime import date

link = "https://www.basketball-reference.com/teams/" + 'NOH' + "/stats_per_game_totals.html"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
text_table = soup.find('table', id='stats')
headers = []
for i in text_table.find_all('td'):
    title = i.text
    headers.append(title)
team_stats = []
team_stats.append(1)
team_stats.append(headers[4])
for i in range(6, 33):
    if i == 7:
        g = list(headers[i])
        g[1] = '.'
        team_stats.append("".join(g))
    elif i != 9 and i != 10:
        team_stats.append(headers[i])
time.sleep(5)
link = "https://www.basketball-reference.com/teams/" + 'ATL' + "/opp_stats_per_game_totals.html"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
text_table = soup.find('table', id='stats')
headers = []
for i in text_table.find_all('td'):
    title = i.text
    headers.append(title)
team_stats.append(headers[4])
for i in range(6, 29):
    if i != 8 and i != 9:
        team_stats.append(headers[i])

print(team_stats)