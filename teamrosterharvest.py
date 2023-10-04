from bs4 import BeautifulSoup
import requests
import numpy as np
import urllib.request
"""weights = np.random.rand(51, 1)
counter = 0

def relu(x):
	if x > 0:
		return x
	else:
		return 0


def deriv(x):
	if x > 0:
		return 1
	else:
		return 0


def derivativeBias(x, y, z, g, h):
	dc = z - h
	da = deriv(np.dot(x, y) + g)
	db = dc * da
	return db


def derivativeWeights(x, y, z, g, h):
	dc = z - h
	da = deriv(np.dot(x, y) + g)
	dz = x
	dw = dz * dc * da
	return dw


def back(x, y, weights, bias):
	LR = .0000005
	actual = relu(np.dot(x, weights) + bias)
	bias -= derivativeBias(x, weights, actual, bias, y)
	weights -= np.reshape(derivativeWeights(x, weights, actual, bias, y),(51, 1)) * LR

results = [116,107, 114,106,112,100]
inputs = [[0.0, 2.0, 29.4, 6.6, 219.0, 61.0, 241.2, 40.3, 85.8, 0.469, 12.7, 33.5, 0.378, 27.6, 52.3, 0.528, 18.3, 23.5, 0.777, 9.9, 33.6, 43.5, 22.9, 6.8, 4.6, 14.0, 19.5, 111.4, 3.0, 60.0, 241.7, 85.7, 0.467, 11.4, 31.7, 0.359, 28.7, 54.0, 0.531, 19.8, 25.1, 0.791, 10.4, 32.6, 42.9, 23.6, 7.5, 4.0, 15.0, 20.3, 111.3], [1.0, 3.0, 27.9, 6.5, 216.0, 60.0, 241.7, 41.7, 89.6, 0.465, 12.3, 32.6, 0.378, 29.3, 57.1, 0.514, 17.1, 21.5, 0.793, 11.9, 32.0, 43.9, 27.2, 7.4, 5.0, 14.2, 21.0, 112.7, 2.0, 61.0, 241.2, 87.1, 0.47, 12.2, 33.6, 0.364, 28.7, 53.6, 0.536, 17.0, 22.4, 0.759, 9.9, 33.1, 43.0, 24.5, 7.6, 4.2, 13.0, 19.5, 111.1], [0.0, 3.0, 26.4, 6.7, 213.0, 58.0, 240.9, 42.0, 86.6, 0.485, 11.4, 31.8, 0.359, 30.6, 54.8, 0.558, 18.3, 23.2, 0.786, 9.4, 34.7, 44.0, 25.3, 6.9, 5.4, 14.1, 19.1, 113.6, 2.0, 61.0, 241.2, 88.7, 0.47, 12.8, 34.8, 0.368, 28.9, 53.9, 0.537, 19.6, 26.0, 0.752, 11.6, 32.9, 44.4, 25.6, 8.2, 4.0, 15.9, 20.1, 115.8], [1.0, 2.0, 25.4, 6.6, 218.0, 61.0, 241.2, 42.8, 87.0, 0.492, 11.9, 33.5, 0.356, 30.9, 53.5, 0.577, 18.2, 23.5, 0.773, 9.1, 32.3, 41.4, 25.5, 8.1, 5.3, 15.7, 21.8, 115.7, 3.0, 58.0, 240.9, 90.1, 0.464, 11.7, 32.8, 0.357, 30.1, 57.2, 0.526, 18.0, 22.4, 0.802, 10.8, 32.2, 43.0, 23.8, 6.8, 4.7, 12.3, 19.6, 113.3], [0.0, 1.0, 29.6, 6.6, 224.0, 58.0, 242.2, 41.8, 90.1, 0.463, 14.4, 40.0, 0.359, 27.4, 50.1, 0.546, 16.9, 22.9, 0.738, 11.6, 37.6, 49.2, 24.7, 6.6, 5.0, 15.0, 18.4, 114.8, 3.0, 59.0, 242.1, 87.9, 0.469, 13.0, 36.7, 0.354, 28.3, 51.2, 0.552, 17.9, 22.7, 0.786, 9.5, 34.1, 43.6, 25.9, 6.7, 5.0, 14.7, 18.9, 113.4], [1.0, 3.0, 27.5, 6.6, 215.0, 59.0, 242.1, 42.3, 87.0, 0.486, 10.3, 28.8, 0.359, 32.0, 58.3, 0.549, 18.1, 22.3, 0.812, 8.5, 34.3, 42.9, 24.1, 7.5, 4.5, 13.9, 19.5, 113.1, 1.0, 58.0, 242.2, 92.2, 0.453, 11.6, 33.5, 0.346, 30.2, 58.8, 0.514, 16.5, 21.2, 0.779, 10.6, 33.4, 44.1, 22.8, 7.1, 4.1, 12.0, 19.1, 111.6]]
bias = 113
count = 0
for i in range(90000):
	count = 0
	for i in inputs:
		count += 1
		back(inputs[count-1],results[count-1],weights,bias)

results = [125,131,113,123,109,120,124,134,126,101]
inputsForTraining = [[0.0, 1.0, 27.3, 6.6, 222.0, 58.0, 243.4, 41.7, 88.1, 0.473, 15.9, 42.2, 0.376, 25.8, 45.9, 0.563, 18.4, 22.3, 0.826, 9.5, 35.6, 45.1, 26.3, 6.2, 5.3, 13.5, 19.0, 117.7, 1.0, 57.0, 242.2, 41.9, 0.454, 11.6, 33.5, 0.346, 30.3, 58.7, 0.516, 16.5, 21.2, 0.779, 10.5, 33.4, 43.9, 22.9, 7.2, 4.2, 12.1, 19.1, 111.8], [1.0, 1.0, 29.6, 6.6, 224.0, 57.0, 242.2, 41.8, 90.2, 0.464, 14.3, 39.9, 0.359, 27.5, 50.3, 0.547, 16.9, 23.0, 0.737, 11.7, 37.5, 49.2, 24.7, 6.6, 4.9, 15.1, 18.4, 114.9, 1.0, 58.0, 243.4, 90.2, 0.466, 11.6, 32.9, 0.353, 30.4, 57.4, 0.53, 16.2, 20.8, 0.776, 9.5, 34.2, 43.7, 22.8, 6.6, 3.9, 12.6, 19.6, 111.8], [0.0, 4.0, 23.2, 6.7, 224.0, 59.0, 241.3, 40.1, 85.1, 0.472, 10.7, 30.6, 0.35, 29.4, 54.5, 0.54, 19.9, 25.4, 0.787, 9.9, 32.6, 42.6, 22.7, 7.1, 4.6, 15.2, 20.3, 110.9, 5.0, 59.0, 241.7, 40.6, 0.49, 12.4, 33.5, 0.371, 28.2, 49.3, 0.571, 18.8, 23.7, 0.794, 9.3, 33.0, 42.3, 26.0, 6.0, 4.6, 16.6, 20.7, 112.5], [1.0, 5.0, 25.8, 6.7, 217.0, 59.0, 241.7, 41.5, 90.9, 0.456, 10.9, 32.3, 0.336, 30.6, 58.5, 0.523, 19.5, 24.9, 0.782, 12.7, 30.1, 42.8, 23.3, 9.3, 5.3, 11.8, 20.5, 113.3, 4.0, 59.0, 241.3, 87.1, 0.475, 12.9, 37.2, 0.346, 28.5, 49.9, 0.571, 18.1, 23.2, 0.78, 9.8, 32.2, 42.1, 25.7, 7.8, 5.0, 14.5, 20.4, 113.7], [0.0, 1.0, 25.4, 6.6, 212.0, 57.0, 241.3, 43.2, 87.4, 0.494, 13.2, 36.3, 0.365, 29.9, 51.1, 0.585, 19.9, 24.8, 0.802, 9.1, 32.7, 41.8, 26.8, 6.9, 3.3, 14.0, 19.8, 119.5, 2.0, 59.0, 241.7, 40.1, 0.467, 11.4, 31.6, 0.36, 28.7, 54.1, 0.53, 19.7, 25.0, 0.789, 10.4, 32.5, 42.9, 23.5, 7.5, 4.1, 15.0, 20.4, 111.2], [1.0, 2.0, 27.9, 6.5, 216.0, 59.0, 241.7, 41.6, 89.6, 0.465, 12.3, 32.6, 0.379, 29.3, 57.1, 0.514, 17.2, 21.6, 0.793, 12.0, 32.1, 44.0, 27.2, 7.3, 5.0, 14.2, 20.9, 112.8, 1.0, 57.0, 241.3, 88.9, 0.493, 11.8, 32.1, 0.367, 32.0, 56.8, 0.564, 17.8, 22.4, 0.793, 9.7, 32.3, 42.0, 25.8, 7.4, 4.2, 14.4, 20.9, 117.2], [0.0, 4.0, 27.2, 6.5, 209.0, 58.0, 242.2, 43.1, 90.1, 0.479, 16.6, 43.0, 0.386, 26.5, 47.1, 0.563, 15.8, 20.0, 0.788, 9.9, 33.8, 43.7, 29.9, 7.1, 3.7, 16.4, 22.1, 118.6, 3.0, 60.0, 241.3, 40.9, 0.47, 12.2, 33.6, 0.364, 28.7, 53.5, 0.536, 17.1, 22.5, 0.759, 9.9, 33.2, 43.1, 24.4, 7.5, 4.3, 12.9, 19.4, 111.2], [1.0, 3.0, 29.4, 6.6, 219.0, 60.0, 241.3, 40.3, 85.9, 0.469, 12.7, 33.5, 0.378, 27.6, 52.4, 0.527, 18.2, 23.4, 0.775, 9.9, 33.6, 43.5, 22.8, 6.8, 4.7, 14.0, 19.5, 111.4, 4.0, 58.0, 242.2, 90.1, 0.474, 12.8, 35.3, 0.363, 29.9, 54.8, 0.546, 20.2, 26.0, 0.777, 10.6, 33.3, 43.8, 25.6, 7.8, 4.1, 14.7, 18.5, 118.5], [0.0, 3.0, 26.4, 6.7, 213.0, 57.0, 240.9, 42.0, 86.4, 0.485, 11.4, 31.7, 0.358, 30.6, 54.7, 0.559, 18.3, 23.4, 0.785, 9.3, 34.6, 43.9, 25.3, 6.8, 5.4, 14.1, 19.2, 113.6, 4.0, 58.0, 240.9, 42.1, 0.484, 12.0, 32.5, 0.37, 30.1, 54.5, 0.551, 18.9, 24.0, 0.787, 10.2, 31.2, 41.4, 26.0, 7.5, 4.2, 13.3, 21.4, 115.0], [1.0, 4.0, 25.6, 6.6, 215.0, 58.0, 240.9, 40.8, 84.6, 0.482, 13.0, 34.8, 0.374, 27.8, 49.8, 0.557, 20.3, 25.2, 0.803, 9.9, 31.7, 41.6, 24.2, 6.3, 4.3, 14.6, 20.6, 114.9, 3.0, 57.0, 240.9, 90.0, 0.465, 11.8, 32.9, 0.359, 30.1, 57.1, 0.527, 17.9, 22.4, 0.8, 10.7, 32.1, 42.8, 23.9, 6.8, 4.7, 12.2, 19.7, 113.5]]

bias = 113
count = 0
for i in range(90000):
	count = 0
	for i in inputsForTraining:
		count += 1
		back(inputsForTraining[count-1],results[count-1],weights,bias)

print(weights,bias)
print(relu(np.dot(inputs[0], weights) + bias), relu(np.dot(inputs[1], weights) + bias),relu(np.dot(inputs[2], weights) + bias),relu(np.dot(inputs[3], weights) + bias),relu(np.dot(inputs[4], weights) + bias),relu(np.dot(inputs[5], weights) + bias))
for i in inputsForTraining:
	print(relu(np.dot(i, weights) + bias))"""

"""link = "https://www.basketball-reference.com/teams/MIL/2023.html#all_per_minute-playoffs_per_minute"
page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
table_text = str(soup.find(id = "all_team_misc"))

print(table_text[5])
print(table_text)
headers = []"""
"""for i in table.find_all('td'):
	title = i.text
	headers.append(title)"""
team_stats = []
import pandas as pd
def shootingStats(x):
    vals = []
    link = 'https://www.basketball-reference.com/teams/' + x + '/2023.html#advanced'
    dfs = pd.read_html(link)
    stats = dfs[1].dropna()
    d = stats.to_dict('records')
    count = 0
    for i in d:
        mult = 1
        count += 1
        counter = 0
        for value in i.items():
            counter += 1
            if counter != 1 and counter != 2 and counter != 4 and counter != 5:
                (vals.append(value[1] * mult))
            if counter == 6:
                mult = value[1] / 100
        if count > 9:
            break
    return vals


teamList = ['PHO', 'LAC']
def teamHarvesterEven(x, counter):
    team_stats = []
    try:
        link = "https://www.basketball-reference.com/teams/" + x + "/stats_per_game_totals.html"
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='stats')
        headers = []
        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)

        team_stats = [1]
        team_stats.append(headers[4])
        for i in range(6, 33):
            if i == 7:
                g = list(headers[i])
                g[1] = '.'
                team_stats.append("".join(g))
            elif i != 9 and i != 10:
                team_stats.append(headers[i])
        link = "https://www.basketball-reference.com/teams/" + teamList[counter - 2] + "/opp_stats_per_game_totals.html"
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='stats')
        headers = []
        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)
        team_stats.append(headers[4])
        for i in range(6, 29):
            if i != 6:
                team_stats.append(headers[i])

    except:
        print('e')

    return(team_stats)

"""inputs = teamHarvesterEven('LAC', 2)"""
"""for i in shootingStats('PHO'):
    inputs.append(float(i))
print(inputs)"""



