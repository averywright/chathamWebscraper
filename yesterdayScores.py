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

link = 'https://www.basketball-reference.com/boxscores/'

page = requests.get(link)
soup = BeautifulSoup(page.content, 'html.parser')
text_table = soup.find_all('table', class_ = 'teams')
headers = []
counter = 0
for i in text_table:
     for j in i.find_all('td', class_ = 'right'):
        title = i.text
        headers.append(title)

print(headers)
import re

pattern = r'\d+'

# Use a list comprehension to extract the numbers from each element of the input list
numbers_only = [int(''.join(num)) for elem in headers for num in re.findall(pattern, elem)]

# Print the resulting list of numbers
print(numbers_only)
counter = 0
for i in numbers_only:
    counter +=1
    if i < 10:
        numbers_only.pop(counter - 1)
print(numbers_only)
storageDict ={}
g = 0
for i in headers:
    g += 1
    add = True
    print(i)
    team1 = []
    team2 = []
    used = False
    if (i.find('Atlanta')) > -1:
        team1.append('ATL')
        used = True
    if (i.find('New Orleans')) > -1:
        if not used:
            team1.append('NOP')
        else:
            team2.append('NOP')
        used = True
    if (i.find('Minnesota')) > -1:
        if not used:
            team1.append('MIN')
        else:
            team2.append('MIN')
        used = True
    if (i.find('LA Lakers')) > -1:
        if not used:
            team1.append('LAL')
        else:
            team2.append('LAL')
        used = True
    if (i.find('Golden State')) > -1:
        if not used:
            team1.append('GSW')
        else:
            team2.append('GSW')
        used = True
    if (i.find('Brooklyn')) > -1:
        if not used:
            team1.append('BRK')
        else:
            team2.append('BRK')
        used = True
    if (i.find('Dallas')) > -1:
        if not used:
            team1.append('DAL')
        else:
            team2.append('DAL')
        used = True
    if (i.find('Phoenix')) > -1:
        if not used:
            team1.append('PHO')
        else:
            team2.append('PHO')
        used = True
    if (i.find('Milwaukee')) > -1:
        if not used:
            team1.append('MIL')
        else:
            team2.append('MIL')
        used = True
    if (i.find('New York')) > -1:
        if not used:
            team1.append('NYK')
        else:
            team2.append('NYK')
        used = True
    if (i.find('Toronto')) > -1:
        if not used:
            team1.append('TOR')
        else:
            team2.append('TOR')
        used = True
    if (i.find('Chicago')) > -1:
        if not used:
            team1.append('CHI')
        else:
            team2.append('CHI')
        used = True
    if (i.find('Utah')) > -1:
        if not used:
            team1.append('UTA')
        else:
            team2.append('UTA')
        used = True
    if (i.find('Cleveland')) > -1:
        if not used:
            team1.append('CLE')
        else:
            team2.append('CLE')
        used = True
    if (i.find('Philadelphia')) > -1:
        if not used:
            team1.append('PHI')
        else:
            team2.append('PHI')
        used = True
    if (i.find('LA Clippers')) > -1:
        if not used:
            team1.append('LAC')
        else:
            team2.append('LAC')
        used = True
    if (i.find('Miami')) > -1:
        if not used:
            team1.append('MIA')
        else:
            team2.append('MIA')
        used = True
    if (i.find('Portland')) > -1:
        if not used:
            team1.append('POR')
        else:
            team2.append('POR')
        used = True
    if (i.find('Denver')) > -1:
        if not used:
            team1.append('DEN')
        else:
            team2.append('DEN')
        used = True
    if (i.find('Sacramento')) > -1:
        if not used:
            team1.append('SAC')
        else:
            team2.append('SAC')
        used = True
    if (i.find('Oklahoma City')) > -1:
        if not used:
            team1.append('OKC')
        else:
            team2.append('OKC')
        used = True
    if (i.find('Memphis')) > -1:
        if not used:
            team1.append('MEM')
        else:
            team2.append('MEM')
        used = True
    if (i.find('San Antonio')) > -1:
        if not used:
            team1.append('SAS')
        else:
            team2.append('SAS')
        used = True
    if (i.find('Houston')) > -1:
        if not used:
            team1.append('HOU')
        else:
            team2.append('HOU')
        used = True
    if (i.find('Charlotte')) > -1:
        if not used:
            team1.append('CHO')
        else:
            team2.append('CHO')
        used = True
    if (i.find('Detroit')) > -1:
        if not used:
            team1.append('DET')
        else:
            team2.append('DET')
        used = True
    if (i.find('Washington')) > -1:
        if not used:
            team1.append('WAS')
        else:
            team2.append('WAS')
        used = True
    if (i.find('Orlando')) > -1:
        if not used:
            team1.append('ORL')
        else:
            team2.append('ORL')
        used = True
    if (i.find('Indiana')) > -1:
        if not used:
            team1.append('IND')
        else:
            team2.append('IND')
        used = True
    if (i.find('Boston')) > -1:
        if not used:
            team1.append('BOS')
        else:
            team2.append('BOS')
        used = True
    # Print the resulting list of numbers
    print(team1,team2)
    for j in storageDict:
        if team1[0] == j or team2[0] == j:
            add = False
    if add:
        storageDict.update({team1[0]: numbers_only[2*g-1]})
        storageDict.update({team2[0]: numbers_only[2*g]})

with open('scoresofYesterday', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
with open("scoresofYesterday", "a") as o:
    o.write(',')
    o.write(str(storageDict))
    o.write(']')
