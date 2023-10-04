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

def remove_duplicates(lst):
    """
    Given a list, remove duplicate indices by deleting the second occurrence of each duplicate index.

    Args:
    - lst: a list

    Returns:
    - a list with duplicates removed
    """
    seen = set()
    result = []
    for i in lst:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result


mlb_stadiums = {
    "ARI": [335, 407, 335, 166, 191, 171],
    "ATL": [335, 400, 325, 167, 197, 162],
    "BAL": [333, 400, 318, 194, 211, 219],
    "BOS": [310, 379, 302, 146, 171, 157],
    "CHC": [355, 400, 353, 162, 154, 135],
    "CWS": [330, 400, 335, 156, 165, 172],
    "CIN": [328, 404, 325, 158, 181, 173],
    "CLE": [325, 405, 325, 170, 196, 158],
    "COL": [347, 415, 350, 129, 152, 148],
    "DET": [345, 420, 330, 172, 187, 160],
    "HOU": [315, 409, 326, 148, 175, 163],
    "KC": [330, 410, 330, 157, 187, 177],
    "LAA": [347, 396, 347, 143, 175, 147],
    "LAD": [330, 395, 330, 162, 177, 137],
    "MIA": [344, 418, 335, 120, 146, 137],
    "MIL": [344, 400, 345, 149, 165, 163],
    "MIN": [328, 400, 327, 148, 198, 143],
    "NYM": [335, 408, 330, 144, 156, 163],
    "NYY": [318, 408, 314, 153, 174, 151],
    "OAK": [330, 400, 330, 144, 174, 135],
    "PHI": [329, 401, 330, 133, 172, 135],
    "PIT": [325, 399, 320, 132, 154, 137],
    "SD": [336, 396, 322, 167, 180, 156],
    "SF": [339, 399, 309, 122, 138, 109],
    "SEA": [331, 405, 326, 152, 168, 142],
    "STL": [336, 400, 335, 138, 179, 157],
    "TB": [315, 404, 370, 136, 162, 128],
    "TEX": [332, 400, 325, 157, 183, 165],
    "TOR": [328, 400, 375, 120, 136, 109],
    "WSH": [335, 402, 335, 157, 192, 146]
}

stadium_directions = {
    'ATL': 22.5,
    'WSH': 22.5,
    'SF': 247.5,
    'NYY': 22.5,
    'BAL': 22.5,
    'BOS': 22.5,
    'MIL': 337.5,
    'CHC': 337.5,
    'DET': 22.5,
    'TB': 22.5,
    'PHI': 22.5,
    'TEX': 202.5,
    'PIT': 292.5,
    'CIN': 292.5,
    'TOR': 22.5,
    'STL': 337.5,
    'MIN': 202.5,
    'KC': 202.5,
    'NYM': 22.5,
    'MIA': 22.5,
    'CWS': 157.5,
    'HOU': 202.5,
    'COL': 192.5,
    'SD': 247.5,
    'LAA': 247.5,
    'OAK': 292.5,
    'ARI': 292.5,
    'LAD': 247.5,
    'CLE': 202.5,
    'SEA': 292.5
}

city_mascot_dict = {
	'ATL': 'braves',
	'WSH': 'nationals',
	'SF': 'giants',
	'NYY': 'yankees',
	'BAL': 'orioles',
	'BOS': 'redsox',
	'MIL': 'brewers',
	'CHC': 'cubs',
	'DET': 'tigers',
	'TB': 'rays',
	'PHI': 'phillies',
	'TEX': 'rangers',
	'PIT': 'pirates',
	'CIN': 'reds',
	'TOR': 'bluejays',
	'STL': 'cardinals',
	'MIN': 'twins',
	'KC': 'royals',
	'NYM': 'mets',
	'MIA': 'marlins',
	'CWS': 'whitesox',
	'HOU': 'astros',
	'COL': 'rockies',
	'SD': 'padres',
	'LAA': 'angels',
	'OAK': 'athletics',
	'AZ': 'd\'backs',
	'LAD': 'dodgers',
	'CLE': 'guardians',
	'SEA': 'mariners'
}
english_pattern = re.compile(r'^[a-zA-Z]+$')

def extract_name(input_string):
	start_index = input_string.find('/player/') + len('/player/')
	end_index = input_string.find('-', start_index)
	if end_index == -1:
		end_index = input_string.find('"', start_index)
	name = input_string[start_index:end_index].replace('-', ' ').title()

	# Extract last name from href attribute
	end_index = input_string.find('-', end_index) + 1
	if end_index == -1:
		end_index = input_string.find('"', start_index)
	last_name = input_string[end_index:end_index+5].replace('-', ' ').title()

	full_name = name + ' ' + last_name
	return full_name

url = "https://www.mlb.com/schedule"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
soupTwo = soup.find('div',"ScheduleCollectionGridstyle__SectionWrapper-sc-c0iua4-0 guIOQi")
text_table = soupTwo.find_all('div',"TeamWrappersstyle__MobileTeamWrapper-sc-uqs6qh-1 IESfj")
headers = []
for i in text_table:
	title = i.text
	headers.append(title)

headers = remove_duplicates(headers)
pitching_stats = {}
for i in headers:
	if i == "WSH":
		i = 'WSN'
	if i == 'AZ':
		i = 'ARI'
	if i == 'CWS':
		i = 'CHW'
	url = 'https://www.baseball-reference.com/teams/' + i + '/2023.shtml'
	time.sleep(5)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	table = []
	stats = []
	counter = 0
	try:
		table = soup.find_all('tfoot')[1]
		tableTwo = table.find_all('td')
		for j in tableTwo:
			counter += 1
			if j.text != "Team Totals":
				stats.append(j.text)
	except:
		print(i)
	pitching_stats[i] = stats

print('3')

playerInfo = []
url = 'https://www.baseball-reference.com/previews/'
time.sleep(5)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
textTables = soup.find(class_="game_summaries")
for i in (textTables.find_all('div')):
	count = 0
	temp = ((i.find_all('tr')))
	if len(temp) == 4:
		for j in temp:
			for k in (j.find_all('a')):
				if k.text != 'Preview':
					if k.get('href') != '':
						count += 1
	if count == 4:
		for j in temp:
			for k in (j.find_all('a')):
				if k.text != 'Preview':
					playerInfo.append(k)

del textTables

teamAndPitcher = {}
counter = 0
for i in playerInfo:
	fruit = i.text
	counter += 1
	if (counter - 1) % 4 == 0:
		teamAndPitcher[fruit] = ''
		slotOne = fruit
	elif (counter - 2) % 4 == 0:
		teamAndPitcher[fruit] = ''
		slotTwo = fruit
	elif (counter - 3) % 4 == 0:
		fruit = i.get('href')
		teamAndPitcher[slotOne] = fruit
	else:
		fruit = i.get('href')
		teamAndPitcher[slotTwo] = fruit

for k in teamAndPitcher:
	temp = []
	url = teamAndPitcher[k]
	time.sleep(5)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	counter = 0
	try:
		for i in (soup.find('tbody').find(id="pitching_standard.2023")).find_all('td'):
			if counter != 1 and counter != 2:
				temp.append(i.text)
			counter += 1
		teamAndPitcher[k] = temp
	except:
		teamAndPitcher[k] = ''

newPitchers = {}
for i in teamAndPitcher:
	for j in city_mascot_dict:
		if i.lower() == city_mascot_dict[j]:
			newPitchers[j] = teamAndPitcher[i]

del teamAndPitcher
			
print('4')

totals = []
count = 0
for i in headers:
	count += 1
	x = city_mascot_dict[i]
	if x == 'd\'backs':
		x = 'dbacks'
	url = 'https://www.mlb.com/' + x + '/roster/starting-lineups'
	print(url)
	time.sleep(5)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	soupTwo = soup.find('div','starting-lineups__matchup')
	text_table = soupTwo.find(class_="starting-lineups__teams starting-lineups__teams--sm starting-lineups__teams--xl").find_all('ol')
	counter = 0
	player_list = []
	for i in text_table:
		counter += 1
		if count % 2 != 0:
			if counter > 1:
				break
		else:
			if counter < 2:
				continue
		player_list.append(i.text)

	player_list = player_list[0].strip()

	# Split the string into individual lines
	player_lines = player_list.split('\n')

	# Extract only the player names and concatenate them with commas
	player_names = []
	try:
		for line in player_lines:
			name_parts = line.split(' ')
			if name_parts[2] == 'Jr.':
				# If the name has a suffix (e.g. Jr.), keep it
				player_names.append(name_parts[0] + ' ' + name_parts[1] + ' ' + name_parts[2])
			else:
				player_names.append(name_parts[0] + ' ' + name_parts[1])
	except:
		error = True
	totals.append(player_names)

team_starting_dict = {team: pitcher for pitcher, team in zip(totals, headers)}


batting_dict = team_starting_dict
temp = ''
for i in team_starting_dict:
	time.sleep(5)
	temp = i
	if i == 'WSH':
		i = "WSN"
	if i == 'CWS':
		i = 'CHW'
	if i == 'KC':
		i = 'KC'
	if i == 'AZ':
		i = 'ARI'
	url = 'https://www.baseball-reference.com/teams/' + i + '/2023.shtml#team_batting'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	text_table = soup.find("table", id = "team_batting")
	count = 0
	battingTemp = []
	for j in text_table.find_all('tr'):
		count += 1
		for k in j.find_all('td'):
			battingTemp.append(k.text)
		if count > 9:
			break
	batting_dict[temp] = battingTemp

def bruh(player_stats):
	for i, stat in enumerate(player_stats):
		if any(c.isalpha() for c in stat) and not ('#' in stat or '*' in stat):
			player_stats[i] = '0'
		elif '#' in stat:
			player_stats[i] = '2'
		elif '*' in stat:
			player_stats[i] = '1'
	return player_stats

temp = batting_dict
for i in temp:
	batting_dict[i] = bruh(temp[i])

del batting_dict

print('5')

empty_slate = team_starting_dict

counter = 0

def find_all(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub)


for m in empty_slate:
	print(m)
	my_list = team_starting_dict[m]
	empty_slate[m] = []
	if m == 'WSH':
		m = "WSN"
	if m == 'CWS':
		m = 'CHW'
	if m == 'KC':
		m = 'KC'
	if m == 'AZ':
		m = 'ARI'
	url = 'https://www.baseball-reference.com/teams/' + m + '/2023.shtml'
	time.sleep(5)
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	table = soup.find(id="team_batting")
	tableTwo = table.find_all('tr')
	if m == 'WSN':
		m = "WSH"
	if m == 'CHW':
		m = 'CWS'
	if m == 'ARI':
		m = 'AZ'
	count = 0
	hrefs = {}
	for i in tableTwo:
		count += 1
		if count > 16:
			break
		counter = 0
		for j in i.find_all('td'):
			counter += 1
			if counter == 2:
				hrefs[str(j.find('a').text)] = str(j.find('a').get('href'))
	
	for i in hrefs:
		print(i)
		url = 'https://www.baseball-reference.com/' + hrefs[i] + '#batting_advanced'
		time.sleep(5)
		page = requests.get(url)
		soup = BeautifulSoup(page.content, 'html.parser')
		start = (list(find_all(str(soup), "<tr id=\"batting_advanced.2023\"")))
		end = (list(find_all(str(soup), "</tr>")))
		finalEnd = 0
		for j in end:
			if int(j) > start[0]:
				finalEnd = j
				break
		tables = []
		count = 0
		for k in start:
			count += 1
			counter = 0
			newSoup = ''
			for i in (str(soup)):
				counter += 1
				if counter >= k and counter <= finalEnd:
					newSoup += i
			tables.append(newSoup)
		
		stats = []
		soup = BeautifulSoup(tables[0], 'html.parser')
		count = 0
		for j in (soup.find_all('td')):
			count += 1
			if count != 2 and count != 3:
				stats.append(j.text)
		for j in stats:
			empty_slate[m].append(j)


print(empty_slate)

# Your OpenWeatherMap API key
api_key = "62b3d7333daab23975263c0d56992167"

# Dictionary to store weather data for each MLB city
mlb_weather = {}

# List of MLB cities and their latitude and longitude coordinates
mlb_cities = {
	'ARI': (33.445, -112.066),
	'ATL': (33.755, -84.39),
	'BAL': (39.283, -76.621),
	'BOS': (42.346, -71.097),
	'CHC': (41.948, -87.655),
	'CWS': (41.829, -87.633),
	'CIN': (39.097, -84.506),
	'CLE': (41.495, -81.685),
	'COL': (39.756, -104.993),
	'DET': (42.339, -83.049),
	'HOU': (29.757, -95.355),
	'KC': (39.048, -94.484),
	'LAA': (33.800, -117.882),
	'LAD': (34.073, -118.240),
	'MIA': (25.778, -80.220),
	'MIL': (43.028, -87.971),
	'MIN': (44.981, -93.277),
	'NYM': (40.758, -73.843),
	'NYY': (40.829, -73.926),
	'OAK': (37.751, -122.200),
	'PHI': (39.905, -75.166),
	'PIT': (40.447, -80.006),
	'SD': (32.707, -117.157),
	'SF': (37.778, -122.389),
	'SEA': (47.591, -122.333),
	'STL': (38.623, -90.185)
}

weather_data = {}
# Loop through each city in the list and get the current weather data from OpenWeatherMap
for city, coords in mlb_cities.items():
	lat, lon = coords
	# Make a request to OpenWeatherMap API for the current weather in the city
	response = requests.get(
		f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric")
	if response.status_code == 200:
		# Extract the relevant data from the API response
		data = response.json()
		current_temp = data["main"]["temp"]
		feels_like = data["main"]["feels_like"]
		min_temp = data["main"]["temp_min"]
		max_temp = data["main"]["temp_max"]
		pressure = data["main"]["pressure"]
		humidity = data["main"]["humidity"]
		wind_speed = data["wind"]["speed"]
		wind_dir = data["wind"]["deg"]
		visibility = data.get("visibility", "N/A")
		uv_index = data.get("uvi", "N/A")
		rain = data.get("rain", {}).get("1h", 0)
		# Add the weather data to the dictionary
		weather_data[city] = {"Current Temp": current_temp,
							  "Feels Like": feels_like,
							  "Min Temp": min_temp,
							  "Max Temp": max_temp,
							  "Pressure": pressure,
							  "Humidity": humidity,
							  "Wind Speed": wind_speed,
							  "Wind Direction": wind_dir,
							  "Rain (last hour)": rain}
	else:
		# If the API call fails, print an error message
		print(f"Failed to retrieve weather data for {city}")


# Print the weather data for each MLB city
def extract_numbers(d):
	numbers = []
	for key, value in d.items():
		if isinstance(value, (int, float)):
			numbers.append(value)
	return numbers


for i in weather_data:
	weather_data[i] = extract_numbers(weather_data[i])

print('6')
print(newPitchers)
print(weather_data)
print(mlb_stadiums)
print(pitching_stats)
print(stadium_directions)
print(empty_slate)
total_stats = {}
for i in newPitchers:
	total_stats[i] = []
	for j in newPitchers[i]:
		total_stats[i].append(j)
	if i == 'AZ':
		try:
			for j in weather_data['ARI']:
				total_stats[i].append(j)
		except:
			print('2')
		try:
			for j in mlb_stadiums['ARI']:
				total_stats[i].append(j)
		except:
			print('3')
		try:
			for j in empty_slate['ARI']:
				total_stats[i].append(j)
		except:
			print('4')
		try:
			for j in stadium_directions['ARI']:
				total_stats[i].append(j)
		except:
			print('5')
		try:
			for j in pitching_stats['ARI']:
				total_stats[i].append(j)
		except:
			print('6')
	elif i == 'WSH':
		try:
			for j in weather_data['WSN']:
				total_stats[i].append(j)
		except:
			print('2')
		try:
			for j in mlb_stadiums['WSN']:
				total_stats[i].append(j)
		except:
			print('3')
		try:
			for j in empty_slate['WSN']:
				total_stats[i].append(j)
		except:
			print('4')
		try:
			for j in stadium_directions['WSN']:
				total_stats[i].append(j)
		except:
			print('5')
		try:
			for j in pitching_stats['WSN']:
				total_stats[i].append(j)
		except:
			print('6')
	elif i == 'CWS':
		try:
			for j in weather_data['CHW']:
				total_stats[i].append(j)
		except:
			print('2')
		try:
			for j in mlb_stadiums['CHW']:
				total_stats[i].append(j)
		except:
			print('3')
		try:
			for j in empty_slate['CHW']:
				total_stats[i].append(j)
		except:
			print('4')
		try:
			for j in stadium_directions['CHW']:
				total_stats[i].append(j)
		except:
			print('5')
		try:
			for j in pitching_stats['CHW']:
				total_stats[i].append(j)
		except:
			print('6')
	try:
		for j in weather_data[i]:
			total_stats[i].append(j)
	except:
		print('2')
	try:
		for j in mlb_stadiums[i]:
			total_stats[i].append(j)
	except:
		print('3')
	try:
		for j in empty_slate[i]:
			total_stats[i].append(j)
	except:
		print('4')
	try:
		for j in stadium_directions[i]:
			total_stats[i].append(j)
	except:
		print('5')
	try:
		for j in pitching_stats[i]:
			total_stats[i].append(j)
	except:
		print('6')
del newPitchers
del weather_data
del mlb_stadiums
del empty_slate
del stadium_directions
del pitching_stats

temp = {}
for i in total_stats:
	temp[i] = total_stats[i]
	total_stats[i] = []
print(temp)
for i in temp:
	counter = 0
	for j in temp[i]:
		counter += 1
		if counter < len(temp[i]):
			if j != 'Rank in 15 AL teams' and j != 'Rank in 15 NL teams' and j != 'NL' and j != 'AL' and temp[i][
				counter] != 'NL' and temp[i][counter] != 'AL':
				if j == '':
					total_stats[i].append(0)
				else:
					newString = ''
					for k in str(j):
						if k != '%':
							newString += k
					total_stats[i].append((float(newString)))
		
		else:
			if j != 'Rank in 15 AL teams' and j != 'Rank in 15 NL teams' and j != 'NL' and j != 'AL':
				if j == '':
					total_stats[i].append(0)
				else:
					newString = ''
					for k in str(j):
						if k != '%':
							newString += k
					total_stats[i].append((float(newString)))
print(total_stats)

with open('MLBdataForTraining.txt', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
with open("MLBdataForTraining.txt", "a") as o:
	o.write("," + str(total_stats) + ']')
