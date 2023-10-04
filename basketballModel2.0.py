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
import os, sys

today = date.today()

activePlayers = [
    'Precious Achiuwa',
    'Steven Adams',
    'Bam Adebayo',
    'Ochai Agbaji',
    'Santi Aldama',
    'Nickeil Alexander-Walker',
    'Grayson Allen',
    'Jarrett Allen',
    'Jose Alvarado',
    'Kyle Anderson',
    'Giannis Antetokounmpo',
    'Thanasis Antetokounmpo',
    'Cole Anthony',
    'OG Anunoby',
    'Ryan Arcidiacono',
    'Deni Avdija',
    'Deandre Ayton',
    'Udoka Azubuike',
    'Marvin Bagley III',
    'Patrick Baldwin Jr.',
    'LaMelo Ball',
    'Mo Bamba',
    'Paolo Banchero',
    'Desmond Bane',
    'Dalano Banton',
    'Dominick Barlow',
    'Harrison Barnes',
    'Scottie Barnes',
    'RJ Barrett',
    'Will Barton',
    'Charles Bassey',
    'Keita Bates-Diop',
    'Nicolas Batum',
    'Darius Bazley',
    'Bradley Beal',
    'Malik Beasley',
    'Malik Beasley',
    'Malik Beasley',
    'MarJon Beauchamp',
    'Davis Bertans',
    'Patrick Beverley',
    'Saddiq Bey',
    'Khem Birch',
    'Goga Bitadze',
    'Bismack Biyombo',
    'Buddy Boeheim',
    'Bogdan Bogdanovi',
    'Bojan Bogdanovi',
    'Bol Bol',
    'Leandro Bolmaro',
    'Devin Booker',
    'Brandon Boston Jr.',
    'Chris Boucher',
    'James Bouknight',
    'Jamaree Bouyea',
    'Tony Bradley',
    'Malaki Branham',
    'Christian Braun',
    'Mikal Bridges',
    'Mikal Bridges',
    'Mikal Bridges',
    'Oshae Brissett',
    'Malcolm Brogdon',
    'Dillon Brooks',
    'Bruce Brown',
    'Greg Brown III',
    'Jaylen Brown',
    'Kendall Brown',
    'Moses Brown',
    'Sterling Brown',
    'Troy Brown Jr.',
    'Jalen Brunson',
    'Thomas Bryant',
    'Thomas Bryant',
    'Thomas Bryant',
    'Reggie Bullock',
    'Alec Burks',
    'Deonte Burton',
    'Jimmy Butler',
    'John Butler',
    'Jamal Cain',
    'Kentavious Caldwell-Pope',
    'Facundo Campazzo',
    'Vlatko',
    'Clint Capela',
    'Vernon Carey Jr.',
    'Jevon Carter',
    'Wendell Carter Jr.',
    'Alex Caruso',
    'Julian Champagnie',
    'Justin Champagnie',
    'Kennedy Chandler',
    'Max Christie',
    'Josh Christopher',
    'Brandon Clarke',
    'Jordan Clarkson',
    'Nic Claxton',
    'Amir Coffey',
    'John Collins',
    'Zach Collins',
    'Mike Conley',
    'Mike Conley',
    'Mike Conley',
    'Pat Connaughton',
    'Robert Covington',
    'Torrey Craig',
    'Jarrett Culver',
    'Cade Cunningham',
    'Seth Curry',
    'Stephen Curry',
    'Dyson Daniels',
    'Anthony Davis',
    'Johnny Davis',
    'Terence Davis',
    'JD Davison',
    'Darius Days',
    'Dewayne Dedmon',
    'Matthew Dellavedova',
    'DeMar DeRozan',
    'Moussa Diabaté',
    'Mamadi Diakite',
    'Hamidou Diallo',
    'Gorgui Dieng',
    'Ousmane Dieng',
    'Spencer Dinwiddie',
    'Spencer Dinwiddie',
    'Spencer Dinwiddie',
    'Donte DiVincenzo',
    'Luka Don',
    'Tyler Dorsey',
    'Luguentz Dort',
    'Ayo Dosunmu',
    'Devon Dotson',
    'Jeff Dowtin',
    'PJ Dozier',
    'Goran Dragi',
    'Andre Drummond',
    'Chris Duarte',
    'David Duke Jr.',
    'Kevin Durant',
    'Jalen Duren',
    'Tari Eason',
    'Anthony Edwards',
    'Kessler Edwards',
    'Keon Ellis',
    'Joel Embiid',
    'Drew Eubanks',
    'Bruno Fernando',
    'Dorian Finney-Smith',
    'Dorian Finney-Smith',
    'Dorian Finney-Smith',
    'Malachi Flynn',
    'Simone Fontecchio',
    'Bryn Forbes',
    'Trent Forrest',
    'Michael Foster Jr.',
    'Evan Fournier',
    'De\'Aaron Fox',
    'Markelle Fultz',
    'Wenyen Gabriel',
    'Daniel Gafford',
    'Darius Garland',
    'Usman Garuba',
    'Luka Garza',
    'Rudy Gay',
    'Paul George',
    'Taj Gibson',
    'Josh Giddey',
    'Shai Gilgeous-Alexander',
    'Anthony Gill',
    'Rudy Gobert',
    'Jordan Goodwin',
    'Aaron Gordon',
    'Eric Gordon',
    'Devonte\' Graham',
    'Jerami Grant',
    'A.J. Green',
    'Danny Green',
    'Draymond Green',
    'Jalen Green',
    'JaMychal Green',
    'Javonte Green',
    'Jeff Green',
    'Josh Green',
    'AJ Griffin',
    'Blake Griffin',
    'Quentin Grimes',
    'Rui Hachimura',
    'Rui Hachimura',
    'Rui Hachimura',
    'Tyrese Haliburton',
    'Jordan Hall',
    'R.J. Hampton',
    'Tim Hardaway Jr.',
    'James Harden',
    'Jaden Hardy',
    'Ron Harper Jr.',
    'Montrezl Harrell',
    'Gary Harris',
    'Joe Harris',
    'Kevon Harris',
    'Tobias Harris',
    'Josh Hart',
    'Josh Hart',
    'Josh Hart',
    'Isaiah Hartenstein',
    'Udonis Haslem',
    'Sam Hauser',
    'Jaxson Hayes',
    'Killian Hayes',
    'Gordon Hayward',
    'Juancho Hernangómez',
    'Willy Hernangómez',
    'Tyler Herro',
    'Buddy Hield',
    'Haywood Highsmith',
    'George Hill',
    'Malcolm Hill',
    'Aaron Holiday',
    'Jrue Holiday',
    'Justin Holiday',
    'Richaun Holmes',
    'Al Horford',
    'Talen Horton-Tucker',
    'Danuel House Jr.',
    'Caleb Houstan',
    'Trevor Hudgins',
    'Kevin Huerter',
    'De\'Andre Hunter',
    'Bones Hyland',
    'Serge Ibaka',
    'Andre Iguodala',
    'Joe Ingles',
    'Brandon Ingram',
    'Kyrie Irving',
    'Kyrie Irving',
    'Kyrie Irving',
    'Jonathan Isaac',
    'Jaden Ivey',
    'Isaiah Jackson',
    'Jaren Jackson Jr.',
    'Justin Jackson',
    'Quenton Jackson',
    'Reggie Jackson',
    'LeBron James',
    'Ty Jerome',
    'Isaiah Joe',
    'Alize Johnson',
    'Cameron Johnson',
    'Cameron Johnson',
    'Cameron Johnson',
    'Jalen Johnson',
    'James Johnson',
    'Keldon Johnson',
    'Keon Johnson',
    'Stanley Johnson',
    'Nikola Joki',
    'Carlik Jones',
    'Damian Jones',
    'Derrick Jones Jr.',
    'Herbert Jones',
    'Kai Jones',
    'Tre Jones',
    'Tyus Jones',
    'DeAndre Jordan',
    'Cory Joseph',
    'Nikola Jovi',
    'Mfiondu Kabengele',
    'Frank Kaminsky',
    'Frank Kaminsky',
    'Frank Kaminsky',
    'Trevor Keels',
    'Luke Kennard',
    'Walker Kessler',
    'Braxton Key',
    'Corey Kispert',
    'Maxi Kleber',
    'Nathan Knight',
    'Kevin Knox',
    'Christian Koloko',
    'John Konchar',
    'Furkan Korkmaz',
    'Luke Kornet',
    'Vit Krejci',
    'Jonathan Kuminga',
    'Kyle Kuzma',
    'Anthony Lamb',
    'Jock Landale',
    'Romeo Langford',
    'Jake LaRavia',
    'Zach LaVine',
    'A.J. Lawson',
    'A.J. Lawson',
    'A.J. Lawson',
    'Damion Lee',
    'Saben Lee',
    'Saben Lee',
    'Saben Lee',
    'Alex Len',
    'Kawhi Leonard',
    'Caris LeVert',
    'Kira Lewis Jr.',
    'Damian Lillard',
    'Nassir Little',
    'Isaiah Livers',
    'Kenneth Lofton Jr.',
    'Kevon Looney',
    'Brook Lopez',
    'Robin Lopez',
    'Kevin Love',
    'Kyle Lowry',
    'Trey Lyles',
    'Théo Maledon',
    'Sandro Mamukelashvili',
    'Terance Mann',
    'Tre Mann',
    'Boban Marjanovi',
    'Lauri Markkanen',
    'Cody Zeller',
    'Naji Marshall',
    'Caleb Martin',
    'Cody Martin',
    'Kenyon Martin Jr.',
    'Tyrese Martin',
    'Garrison Mathews',
    'Bennedict Mathurin',
    'Wesley Matthews',
    'Tyrese Maxey',
    'Miles McBride',
    'CJ McCollum',
    'T.J. McConnell',
    'Jaden McDaniels',
    'Jalen McDaniels',
    'Jalen McDaniels',
    'Jalen McDaniels',
    'Doug McDermott',
    'JaVale McGee',
    'Bryce McGowens',
    'Rodney McGruder',
    'Jordan McLaughlin',
    'De\'Anthony Melton',
    'Chimezie Metu',
    'Khris Middleton',
    'Patty Mills',
    'Shake Milton',
    'Josh Minott',
    'Davion Mitchell',
    'Donovan Mitchell',
    'Evan Mobley',
    'Isaiah Mobley',
    'Chima Moneke',
    'Malik Monk',
    'Moses Moody',
    'Wendell Moore Jr.',
    'Ja Morant',
    'Marcus Morris',
    'Markieff Morris',
    'Monte Morris',
    'Trey Murphy III',
    'Dejounte Murray',
    'Jamal Murray',
    'Keegan Murray',
    'Shaedon Sharpe',
    'Mike Muscala',
    'Mike Muscala',
    'Mike Muscala',
    'Svi Mykhailiuk',
    'Larry Nance Jr.',
    'Andrew Nembhard',
    'Aaron Nesmith',
    'Raul Neto',
    'Georges Niang',
    'Daishen Nix',
    'Zeke Nnaji',
    'Nerlens Noel',
    'Jaylen Nowell',
    'Frank Ntilikina',
    'Kendrick Nunn',
    'Kendrick Nunn',
    'Kendrick Nunn',
    'Jusuf Nurki',
    'Jordan Nwora',
    'Royce O\'Neale',
    'Chuma Okeke',
    'Josh Okogie',
    'Onyeka Okongwu',
    'Isaac Okoro',
    'KZ Okpala',
    'Victor Oladipo',
    'Kelly Olynyk',
    'Eugene Omoruyi',
    'Cedi Osman',
    'Kelly Oubre Jr.',
    'Chris Paul',
    'Cameron Payne',
    'Gary Payton II',
    'Theo Pinson',
    'Scotty Pippen Jr.',
    'Mason Plumlee',
    'Jakob Poeltl',
    'Jakob Poeltl',
    'Jakob Poeltl',
    'Aleksej Pokusevski',
    'Jordan Poole',
    'Kevin Porter Jr.',
    'Michael Porter Jr.',
    'Otto Porter Jr.',
    'Bobby Portis',
    'Kristaps Porzi',
    'Kris Dunn',
    'Micah Potter',
    'Dwight Powell',
    'Norman Powell',
    'Jason Preston',
    'Joshua Primo',
    'Taurean Prince',
    'Payton Pritchard',
    'Trevelin Queen',
    'Neemias Queta',
    'Immanuel Quickley',
    'Julius Randle',
    'Austin Reaves',
    'Cam Reddish',
    'Cam Reddish',
    'Cam Reddish',
    'Davon Reed',
    'Paul Reed',
    'Naz Reid',
    'Jared Rhoden',
    'Nick Richards',
    'Josh Richardson',
    'Austin Rivers',
    'Duncan Robinson',
    'Mitchell Robinson',
    'Orlando Robinson',
    'Jeremiah Robinson-Earl',
    'Isaiah Roby',
    'David Roddy',
    'Ryan Rollins',
    'Derrick Rose',
    'Terrence Ross',
    'Terry Rozier',
    'Ricky Rubio',
    'D\'Angelo Russell',
    'Matt Ryan',
    'Domantas Sabonis',
    'Dario',
    'Jordan Schakel',
    'Admiral Schofield',
    'Dennis Schröder',
    'Dereon Seabron',
    'Alperen',
    'Collin Sexton',
    'Landry Shamet',
    'Day\'Ron Sharpe',
    'S\'haedon Sharpe',
    'Pascal Siakam',
    'Chris Silva',
    'Ben Simmons',
    'Marko Simonovic',
    'Anfernee Simons',
    'Jericho Sims',
    'Marcus Smart',
    'Dennis Smith Jr.',
    'Dru Smith',
    'Dru Smith',
    'Dru Smith',
    'Ish Smith',
    'Jabari Smith Jr.',
    'Jalen Smith',
    'Jeremy Sochan',
    'Jaden Springer',
    'Lamar Stevens',
    'Isaiah Stewart',
    'Max Strus',
    'Jalen Suggs',
    'Edmond Sumner',
    'Cole Swider',
    'Jae Crowder',
    "Jae\'Sean Tate",
    'Jayson Tatum',
    'Terry Taylor',
    'Garrett Temple',
    'Dalen Terry',
    'Daniel Theis',
    'Cam Thomas',
    'Klay Thompson',
    'JT Thor',
    'Matisse Thybulle',
    'Xavier Tillman Sr.',
    'Isaiah Todd',
    'Obi Toppin',
    'Juan Toscano-Anderson',
    'Karl-Anthony Towns',
    'Gary Trent Jr.',
    'P.J. Tucker',
    'Myles Turner',
    'Jonas Valan',
    'Jarred Vanderbilt',
    'Jarred Vanderbilt',
    'Jarred Vanderbilt',
    'Fred VanVleet',
    'Devin Vassell',
    'Gabe Vincent',
    'Noah Vonleh',
    'Nikola Vu',
    'Dean Wade',
    'Franz Wagner',
    'Moritz Wagner',
    'Ish Wainright',
    'Jabari Walker',
    'Kemba Walker',
    'Lonnie Walker IV',
    'John Wall',
    'T.J. Warren',
    'Duane Washington Jr.',
    'P.J. Washington',
    'TyTy Washington Jr.',
    'Yuta Watanabe',
    'Lindy Waters III',
    'Trendon Watford',
    'Peyton Watson',
    'Blake Wesley',
    'Russell Westbrook',
    'Coby White',
    'Derrick White',
    'Jack White',
    'Joe Wieskamp',
    'Aaron Wiggins',
    'Andrew Wiggins',
    'Alondes Williams',
    'Grant Williams',
    'Jalen Williams',
    'Jaylin Williams',
    'Kenrich Williams',
    'Mark Williams',
    'Patrick Williams',
    'Robert Williams',
    'Vince Williams Jr.',
    'Ziaire Williams',
    'Zion Williamson',
    'Justise Winslow',
    'James Wiseman',
    'Christian Wood',
    'Delon Wright',
    'McKinley Wright IV',
    'Thaddeus Young',
    'Trae Young',
    'Ivica Zubac'
]

proxy = [
    '162.144.233.16:80',
    '46.101.49.62:80',
    '138.197.102.119:80',
    '65.21.131.27:80',
    '137.184.100.135:80',
    '78.28.152.111:80',
    '158.69.52.218:9300',
    '116.0.61.122:3128',
    '81.12.44.197:3129',
    '115.144.100.124:10000',
    '1.214.62.71:8000',
    '94.100.26.202:80',
    '65.0.160.35:8080',
    '91.209.11.132:80',
    '5.189.184.6:80',
    '45.92.108.112:8080',
    '82.98.147.36:80',
    '117.54.114.99:80',
    '212.182.90.118:80',
    '93.188.161.84:80',
    '54.206.42.168:80',
    '51.75.122.80:80',
    '8.210.83.33:80',
    '198.49.68.80:80',
    '78.46.175.184:80',
    '143.110.232.177:80',
    '212.107.31.118:80',
    '119.93.129.34:80',
    '157.254.193.139:80',
    '23.238.33.186:80',
    '190.61.88.147:8080',
    '46.209.106.202:3128',
    '190.128.228.182:80',
    '185.218.125.70:80',
    '105.16.115.202:80',
    '146.255.100.226:80',
    '24.13.39.215:80',
    '194.104.158.177:80',
    '138.68.235.51:80',
    '141.95.122.232:80',
    '173.249.198.244:8080',
    '109.122.195.14:80',
    '104.225.220.233:80',
    '45.32.101.24:80',
    '8.209.198.247:80',
    '103.92.26.190:4002',
    '82.180.163.130:80',
    '3.108.174.46:80',
    '65.108.9.181:80',
    '42.98.75.138:80',
    '20.210.113.32:80',
    '20.206.106.192:80',
    '47.241.122.19:80',
    '20.24.43.214:80',
    '185.162.251.76:80',
    '119.237.37.28:80',
    '165.154.224.14:80',
    '103.155.217.52:41367',
    '169.55.89.6:80',
    '196.1.97.209:80',
    '51.75.141.46:80',
    '184.72.36.89:80',
    '45.77.198.163:80',
    '172.104.155.146:80',
    '103.152.9.150:80',
    '117.54.114.35:80',
    '91.238.103.65:80',
    '203.198.207.253:80',
    '116.203.254.38:80',
    '220.136.144.216:80',
    '123.202.159.203:80',
    '141.147.33.121:80',
    '91.229.114.143:80',
    '163.53.18.119:80',
    '46.47.197.210:3128',
    '146.59.127.168:80',
    '108.61.173.226:80',
    '91.229.114.153:80',
    '117.54.114.100:80',
    '200.103.102.18:80',
    '125.141.151.83:80',
    '158.69.53.98:9300',
    '134.209.29.120:3128',
    '47.253.105.175:8047',
    '207.180.250.238:80',
    '209.169.71.193:80',
    '182.72.203.246:80',
    '47.88.87.74:1080',
    '54.243.30.23:80',
    '54.235.240.201:80',
    '197.255.125.12:80',
    '192.236.160.186:80',
    '34.239.204.118:80',
    '34.87.103.220:80',
    '202.173.214.73:80',
    '202.173.214.72:80',
    '157.245.27.9:3128',
    '103.214.201.209:8080',
    '43.251.117.134:45787',
    '181.209.97.189:9998',
    '103.52.37.46:41890',
    '144.48.178.113:83',
    '196.251.221.2:8104',
    '38.49.138.133:999',
    '79.116.27.227:80',
    '14.207.132.236:8080',
    '34.146.64.228:3128',
    '43.251.118.134:45787',
    '103.155.217.105:41407',
    '41.93.71.12:80',
    '113.161.131.43:80',
    '13.95.173.197:80',
    '216.137.184.253:80',
    '41.170.12.92:37444',
    '103.157.117.227:8080',
    '103.251.214.167:6666',
    '213.230.127.93:3128',
    '185.65.203.218:8080',
    '187.217.54.84:80',
    '201.217.49.2:80',
    '68.183.143.134:80',
    '86.18.228.152:80',
    '37.9.171.157:80',
    '118.26.110.48:8080',
    '103.98.135.121:80',
    '159.224.243.185:37793',
    '103.75.196.121:80',
    '117.54.114.98:80',
    '3.128.142.113:80',
    '18.163.96.231:80',
    '3.109.238.5:8080',
    '103.155.217.156:41482',
    '94.21.200.159:80',
    '113.161.114.2:3128',
    '124.13.181.6:80',
    '13.232.245.132:80',
    '103.242.119.88:80',
    '46.101.3.81:443',
    '31.186.239.246:8080',
    '51.159.115.233:3128',
    '220.122.126.86:8001',
    '200.69.210.59:80',
    '141.147.9.254:80',
    '103.38.214.21:3128',
    '91.234.195.124:80',
    '103.152.9.144:80',
    '124.13.181.7:80',
    '190.52.178.17:80',
    '164.92.200.113:80',
    '31.186.239.244:8080',
    '78.30.230.117:50932',
    '91.225.48.111:8888',
    '108.170.12.12:80',
    '143.198.182.218:80',
    '103.156.248.102:8080',
    '103.73.158.76:80',
    '45.149.43.56:53281',
    '104.45.128.122:80',
    '138.0.233.33:41890',
    '52.51.64.165:8118',
    '103.76.151.133:8181',
    '75.89.101.63:80',
    '182.72.203.243:80',
    '216.215.123.174:8080',
    '163.44.253.160:80',
    '185.33.181.41:80',
    '103.123.25.65:80',
    '172.106.16.60:3128',
    '159.69.245.208:57119',
    '41.204.63.118:80',
    '190.64.148.26:8087',
    '154.236.179.226:1981',
    '213.191.194.24:80',
    '157.100.53.133:8080',
    '41.65.236.43:1976',
    '200.105.215.22:33630',
    '117.54.114.103:80',
    '5.9.139.204:60013',
    '89.58.29.103:80',
    '51.75.206.209:80',
    '47.56.110.204:8989',
    '91.126.41.206:80',
    '146.59.199.12:80',
    '65.108.69.40:10046',
    '51.178.18.88:80',
    '202.61.192.193:80',
    '152.67.99.80:80',
    '43.251.117.6:45787',
    '94.228.204.225:41890',
    '107.152.39.44:8080',
    '134.122.58.174:80',
    '3.226.168.144:80',
    '8.219.169.172:3790',
    '45.229.206.15:55555',
    '45.229.34.174:999',
    '52.41.249.10:80',
    '31.207.38.66:80',
    '103.155.62.163:8080',
    '3.143.37.255:80',
    '95.154.104.147:44393',
    '195.154.106.167:80',
    '138.2.70.213:80',
    '103.148.192.83:8089',
    '34.81.72.31:80',
    '201.229.250.21:8080',
    '103.171.182.225:8080',
    '93.180.222.134:8080',
    '189.250.93.75:80',
    '74.208.51.197:5000',
    '45.32.245.26:80',
    '43.255.113.232:8082',
    '146.59.243.214:80',
    '103.178.54.149:80',
    '51.89.73.43:80',
    '20.111.54.16:80',
    '20.205.61.143:80',
    '23.95.94.41:3128',
    '192.248.125.3:80',
    '128.111.5.234:3128',
    '83.171.248.156:3128',
    '152.69.215.206:80',
    '195.201.231.22:8080',
    '139.99.135.214:80',
    '2.58.56.143:8080',
    '202.173.214.77:80',
    '45.84.241.250:3128',
    '20.69.79.158:8443',
    '31.186.239.245:8080',
    '198.11.175.192:8081',
    '13.71.80.224:80',
    '185.73.202.85:80',
    '191.252.193.200:8080',
    '51.222.155.142:80',
    '47.245.34.161:8080',
    '146.83.128.23:80',
    '168.119.119.107:80',
    '115.144.102.39:10080',
    '51.68.181.108:80',
    '149.202.172.113:80',
    '47.74.152.29:8888',
    '82.146.37.145:80',
    '185.233.104.162:80',
    '52.24.80.166:80',
    '125.17.80.226:8080',
    '162.223.94.164:80',
    '43.230.202.171:80',
    '139.162.78.109:3128',
    '102.68.85.187:80',
    '152.32.202.108:80',
    '137.184.232.148:80',
    '174.70.1.210:8080',
    '104.223.135.178:10000',
    '103.169.255.74:8080',
    '49.0.246.130:45554',
    '139.59.1.14:3128',
    '137.184.197.190:80',
    '138.219.244.154:6666',
    '45.189.117.74:999',
    '45.179.245.1:999',
    '157.230.241.133:36835',
    '15.206.33.130:1080',
    '102.177.192.84:3128',
    '193.123.243.148:80',
    '68.178.161.107:80',
    '202.61.204.51:80',
    '51.79.50.22:9300',
    '45.84.241.4:3128',
    '117.54.114.97:80',
    '8.208.90.243:443',
    '172.104.117.89:80',
    '117.54.114.96:80',
    '201.212.246.80:80',
    '163.172.85.30:80',
    '195.190.144.6:80',
    '108.61.174.218:80',
    '161.35.161.38:80',
    '138.2.9.75:8080',
    '137.74.65.101:80',
    '125.17.80.227:8080',
    '125.17.80.229:8080',
    '51.68.124.241:80',
    '14.139.242.7:80',
    '82.66.172.182:80',
    '45.85.45.30:80',
    '191.252.178.3:80',
    '178.32.101.200:80',
    '47.243.177.210:8088',
    '158.69.157.172:80',
    '103.234.55.173:80',
    '161.97.93.15:80',
    '82.102.10.125:18345',
    '117.54.114.101:80',
    '185.103.87.30:8081',
    '164.52.192.156:80',
    '193.31.27.123:80',
    '142.132.243.163:3128',
    '78.138.98.115:3128',
    '13.75.216.118:3128',
    '201.17.26.54:80',
    '45.32.246.111:80',
]
proxy = [
    '162.144.233.16:80',
    '46.101.49.62:80',
    '138.197.102.119:80',
    '65.21.131.27:80',
    '137.184.100.135:80',
    '78.28.152.111:80',
    '158.69.52.218:9300',
    '116.0.61.122:3128',
    '81.12.44.197:3129',
    '115.144.100.124:10000',
    '1.214.62.71:8000',
    '94.100.26.202:80',
    '65.0.160.35:8080',
    '91.209.11.132:80',
    '5.189.184.6:80',
    '45.92.108.112:8080',
    '82.98.147.36:80',
    '117.54.114.99:80',
    '212.182.90.118:80',
    '93.188.161.84:80',
    '54.206.42.168:80',
    '51.75.122.80:80',
    '8.210.83.33:80',
    '198.49.68.80:80',
    '78.46.175.184:80',
    '143.110.232.177:80',
    '212.107.31.118:80',
    '119.93.129.34:80',
    '157.254.193.139:80',
    '23.238.33.186:80',
    '190.61.88.147:8080',
    '46.209.106.202:3128',
    '190.128.228.182:80',
    '185.218.125.70:80',
    '105.16.115.202:80',
    '146.255.100.226:80',
    '24.13.39.215:80',
    '194.104.158.177:80',
    '138.68.235.51:80',
    '141.95.122.232:80',
    '173.249.198.244:8080',
    '109.122.195.14:80',
    '104.225.220.233:80',
    '45.32.101.24:80',
    '8.209.198.247:80',
    '103.92.26.190:4002',
    '82.180.163.130:80',
    '3.108.174.46:80',
    '65.108.9.181:80',
    '42.98.75.138:80',
    '20.210.113.32:80',
    '20.206.106.192:80',
    '47.241.122.19:80',
    '20.24.43.214:80',
    '185.162.251.76:80',
    '119.237.37.28:80',
    '165.154.224.14:80',
    '103.155.217.52:41367',
    '169.55.89.6:80',
    '196.1.97.209:80',
    '51.75.141.46:80',
    '184.72.36.89:80',
    '45.77.198.163:80',
    '172.104.155.146:80',
    '103.152.9.150:80',
    '117.54.114.35:80',
    '91.238.103.65:80',
    '203.198.207.253:80',
    '116.203.254.38:80',
    '220.136.144.216:80',
    '123.202.159.203:80',
    '141.147.33.121:80',
    '91.229.114.143:80',
    '163.53.18.119:80',
    '46.47.197.210:3128',
    '146.59.127.168:80',
    '108.61.173.226:80',
    '91.229.114.153:80',
    '117.54.114.100:80',
    '200.103.102.18:80',
    '125.141.151.83:80',
    '158.69.53.98:9300',
    '134.209.29.120:3128',
    '47.253.105.175:8047',
    '207.180.250.238:80',
    '209.169.71.193:80',
    '182.72.203.246:80',
    '47.88.87.74:1080',
    '54.243.30.23:80',
    '54.235.240.201:80',
    '197.255.125.12:80',
    '192.236.160.186:80',
    '34.239.204.118:80',
    '34.87.103.220:80',
    '202.173.214.73:80',
    '202.173.214.72:80',
    '157.245.27.9:3128',
    '103.214.201.209:8080',
    '43.251.117.134:45787',
    '181.209.97.189:9998',
    '103.52.37.46:41890',
    '144.48.178.113:83',
    '196.251.221.2:8104',
    '38.49.138.133:999',
    '79.116.27.227:80',
    '14.207.132.236:8080',
    '34.146.64.228:3128',
    '43.251.118.134:45787',
    '103.155.217.105:41407',
    '41.93.71.12:80',
    '113.161.131.43:80',
    '13.95.173.197:80',
    '216.137.184.253:80',
    '41.170.12.92:37444',
    '103.157.117.227:8080',
    '103.251.214.167:6666',
    '213.230.127.93:3128',
    '185.65.203.218:8080',
    '187.217.54.84:80',
    '201.217.49.2:80',
    '68.183.143.134:80',
    '86.18.228.152:80',
    '37.9.171.157:80',
    '118.26.110.48:8080',
    '103.98.135.121:80',
    '159.224.243.185:37793',
    '103.75.196.121:80',
    '117.54.114.98:80',
    '3.128.142.113:80',
    '18.163.96.231:80',
    '3.109.238.5:8080',
    '103.155.217.156:41482',
    '94.21.200.159:80',
    '113.161.114.2:3128',
    '124.13.181.6:80',
    '13.232.245.132:80',
    '103.242.119.88:80',
    '46.101.3.81:443',
    '31.186.239.246:8080',
    '51.159.115.233:3128',
    '220.122.126.86:8001',
    '200.69.210.59:80',
    '141.147.9.254:80',
    '103.38.214.21:3128',
    '91.234.195.124:80',
    '103.152.9.144:80',
    '124.13.181.7:80',
    '190.52.178.17:80',
    '164.92.200.113:80',
    '31.186.239.244:8080',
    '78.30.230.117:50932',
    '91.225.48.111:8888',
    '108.170.12.12:80',
    '143.198.182.218:80',
    '103.156.248.102:8080',
    '103.73.158.76:80',
    '45.149.43.56:53281',
    '104.45.128.122:80',
    '138.0.233.33:41890',
    '52.51.64.165:8118',
    '103.76.151.133:8181',
    '75.89.101.63:80',
    '182.72.203.243:80',
    '216.215.123.174:8080',
    '163.44.253.160:80',
    '185.33.181.41:80',
    '103.123.25.65:80',
    '172.106.16.60:3128',
    '159.69.245.208:57119',
    '41.204.63.118:80',
    '190.64.148.26:8087',
    '154.236.179.226:1981',
    '213.191.194.24:80',
    '157.100.53.133:8080',
    '41.65.236.43:1976',
    '200.105.215.22:33630',
    '117.54.114.103:80',
    '5.9.139.204:60013',
    '89.58.29.103:80',
    '51.75.206.209:80',
    '47.56.110.204:8989',
    '91.126.41.206:80',
    '146.59.199.12:80',
    '65.108.69.40:10046',
    '51.178.18.88:80',
    '202.61.192.193:80',
    '152.67.99.80:80',
    '43.251.117.6:45787',
    '94.228.204.225:41890',
    '107.152.39.44:8080',
    '134.122.58.174:80',
    '3.226.168.144:80',
    '8.219.169.172:3790',
    '45.229.206.15:55555',
    '45.229.34.174:999',
    '52.41.249.10:80',
    '31.207.38.66:80',
    '103.155.62.163:8080',
    '3.143.37.255:80',
    '95.154.104.147:44393',
    '195.154.106.167:80',
    '138.2.70.213:80',
    '103.148.192.83:8089',
    '34.81.72.31:80',
    '201.229.250.21:8080',
    '103.171.182.225:8080',
    '93.180.222.134:8080',
    '189.250.93.75:80',
    '74.208.51.197:5000',
    '45.32.245.26:80',
    '43.255.113.232:8082',
    '146.59.243.214:80',
    '103.178.54.149:80',
    '51.89.73.43:80',
    '20.111.54.16:80',
    '20.205.61.143:80',
    '23.95.94.41:3128',
    '192.248.125.3:80',
    '128.111.5.234:3128',
    '83.171.248.156:3128',
    '152.69.215.206:80',
    '195.201.231.22:8080',
    '139.99.135.214:80',
    '2.58.56.143:8080',
    '202.173.214.77:80',
    '45.84.241.250:3128',
    '20.69.79.158:8443',
    '31.186.239.245:8080',
    '198.11.175.192:8081',
    '13.71.80.224:80',
    '185.73.202.85:80',
    '191.252.193.200:8080',
    '51.222.155.142:80',
    '47.245.34.161:8080',
    '146.83.128.23:80',
    '168.119.119.107:80',
    '115.144.102.39:10080',
    '51.68.181.108:80',
    '149.202.172.113:80',
    '47.74.152.29:8888',
    '82.146.37.145:80',
    '185.233.104.162:80',
    '52.24.80.166:80',
    '125.17.80.226:8080',
    '162.223.94.164:80',
    '43.230.202.171:80',
    '139.162.78.109:3128',
    '102.68.85.187:80',
    '152.32.202.108:80',
    '137.184.232.148:80',
    '174.70.1.210:8080',
    '104.223.135.178:10000',
    '103.169.255.74:8080',
    '49.0.246.130:45554',
    '139.59.1.14:3128',
    '137.184.197.190:80',
    '138.219.244.154:6666',
    '45.189.117.74:999',
    '45.179.245.1:999',
    '157.230.241.133:36835',
    '15.206.33.130:1080',
    '102.177.192.84:3128',
    '193.123.243.148:80',
    '68.178.161.107:80',
    '202.61.204.51:80',
    '51.79.50.22:9300',
    '45.84.241.4:3128',
    '117.54.114.97:80',
    '8.208.90.243:443',
    '172.104.117.89:80',
    '117.54.114.96:80',
    '201.212.246.80:80',
    '163.172.85.30:80',
    '195.190.144.6:80',
    '108.61.174.218:80',
    '161.35.161.38:80',
    '138.2.9.75:8080',
    '137.74.65.101:80',
    '125.17.80.227:8080',
    '125.17.80.229:8080',
    '51.68.124.241:80',
    '14.139.242.7:80',
    '82.66.172.182:80',
    '45.85.45.30:80',
    '191.252.178.3:80',
    '178.32.101.200:80',
    '47.243.177.210:8088',
    '158.69.157.172:80',
    '103.234.55.173:80',
    '161.97.93.15:80',
    '82.102.10.125:18345',
    '117.54.114.101:80',
    '185.103.87.30:8081',
    '164.52.192.156:80',
    '193.31.27.123:80',
    '142.132.243.163:3128',
    '78.138.98.115:3128',
    '13.75.216.118:3128',
    '201.17.26.54:80',
    '45.32.246.111:80',
]


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

inputs = []
def teamHarvesterEven(x, counter):
    surely = counter
    team_stats = []
    ind = random.randint(0, len(proxy) - 1)
    temp = proxy[ind]
    try:
        vals = []
        ind = random.randint(0, len(proxy) - 1)
        temp = proxy[ind]
        link = 'https://www.basketball-reference.com/teams/' + x + '/2023.html#per_game'

        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='per_game')
        headers = []
        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)

        vals = []
        ind = random.randint(0, len(proxy) - 1)
        temp = proxy[ind]
        link = 'https://www.espn.com/nba/injuries'

        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find_all('table')
        headers = []

        for i in text_table:
            for j in i.find(class_='AnchorLink'):
                title = i.text
                headers.append(title)

        counter = 0
        for i in headers:
            counter += 1
            headers[counter - 1] = headers[counter - 1].replace("NAMEPOSDATESTATUSCOMMENT", "")
        finalList = []
        for i in headers:
            for j in activePlayers:
                if i.find(j) != -1:
                    finalList.append(j)

        removal = []
        count = 0
        for i in headers:
            count += 1
            detector = False
            capitals = 0
            counter = 0
            for j in i:
                counter += 1
                if counter > 2:
                    if j.isupper():
                        capitals += 1
                    if capitals == 2:
                        detector = True
                        break
            removal.append(counter - 1)

        newNames = []
        counter = 0
        for i in headers:
            temp = ''
            counter += 1
            for j in range(removal[counter - 1]):
                temp += i[j]
            newNames.append(temp)

        vals = []
        ind = random.randint(0, len(proxy) - 1)
        temp = proxy[ind]
        link = 'https://www.basketball-reference.com/teams/' + x + '/2023.html#per_game'

        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='per_game')
        headers = []

        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)

        tempList = []
        counter = 0
        inputs = []
        index = 0
        freebie = True
        timer = 0
        for i in headers:
            counter += 1
            found = False
            if timer > 0:
                timer -= 1
            else:
                for j in finalList:
                    if i.find(j) != -1 or i == j:
                        timer = 26
                        found = True
                        index = counter
                        freebie = False
                if not found:
                    if counter > (index + 26) or freebie:
                        inputs.append(i)

        newInputs = []
        number = 0
        passes = 26
        for i in inputs:
            if number > 10:
                if passes == 0:
                    break
                else:
                    passes -= 1
                    newInputs.append(i)
            else:
                found = False
                for j in activePlayers:
                    if i.find(j) != -1:
                        found = True
                if not found:
                    newInputs.append(i)
                else:
                    number += 1

        time.sleep(5)
        team_stats = newInputs
        tempPlace = teamList[surely - 2]
        if x == 'BRK':
            x = 'NJN'
        if x == 'NOP':
            x = 'NOH'
        if x == 'CHO':
            x = 'CHA'
        if tempPlace == 'BRK':
            tempPlace = 'NJN'
        if tempPlace == 'NOP':
            tempPlace = 'NOH'
        if tempPlace == 'CHO':
            tempPlace = 'CHA'
        team_stats.append(0)
        link = "https://www.basketball-reference.com/teams/" + x + "/stats_per_game_totals.html"
        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='stats')
        headers = []
        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)
        team_stats.append(headers[4])
        for i in range(6, 33):
            if i == 7:
                g = list(headers[i])
                g[1] = '.'
                team_stats.append("".join(g))
            elif i != 9 and i != 10:
                team_stats.append(headers[i])

        time.sleep(5)
        link = "https://www.basketball-reference.com/teams/" + teamList[surely-2] + "/opp_stats_per_game_totals.html"
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



    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        print(exc_type, fname, exc_tb.tb_lineno)

    count = 0
    for i in team_stats:
        count += 1
        if i == '':
            team_stats[count - 1] = '0'
    count = 0
    for i in team_stats:
        count += 1
        team_stats[count - 1] = float(i)

    return team_stats


def teamHarvesterOdd(x, counter):
    surely = counter
    team_stats = []
    ind = random.randint(0, len(proxy) - 1)
    temp = proxy[ind]
    try:
        vals = []
        ind = random.randint(0, len(proxy) - 1)
        temp = proxy[ind]
        link = 'https://www.basketball-reference.com/teams/' + x + '/2023.html#per_game'

        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='per_game')
        headers = []
        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)

        vals = []
        ind = random.randint(0, len(proxy) - 1)
        temp = proxy[ind]
        link = 'https://www.espn.com/nba/injuries'

        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find_all('table')
        headers = []

        for i in text_table:
            for j in i.find(class_='AnchorLink'):
                title = i.text
                headers.append(title)

        counter = 0
        for i in headers:
            counter += 1
            headers[counter - 1] = headers[counter - 1].replace("NAMEPOSDATESTATUSCOMMENT", "")
        finalList = []
        for i in headers:
            for j in activePlayers:
                if i.find(j) != -1:
                    finalList.append(j)

        removal = []
        count = 0
        for i in headers:
            count += 1
            detector = False
            capitals = 0
            counter = 0
            for j in i:
                counter += 1
                if counter > 2:
                    if j.isupper():
                        capitals += 1
                    if capitals == 2:
                        detector = True
                        break
            removal.append(counter - 1)

        newNames = []
        counter = 0
        for i in headers:
            temp = ''
            counter += 1
            for j in range(removal[counter - 1]):
                temp += i[j]
            newNames.append(temp)

        vals = []
        ind = random.randint(0, len(proxy) - 1)
        temp = proxy[ind]
        link = 'https://www.basketball-reference.com/teams/'+x +'/2023.html#per_game'

        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='per_game')
        headers = []

        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)

        tempList = []
        counter = 0
        inputs = []
        index = 0
        freebie = True
        timer = 0
        for i in headers:
            counter += 1
            found = False
            if timer > 0:
                timer -= 1
            else:
                for j in finalList:
                    if i.find(j) != -1 or i == j:
                        timer = 26
                        found = True
                        index = counter
                        freebie = False
                if not found:
                    if counter > (index + 26) or freebie:
                        inputs.append(i)

        newInputs = []
        number = 0
        passes = 26
        for i in inputs:
            if number > 10:
                if passes == 0:
                    break
                else:
                    passes -= 1
                    newInputs.append(i)
            else:
                found = False
                for j in activePlayers:
                    if i.find(j) != -1:
                        found = True
                if not found:
                    newInputs.append(i)
                else:
                    number += 1

        time.sleep(5)
        team_stats = newInputs
        if x == 'BRK':
            x = 'NJN'
        if x == 'NOP':
            x = 'NOH'
        if x == 'CHO':
            x = 'CHA'
        tempPlace = teamList[surely]
        if teamList[surely] == 'BRK':
            tempPlace = 'NJN'
        if teamList[surely] == 'NOP':
            tempPlace = 'NOH'
        if teamList[surely] == 'CHO':
            tempPlace = 'CHA'
        team_stats.append(1)
        link = "https://www.basketball-reference.com/teams/" + x + "/stats_per_game_totals.html"
        page = requests.get(link, proxies={'http://': temp, 'https://': temp}, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')
        text_table = soup.find('table', id='stats')
        headers = []
        for i in text_table.find_all('td'):
            title = i.text
            headers.append(title)
        team_stats.append(headers[4])
        for i in range(6, 33):
            if i == 7:
                g = list(headers[i])
                g[1] = '.'
                team_stats.append("".join(g))
            elif i != 9 and i != 10:
                team_stats.append(headers[i])

        time.sleep(5)
        link = "https://www.basketball-reference.com/teams/" + teamList[surely] + "/opp_stats_per_game_totals.html"
        print(link)
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



    except Exception as e:

        exc_type, exc_obj, exc_tb = sys.exc_info()

        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

        print(exc_type, fname, exc_tb.tb_lineno)

    count = 0
    for i in team_stats:
        count += 1
        if i == '':
            team_stats[count - 1] = '0'
    count = 0
    for i in team_stats:
        count += 1
        team_stats[count - 1] = float(i)

    return team_stats


url = "https://www.sportsmediawatch.com/nba-tv-schedule/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

text_table = soup.find('table')
headers = []
for i in text_table.find_all('td'):
    title = i.text
    headers.append(title)
teamList = []
for i in headers:
    team1 = []
    team2 = []
    used = False
    if (i.find('Hawks')) > -1:
        team1.append('ATL')
        team1.append(i.find('Hawks'))
        used = True
    if (i.find('Pelicans')) > -1:
        if not used:
            team1.append('NOP')
            team1.append(i.find('Pelicans'))
        else:
            team2.append('NOP')
            team2.append(i.find('Pelicans'))
        used = True
    if (i.find('Timberwolves')) > -1:
        if not used:
            team1.append('MIN')
            team1.append(i.find('Timberwolves'))
        else:
            team2.append('MIN')
            team2.append(i.find('Timberwolves'))
        used = True
    if (i.find('Lakers')) > -1:
        if not used:
            team1.append('LAL')
            team1.append(i.find('Lakers'))
        else:
            team2.append('LAL')
            team2.append(i.find('Lakers'))
        used = True
    if (i.find('Warriors')) > -1:
        if not used:
            team1.append('GSW')
            team1.append(i.find('Warriors'))
        else:
            team2.append('GSW')
            team2.append(i.find('Warriors'))
        used = True
    if (i.find('Nets')) > -1:
        if not used:
            team1.append('BRK')
            team1.append(i.find('Nets'))
        else:
            team2.append('BRK')
            team2.append(i.find('Nets'))
        used = True
    if (i.find('Mavericks')) > -1:
        if not used:
            team1.append('DAL')
            team1.append(i.find('Mavericks'))
        else:
            team2.append('DAL')
            team2.append(i.find('Mavericks'))
        used = True
    if (i.find('Suns')) > -1:
        if not used:
            team1.append('PHO')
            team1.append(i.find('Suns'))
        else:
            team2.append('PHO')
            team2.append(i.find('Suns'))
        used = True
    if (i.find('Bucks')) > -1:
        if not used:
            team1.append('MIL')
            team1.append(i.find('Bucks'))
        else:
            team2.append('MIL')
            team2.append(i.find('Bucks'))
        used = True
    if (i.find('Knicks')) > -1:
        if not used:
            team1.append('NYK')
            team1.append(i.find('Knicks'))
        else:
            team2.append('NYK')
            team2.append(i.find('Knicks'))
        used = True
    if (i.find('Raptors')) > -1:
        if not used:
            team1.append('TOR')
            team1.append(i.find('Raptors'))
        else:
            team2.append('TOR')
            team2.append(i.find('Raptors'))
        used = True
    if (i.find('Bulls')) > -1:
        if not used:
            team1.append('CHI')
            team1.append(i.find('Bulls'))
        else:
            team2.append('CHI')
            team2.append(i.find('Bulls'))
        used = True
    if (i.find('Jazz')) > -1:
        if not used:
            team1.append('UTA')
            team1.append(i.find('Jazz'))
        else:
            team2.append('UTA')
            team2.append(i.find('Jazz'))
        used = True
    if (i.find('Cavaliers')) > -1:
        if not used:
            team1.append('CLE')
            team1.append(i.find('Cavaliers'))
        else:
            team2.append('CLE')
            team2.append(i.find('Cavaliers'))
        used = True
    if (i.find('76ers')) > -1:
        if not used:
            team1.append('PHI')
            team1.append(i.find('76ers'))
        else:
            team2.append('PHI')
            team2.append(i.find('76ers'))
        used = True
    if (i.find('Clippers')) > -1:
        if not used:
            team1.append('LAC')
            team1.append(i.find('Clippers'))
        else:
            team2.append('LAC')
            team2.append(i.find('Clippers'))
        used = True
    if (i.find('Heat')) > -1:
        if not used:
            team1.append('MIA')
            team1.append(i.find('Heat'))
        else:
            team2.append('MIA')
            team2.append(i.find('Heat'))
        used = True
    if (i.find('Blazers')) > -1:
        if not used:
            team1.append('POR')
            team1.append(i.find('Blazers'))
        else:
            team2.append('POR')
            team2.append(i.find('Blazers'))
        used = True
    if (i.find('Nuggets')) > -1:
        if not used:
            team1.append('DEN')
            team1.append(i.find('Nuggets'))
        else:
            team2.append('DEN')
            team2.append(i.find('Nuggets'))
        used = True
    if (i.find('Kings')) > -1:
        if not used:
            team1.append('SAC')
            team1.append(i.find('Kings'))
        else:
            team2.append('SAC')
            team2.append(i.find('Kings'))
        used = True
    if (i.find('Thunder')) > -1:
        if not used:
            team1.append('OKC')
            team1.append(i.find('Thunder'))
        else:
            team2.append('OKC')
            team2.append(i.find('Thunder'))
        used = True
    if (i.find('Grizzlies')) > -1:
        if not used:
            team1.append('MEM')
            team1.append(i.find('Grizzlies'))
        else:
            team2.append('MEM')
            team2.append(i.find('Grizzlies'))
        used = True
    if (i.find('Spurs')) > -1:
        if not used:
            team1.append('SAS')
            team1.append(i.find('Spurs'))
        else:
            team2.append('SAS')
            team2.append(i.find('Spurs'))
        used = True
    if (i.find('Rockets')) > -1:
        if not used:
            team1.append('HOU')
            team1.append(i.find('Bulls'))
        else:
            team2.append('HOU')
            team2.append(i.find('Bulls'))
        used = True
    if (i.find('Hornets')) > -1:
        if not used:
            team1.append('CHO')
            team1.append(i.find('Hornets'))
        else:
            team2.append('CHO')
            team2.append(i.find('Hornets'))
        used = True
    if (i.find('Pistons')) > -1:
        if not used:
            team1.append('DET')
            team1.append(i.find('Pistons'))
        else:
            team2.append('DET')
            team2.append(i.find('Pistons'))
        used = True
    if (i.find('Wizards')) > -1:
        if not used:
            team1.append('WAS')
            team1.append(i.find('Wizards'))
        else:
            team2.append('WAS')
            team2.append(i.find('Wizards'))
        used = True
    if (i.find('Magic')) > -1:
        if not used:
            team1.append('ORL')
            team1.append(i.find('Magic'))
        else:
            team2.append('ORL')
            team2.append(i.find('Magic'))
        used = True
    if (i.find('Pacers')) > -1:
        if not used:
            team1.append('IND')
            team1.append(i.find('Pacers'))
        else:
            team2.append('IND')
            team2.append(i.find('Pacers'))
        used = True
    if (i.find('Celtics')) > -1:
        if not used:
            team1.append('BOS')
            team1.append(i.find('Celtics'))
        else:
            team2.append('BOS')
            team2.append(i.find('Celtics'))
        used = True

    try:
        if team2[1] > team1[1]:

            teamList.append(team1[0])
            teamList.append(team2[0])
        else:

            teamList.append(team2[0])
            teamList.append(team1[0])
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)

storageDict = {
'ATL' : [],
'NOP' : [],
'MIN' : [],
'LAL' : [],
'GSW' : [],
'BRK' : [],
'DAL' : [],
'PHO' : [],
'MIL' : [],
'NYK' : [],
'TOR' : [],
'CHI' : [],
'UTA' : [],
'CLE' : [],
'PHI' : [],
'LAC' : [],
'MIA' : [],
'POR' : [],
'DEN' : [],
'SAC' : [],
'OKC' : [],
'MEM' : [],
'SAS' : [],
'HOU' : [],
'CHO' : [],
'DET' : [],
'WAS' : [],
'ORL' : [],
'IND' : [],
'BOS' : [],
}
counter = 0

for i in teamList:
    counter += 1
    if counter % 2 == 0:
        storageDict[i] = teamHarvesterEven(i, counter)
    else:
        storageDict[i] = teamHarvesterOdd(i, counter)
    time.sleep(5)

print(storageDict)

with open('scoresofYesterday', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
with open('scoresofYesterday', 'a') as o:
    o.write(',')

counter = 0

for teams,values in storageDict.items():
    counter += 1
    with open("NBAdataForTraining.txt", "a") as o:
        o.write(str(teams) + ': [')
    count = 0
    for i in values:
        count += 1
        with open("NBAdataForTraining.txt", "a") as o:
            o.write(str(i))
        if count != len(values):
            with open("NBAdataForTraining.txt", "a") as o:
                o.write(',')
    if counter == len(storageDict):
        with open("NBAdataForTraining.txt", "a") as o:
            o.write(str(']}'))
    else:
        with open("NBAdataForTraining.txt", "a") as o:
            o.write(str('],'))

with open('scoresofYesterday', 'a') as o:
    o.write(']')

