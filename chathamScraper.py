import re
from datetime import datetime, timedelta
import requests
import json
import time
from bs4 import BeautifulSoup

import re


# Function to extract the second number from a string in the format "3-7"
def extract(input_string):
    # Define a regular expression pattern to match the format "3-7"
    pattern = r'\d+-\d+'

    # Use re.search to find the first match of the pattern in the input string
    match = re.search(pattern, input_string)

    # If a match is found, split the matched text by '-' and return the second part as an integer
    if match:
        numbers = match.group().split('-')
        if len(numbers) == 2:
            return int(numbers[1])

    # Return None if no match is found or the format is invalid
    return None


url = 'https://gochathamcougars.com/sports/baseball/schedule/2023'
time.sleep(5)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
hrefs = []
"""for i in soup.find_all('a', href = True):
    if i['href'].find('boxscore') > -1:
        hrefs.append(i['href'])"""
for i in (soup.find_all(class_="sidearm-schedule-game-result text-italic")):
    counter = 0
    for j in i.find_all('span'):
        counter += 1
        if counter == 3:
            print(extract(j.text))
            break
"""for i in hrefs:
    values = []
    url = 'https://gochathamcougars.com' + i
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    texts = soup.find(id="box-score")
    counter = 0
    for j in texts.find_all('table'):
        counter += 1
        if counter == 4 and j.find('caption').text == 'Chatham':
            for k in j.find('tbody').find_all('tr'):
                for l in k.find_all('td'):
                    values.append(l.text)
            break
        elif counter == 5:
            for k in j.find('tbody').find_all('tr'):
                for l in k.find_all('td'):
                    values.append(l.text)
            break
    cleaned_data = []
    data = values
    for item in data:
        # Remove unnecessary spaces and newline characters
        item = item.strip()

        # Remove parentheses and content within parentheses
        item = re.sub(r'\([^)]*\)', '', item)

        # Remove slashes
        item = item.replace('/', '')

        # Convert numbers to integers if possible
        if item.replace('.', '', 1).isdigit():
            item = (float(item))

        cleaned_data.append(item)
    counter2 = 0
    new_data = []
    for f in cleaned_data:
        appender = True
        counter2 +=1
        if (counter2)%16 == 0:
            appender = False
        if appender:
            new_data.append(f)

    print(new_data)
"""

