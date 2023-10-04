from bs4 import BeautifulSoup
import requests
import numpy as np
import random
import math
import pandas as pd
from io import StringIO
import time
from datetime import date
import os, sys
import re
import string

team_abbreviations = {
	'Oakland Athletics': 'OAK',
	'New York Yankees': 'NYY',
	'Colorado Rockies': 'COL',
	'Pittsburgh Pirates': 'PIT',
	'Detroit Tigers': 'DET',
	'Cleveland Guardians': 'CLE',
	'Los Angeles Dodgers': 'LAD',
	'Milwaukee Brewers': 'MIL',
	'Miami Marlins': 'MIA',
	'Arizona Diamondbacks': 'AZ',
	'Texas Rangers': 'TEX',
	'Seattle Mariners': 'SEA',
	'Washington Nationals': 'WSH',
	'San Francisco Giants': 'SF',
	'Toronto Blue Jays': 'TOR',
	'Philadelphia Phillies': 'PHI',
	'Houston Astros': 'HOU',
	'Los Angeles Angels': 'LAA',
	'Tampa Bay Rays': 'TB',
	'Baltimore Orioles': 'BAL',
	'New York Mets': 'NYM',
	'Cincinnati Reds': 'CIN',
	'Boston Red Sox': 'BOS',
	'Atlanta Braves': 'ATL',
	'St. Louis Cardinals': 'STL',
	'Chicago Cubs': 'CHC',
	'Chicago White Sox': 'CWS',
	'Kansas City Royals': 'KC',
	'San Diego Padres': 'SD',
	'Minnesota Twins': 'MIN'
}

url = 'https://www.baseball-reference.com/boxes/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
names = (soup.find(class_="game_summaries")).find_all('a')
scores = (soup.find(class_="game_summaries")).find_all(class_ = 'right')
teams = []
print(names)
for i in names:

	try:
		if i.text != 'Final':
			teams.append(i.text)
	except:
		if i != 'Final':
			teams.append(i)
numbers = []
for i in scores:
	try:
		numbers.append(float(i.text))
		
	except:
		pass
		
scoreDict = {}
counter = 0
for i in teams:
	counter += 1
	scoreDict[team_abbreviations[i]] = numbers[counter - 1]

print(scoreDict)

with open('MLBscoresForTraining.txt', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
with open("MLBscoresForTraining.txt", "a") as o:
	o.write("," + str(scoreDict) + ']')