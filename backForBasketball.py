from bs4 import BeautifulSoup
import requests
import numpy as np
import random
import math
import time
import pandas as pd
from io import StringIO

"""import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.headless = True # it's more scalable to work in headless mode
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)
"""
proxy = ['41.33.47.146:1981', '90.84.17.133:3128', '194.77.96.179:3128', '3.99.236.216:80', '8.219.97.248:80',
		 '213.230.127.93:3128', '190.64.148.26:8087', '77.232.21.4:8080']


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
	LR = .00000009
	actual = relu(np.dot(x, weights) + bias)
	bias -= derivativeBias(x, weights, actual, bias, y)
	weights -= np.reshape(derivativeWeights(x, weights, actual, bias, y), (49, 1)) * LR


def teamHarvesterEven(x, counter):
	team_stats = []
	ind = random.randint(0, 7)
	temp = proxy[ind]
	try:
		link = "https://www.basketball-reference.com/teams/" + x + "/stats_per_game_totals.html"
		page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
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
		page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
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
	except:
		print('e')
	"""link = "https://www.basketball-reference.com/teams/" + teamList[counter-2] + "/opp_stats_per_game_totals.html"
	page = requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')
	text_table = soup.find('table', id='stats')
	headers = []
	for i in text_table.find_all('td'):
		title = i.text
		headers.append(title)
	team_stats.append(headers[4])
	for i in range(6, 29):
		if i != 8:
			team_stats.append(headers[i])"""

	return team_stats


def teamHarvesterOdd(x, counter):
	team_stats = []
	ind = random.randint(0, 7)
	temp = proxy[ind]
	try:
		link = "https://www.basketball-reference.com/teams/" + x + "/stats_per_game_totals.html"
		page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
		soup = BeautifulSoup(page.content, 'html.parser')
		text_table = soup.find('table', id='stats')
		headers = []
		for i in text_table.find_all('td'):
			title = i.text
			headers.append(title)
		team_stats = [0]
		team_stats.append(headers[4])
		for i in range(6, 33):
			if i == 7:
				g = list(headers[i])
				g[1] = '.'
				team_stats.append("".join(g))
			elif i != 9 and i != 10:
				team_stats.append(headers[i])
		link = "https://www.basketball-reference.com/teams/" + teamList[counter] + "/opp_stats_per_game_totals.html"
		page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
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
	except:
		print('e')

	return team_stats


def shootingStats(x):
	vals = []
	ind = random.randint(0, 7)
	temp = proxy[ind]
	link = 'https://www.basketball-reference.com/teams/' + x + '/2023.html#advanced'
	page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5).text
	dfs = pd.read_csv(StringIO(page), error_bad_lines=False)

	"""link = 'https://www.basketball-reference.com/teams/' + x + '/2023.html#advanced'
	print(link)
	dfs = pd.read_html(link)"""
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

inputs = [[0, '4', '24.6', '6.6', '218', '243.8', '41.3', '89.7', '.461', '12.1', '35.1', '.345', '29.2', '54.6', '.535', '19.8', '25.7', '.771', '12.9', '34.1', '47.0', '22.4', '6.1', '4.0', '12.7', '20.9', '114.6', '3', '58', '240.9', '.464', '11.7', '32.8', '.357', '30.1', '57.2', '.526', '18.0', '22.4', '.802', '10.8', '32.2', '43.0', '23.8', '6.8', '4.7', '12.3', '19.6', '113.3'], [1, '3', '26.4', '6.7', '213', '240.9', '42.0', '86.6', '.485', '11.4', '31.8', '.359', '30.6', '54.8', '.558', '18.3', '23.2', '.786', '9.4', '34.7', '44.0', '25.3', '6.9', '5.4', '14.1', '19.1', '113.6', '4', '60', '243.8', '.455', '12.9', '37.0', '.347', '27.5', '51.7', '.533', '18.8', '24.3', '.771', '11.0', '32.5', '43.5', '24.7', '5.9', '4.6', '12.6', '21.0', '112.3'], [0, '1', '27.6', '6.5', '216', '241.7', '39.1', '86.4', '.452', '11.6', '34.8', '.334', '27.4', '51.6', '.532', '18.6', '22.4', '.828', '10.1', '31.3', '41.4', '23.4', '8.5', '3.0', '13.3', '18.8', '108.3', '1', '58', '242.2', '.453', '11.6', '33.5', '.346', '30.2', '58.8', '.514', '16.5', '21.2', '.779', '10.6', '33.4', '44.1', '22.8', '7.1', '4.1', '12.0', '19.1', '111.6'], [1, '1', '29.6', '6.6', '224', '242.2', '41.8', '90.1', '.463', '14.4', '40.0', '.359', '27.4', '50.1', '.546', '16.9', '22.9', '.738', '11.6', '37.6', '49.2', '24.7', '6.6', '5.0', '15.0', '18.4', '114.8', '1', '59', '241.7', '.477', '13.1', '35.7', '.367', '26.4', '47.0', '.561', '16.3', '21.1', '.771', '8.6', '33.6', '42.2', '25.2', '6.8', '3.9', '16.3', '19.9', '108.3'], [0, '2', '25.4', '6.6', '220', '242.8', '41.2', '84.4', '.488', '11.4', '31.4', '.362', '29.9', '53.0', '.564', '17.9', '23.0', '.779', '9.7', '32.2', '41.9', '24.9', '7.1', '4.4', '13.8', '18.7', '111.7', '2', '59', '242.1', '.478', '11.8', '33.7', '.349', '31.2', '56.3', '.555', '19.0', '23.6', '.803', '11.0', '34.6', '45.6', '25.6', '7.4', '5.0', '14.5', '19.8', '116.7'], [1, '2', '24.9', '6.6', '209', '242.1', '44.1', '92.3', '.478', '10.5', '30.4', '.347', '33.5', '61.9', '.542', '17.7', '21.7', '.816', '10.6', '33.2', '43.9', '24.7', '7.0', '4.9', '12.7', '19.0', '116.4', '2', '62', '242.8', '.465', '11.4', '30.9', '.368', '27.5', '52.6', '.523', '17.2', '22.1', '.777', '9.4', '30.9', '40.3', '22.9', '7.3', '4.2', '15.1', '20.9', '106.3'], [0, '4', '23.0', '6.6', '202', '243.0', '43.6', '92.8', '.470', '12.1', '33.5', '.361', '31.5', '59.3', '.531', '18.6', '23.2', '.802', '11.5', '32.4', '43.9', '24.7', '8.3', '4.8', '13.5', '21.4', '117.9', '3', '60', '241.7', '.467', '11.4', '31.7', '.359', '28.7', '54.0', '.531', '19.8', '25.1', '.791', '10.4', '32.6', '42.9', '23.6', '7.5', '4.0', '15.0', '20.3', '111.3'], [1, '3', '27.9', '6.5', '216', '241.7', '41.7', '89.6', '.465', '12.3', '32.6', '.378', '29.3', '57.1', '.514', '17.1', '21.5', '.793', '11.9', '32.0', '43.9', '27.2', '7.4', '5.0', '14.2', '21.0', '112.7', '4', '58', '243.0', '.469', '12.7', '35.6', '.356', '29.0', '53.3', '.544', '20.2', '25.8', '.782', '12.1', '34.6', '46.7', '25.4', '7.4', '5.6', '16.9', '20.2', '116.3'], [0, '5', '22.5', '6.6', '214', '240.9', '39.7', '88.2', '.451', '10.8', '33.3', '.326', '28.9', '54.9', '.526', '19.5', '25.8', '.755', '13.1', '33.4', '46.6', '22.4', '7.1', '5.0', '17.0', '20.6', '109.8', '4', '59', '242.1', '.475', '12.9', '35.3', '.366', '29.8', '54.8', '.545', '20.2', '26.1', '.775', '10.6', '33.5', '44.1', '25.7', '7.8', '4.1', '14.8', '18.5', '118.6'], [1, '4', '27.1', '6.5', '209', '242.1', '43.1', '90.4', '.477', '16.6', '43.1', '.384', '26.5', '47.2', '.561', '15.8', '20.0', '.788', '10.0', '33.7', '43.7', '29.8', '7.1', '3.7', '16.3', '22.1', '118.5', '5', '58', '240.9', '.477', '14.4', '39.0', '.368', '27.8', '49.5', '.562', '19.4', '24.3', '.797', '10.7', '31.0', '41.7', '25.7', '9.1', '6.0', '13.3', '21.3', '118.2']]
results = [115,109, 99, 128, 119, 136, 115,124,101,116]
bias = 110
weights = np.random.rand(49, 1)
for i in inputs:
	print(i)
	counter = 0
	for j in i:
		counter += 1
		i[counter-1] = float(j)

for i in range(99000):
	count = 0
	for i in inputs:
		count += 1
		back(inputs[count-1],results[count-1],weights,bias)

inputs = [[0, '1', '26.5', '6.6', '224', '240.8', '44.1', '86.1', '.512', '12.1', '30.8', '.392', '32.0', '55.4', '.578', '16.9', '22.5', '.750', '9.8', '33.0', '42.7', '29.1', '7.6', '4.5', '14.9', '19.1', '117.1', '2', '61', '242.9', '.465', '11.3', '30.8', '.366', '27.6', '52.7', '.524', '17.1', '22.1', '.775', '9.3', '30.9', '40.2', '22.8', '7.3', '4.2', '15.1', '21.0', '106.1'], [1, '2', '25.4', '6.6', '220', '242.9', '41.2', '84.3', '.489', '11.4', '31.5', '.363', '29.8', '52.9', '.563', '17.9', '23.0', '.778', '9.7', '32.2', '41.9', '24.9', '7.0', '4.4', '13.9', '18.6', '111.8', '1', '59', '240.8', '.480', '11.6', '33.2', '.349', '29.9', '53.4', '.561', '18.1', '23.7', '.762', '9.7', '30.3', '40.0', '25.7', '7.7', '4.5', '13.8', '19.8', '112.7'], [0, '1', '27.3', '6.6', '222', '243.4', '41.8', '88.2', '.474', '15.9', '42.2', '.378', '25.9', '45.9', '.563', '18.3', '22.1', '.826', '9.5', '35.6', '45.1', '26.4', '6.3', '5.3', '13.5', '19.0', '117.9', '4', '60', '240.4', '.477', '12.6', '33.6', '.374', '29.5', '54.6', '.540', '20.5', '25.4', '.808', '12.1', '33.6', '45.6', '26.3', '7.9', '5.1', '15.7', '20.1', '117.1'], [1, '4', '24.4', '6.6', '210', '240.4', '41.0', '89.4', '.459', '13.8', '38.2', '.362', '27.2', '51.2', '.532', '18.6', '23.4', '.796', '10.1', '31.5', '41.6', '26.4', '8.0', '5.8', '15.2', '21.3', '114.5', '1', '59', '243.4', '.466', '11.6', '32.8', '.353', '30.5', '57.3', '.531', '16.1', '20.7', '.776', '9.4', '34.1', '43.6', '22.9', '6.6', '3.9', '12.6', '19.5', '111.7'], [0, '5', '24.3', '6.6', '219', '242.1', '39.8', '87.5', '.455', '11.7', '33.2', '.354', '28.0', '54.2', '.517', '21.0', '27.1', '.773', '10.9', '31.3', '42.2', '22.8', '7.2', '3.7', '14.9', '22.4', '112.3', '4', '59', '241.3', '.475', '12.9', '37.2', '.346', '28.5', '49.9', '.571', '18.1', '23.2', '.780', '9.8', '32.2', '42.1', '25.7', '7.8', '5.0', '14.5', '20.4', '113.7'], [1, '4', '23.2', '6.7', '224', '241.3', '40.1', '85.1', '.472', '10.7', '30.6', '.350', '29.4', '54.5', '.540', '19.9', '25.4', '.787', '9.9', '32.6', '42.6', '22.7', '7.1', '4.6', '15.2', '20.3', '110.9', '5', '59', '242.1', '.493', '12.2', '33.7', '.361', '31.5', '55.0', '.574', '20.3', '25.7', '.788', '11.0', '34.0', '44.9', '25.6', '7.3', '5.5', '14.0', '21.7', '119.9'], [0, '1', '24.5', '6.6', '220', '240.9', '43.4', '92.3', '.470', '11.3', '32.8', '.345', '32.1', '59.5', '.539', '18.1', '25.2', '.718', '12.9', '34.9', '47.7', '25.3', '8.4', '6.1', '14.3', '20.1', '116.1', '2', '57', '242.2', '.472', '11.2', '32.6', '.344', '29.1', '52.8', '.550', '18.7', '23.8', '.785', '9.8', '32.2', '42.0', '23.8', '6.7', '4.8', '15.0', '19.8', '110.5'], [1, '2', '28.4', '6.6', '225', '242.2', '40.6', '84.1', '.483', '12.6', '32.9', '.384', '28.0', '51.2', '.546', '20.5', '24.7', '.830', '8.6', '31.9', '40.5', '25.1', '8.0', '4.7', '13.8', '20.4', '114.4', '1', '57', '240.9', '.449', '13.0', '36.5', '.357', '27.5', '53.6', '.513', '18.2', '23.3', '.782', '11.1', '32.9', '44.1', '26.5', '7.2', '5.3', '15.4', '21.0', '112.2'], [0, '3', '25.8', '6.6', '217', '242.5', '42.3', '88.1', '.480', '10.8', '30.3', '.355', '31.5', '57.8', '.545', '19.6', '25.1', '.780', '11.1', '33.1', '44.1', '25.7', '8.5', '4.2', '15.0', '20.8', '114.9', '5', '59', '241.7', '.490', '12.4', '33.5', '.371', '28.2', '49.3', '.571', '18.8', '23.7', '.794', '9.3', '33.0', '42.3', '26.0', '6.0', '4.6', '16.6', '20.7', '112.5'], [1, '5', '25.8', '6.7', '217', '241.7', '41.5', '90.9', '.456', '10.9', '32.3', '.336', '30.6', '58.5', '.523', '19.5', '24.9', '.782', '12.7', '30.1', '42.8', '23.3', '9.3', '5.3', '11.8', '20.5', '113.3', '3', '59', '242.5', '.474', '12.2', '36.0', '.340', '29.2', '51.4', '.569', '18.3', '23.6', '.777', '9.8', '32.3', '42.1', '25.3', '7.3', '5.1', '15.1', '20.8', '113.5'], [0, '4', '24.2', '6.6', '218', '241.7', '43.0', '91.8', '.469', '10.5', '30.9', '.341', '32.5', '60.9', '.533', '15.8', '21.2', '.747', '12.0', '31.1', '43.0', '26.9', '7.0', '3.9', '15.6', '20.2', '112.4', '2', '60', '243.3', '.484', '11.0', '31.3', '.351', '30.0', '53.4', '.562', '19.5', '24.9', '.784', '9.7', '34.1', '43.8', '24.3', '6.3', '4.0', '13.5', '22.6', '112.5'], [1, '2', '27.9', '6.6', '216', '243.3', '39.4', '83.3', '.473', '14.8', '40.6', '.364', '24.6', '42.8', '.575', '19.5', '26.0', '.749', '8.0', '30.7', '38.7', '22.4', '6.5', '3.7', '12.4', '20.7', '113.0', '4', '59', '241.7', '.509', '12.4', '31.5', '.394', '33.6', '58.9', '.570', '18.2', '23.6', '.772', '10.7', '33.4', '44.2', '26.5', '8.3', '4.9', '14.0', '18.6', '122.6'], [0, '3', '23.0', '6.6', '202', '242.6', '43.6', '92.5', '.471', '12.2', '33.5', '.364', '31.4', '59.0', '.532', '18.6', '23.1', '.803', '11.4', '32.4', '43.7', '24.7', '8.3', '4.9', '13.5', '21.4', '117.9', '5', '60', '241.3', '.479', '11.7', '32.3', '.362', '31.7', '58.3', '.544', '18.7', '24.2', '.774', '11.6', '31.9', '43.5', '24.1', '7.8', '4.8', '13.2', '21.2', '117.2'], [1, '5', '26.8', '6.6', '215', '241.3', '42.3', '89.2', '.475', '14.1', '38.9', '.362', '28.3', '50.3', '.562', '18.8', '23.9', '.788', '11.8', '32.9', '44.7', '25.7', '6.4', '4.9', '15.2', '20.6', '117.6', '3', '57', '242.6', '.470', '12.7', '35.4', '.358', '29.0', '53.4', '.544', '20.2', '25.8', '.781', '12.1', '34.5', '46.5', '25.4', '7.4', '5.5', '16.9', '20.1', '116.2']]
results = [115,109,142,138,106,108,105,110,110,115,116,142,119,120]
for i in inputs:
	print(i)
	counter = 0
	for j in i:
		counter += 1
		i[counter-1] = float(j)

for i in range(99000):
	count = 0
	for i in inputs:
		count += 1
		back(inputs[count-1],results[count-1],weights,bias)

print(weights,bias)

print(weights,bias)
