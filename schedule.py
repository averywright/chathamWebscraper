from bs4 import BeautifulSoup
import requests
import numpy as np
import random
import math
import time
import pandas as pd
from io import StringIO
import time

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
'Alperen Þengün',
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
'Jae\'Sean Tate',
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
'Ivica Zubac',
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
	weights -= np.reshape(derivativeWeights(x, weights, actual, bias, y),(49, 1)) * LR

def teamHarvesterEven(x, counter):
	team_stats = []
	ind = random.randint(0,len(proxy)-1)
	temp = proxy[ind]
	try:
		link = "https://www.basketball-reference.com/teams/" + x + "/stats_per_game_totals.html"
		page = requests.get(link, proxies = {'http://': temp, 'https://':temp}, timeout = 5)
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
			elif i != 9 and i !=10:
				team_stats.append(headers[i])
		link = "https://www.basketball-reference.com/teams/" + teamList[counter-2] + "/opp_stats_per_game_totals.html"
		page = requests.get(link, proxies = {'http://': temp, 'https://':temp}, timeout = 5)
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
	ind = random.randint(0,len(proxy)-1)
	temp = proxy[ind]
	try:
		link = "https://www.basketball-reference.com/teams/" + x + "/stats_per_game_totals.html"
		page = requests.get(link, proxies = {'http://': temp, 'https://':temp}, timeout = 5)
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
		page = requests.get(link, proxies = {'http://': temp, 'https://':temp}, timeout = 5)
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
	ind = random.randint(0,len(proxy)-1)
	temp = proxy[ind]
	link = 'https://www.basketball-reference.com/teams/' + x + '/2023.html#advanced'
	page = requests.get(link, proxies = {'http://': temp, 'https://':temp}, timeout = 5).text
	dfs = pd.read_csv(StringIO(page),error_bad_lines=False)

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
			team1.append('NOH')
			team1.append(i.find('Pelicans'))
		else:
			team2.append('NOH')
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
			team1.append('NJN')
			team1.append(i.find('Nets'))
		else:
			team2.append('NJN')
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
			team1.append('CHA')
			team1.append(i.find('Hornets'))
		else:
			team2.append('CHA')
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
	except:
		print('')
inputs = []
counter = 0

for i in teamList:
	counter += 1
	if counter % 2 == 0:
		inputs.append(teamHarvesterEven(i,counter))
	else:
		inputs.append(teamHarvesterOdd(i,counter))
	print(inputs)
	print(i)
	time.sleep(5)
	"""if i == 'NOH':
		for j in shootingStats('NOP'):
			inputs[counter-1].append(j)
	else:
		for j in shootingStats(i):
			inputs[counter-1].append(j)"""

"""inputs = [[0, '1', '26.5', '6.6', '224', '240.8', '44.1', '86.1', '.512', '12.1', '30.8', '.392', '32.0', '55.4', '.578', '16.9', '22.5', '.750', '9.8', '33.0', '42.7', '29.1', '7.6', '4.5', '14.9', '19.1', '117.1', '2', '61', '242.9', '.465', '11.3', '30.8', '.366', '27.6', '52.7', '.524', '17.1', '22.1', '.775', '9.3', '30.9', '40.2', '22.8', '7.3', '4.2', '15.1', '21.0', '106.1'], [1, '2', '25.4', '6.6', '220', '242.9', '41.2', '84.3', '.489', '11.4', '31.5', '.363', '29.8', '52.9', '.563', '17.9', '23.0', '.778', '9.7', '32.2', '41.9', '24.9', '7.0', '4.4', '13.9', '18.6', '111.8', '1', '59', '240.8', '.480', '11.6', '33.2', '.349', '29.9', '53.4', '.561', '18.1', '23.7', '.762', '9.7', '30.3', '40.0', '25.7', '7.7', '4.5', '13.8', '19.8', '112.7'], [0, '1', '27.3', '6.6', '222', '243.4', '41.8', '88.2', '.474', '15.9', '42.2', '.378', '25.9', '45.9', '.563', '18.3', '22.1', '.826', '9.5', '35.6', '45.1', '26.4', '6.3', '5.3', '13.5', '19.0', '117.9', '4', '60', '240.4', '.477', '12.6', '33.6', '.374', '29.5', '54.6', '.540', '20.5', '25.4', '.808', '12.1', '33.6', '45.6', '26.3', '7.9', '5.1', '15.7', '20.1', '117.1'], [1, '4', '24.4', '6.6', '210', '240.4', '41.0', '89.4', '.459', '13.8', '38.2', '.362', '27.2', '51.2', '.532', '18.6', '23.4', '.796', '10.1', '31.5', '41.6', '26.4', '8.0', '5.8', '15.2', '21.3', '114.5', '1', '59', '243.4', '.466', '11.6', '32.8', '.353', '30.5', '57.3', '.531', '16.1', '20.7', '.776', '9.4', '34.1', '43.6', '22.9', '6.6', '3.9', '12.6', '19.5', '111.7'], [0, '5', '24.3', '6.6', '219', '242.1', '39.8', '87.5', '.455', '11.7', '33.2', '.354', '28.0', '54.2', '.517', '21.0', '27.1', '.773', '10.9', '31.3', '42.2', '22.8', '7.2', '3.7', '14.9', '22.4', '112.3', '4', '59', '241.3', '.475', '12.9', '37.2', '.346', '28.5', '49.9', '.571', '18.1', '23.2', '.780', '9.8', '32.2', '42.1', '25.7', '7.8', '5.0', '14.5', '20.4', '113.7'], [1, '4', '23.2', '6.7', '224', '241.3', '40.1', '85.1', '.472', '10.7', '30.6', '.350', '29.4', '54.5', '.540', '19.9', '25.4', '.787', '9.9', '32.6', '42.6', '22.7', '7.1', '4.6', '15.2', '20.3', '110.9', '5', '59', '242.1', '.493', '12.2', '33.7', '.361', '31.5', '55.0', '.574', '20.3', '25.7', '.788', '11.0', '34.0', '44.9', '25.6', '7.3', '5.5', '14.0', '21.7', '119.9'], [0, '1', '24.5', '6.6', '220', '240.9', '43.4', '92.3', '.470', '11.3', '32.8', '.345', '32.1', '59.5', '.539', '18.1', '25.2', '.718', '12.9', '34.9', '47.7', '25.3', '8.4', '6.1', '14.3', '20.1', '116.1', '2', '57', '242.2', '.472', '11.2', '32.6', '.344', '29.1', '52.8', '.550', '18.7', '23.8', '.785', '9.8', '32.2', '42.0', '23.8', '6.7', '4.8', '15.0', '19.8', '110.5'], [1, '2', '28.4', '6.6', '225', '242.2', '40.6', '84.1', '.483', '12.6', '32.9', '.384', '28.0', '51.2', '.546', '20.5', '24.7', '.830', '8.6', '31.9', '40.5', '25.1', '8.0', '4.7', '13.8', '20.4', '114.4', '1', '57', '240.9', '.449', '13.0', '36.5', '.357', '27.5', '53.6', '.513', '18.2', '23.3', '.782', '11.1', '32.9', '44.1', '26.5', '7.2', '5.3', '15.4', '21.0', '112.2'], [0, '3', '25.8', '6.6', '217', '242.5', '42.3', '88.1', '.480', '10.8', '30.3', '.355', '31.5', '57.8', '.545', '19.6', '25.1', '.780', '11.1', '33.1', '44.1', '25.7', '8.5', '4.2', '15.0', '20.8', '114.9', '5', '59', '241.7', '.490', '12.4', '33.5', '.371', '28.2', '49.3', '.571', '18.8', '23.7', '.794', '9.3', '33.0', '42.3', '26.0', '6.0', '4.6', '16.6', '20.7', '112.5'], [1, '5', '25.8', '6.7', '217', '241.7', '41.5', '90.9', '.456', '10.9', '32.3', '.336', '30.6', '58.5', '.523', '19.5', '24.9', '.782', '12.7', '30.1', '42.8', '23.3', '9.3', '5.3', '11.8', '20.5', '113.3', '3', '59', '242.5', '.474', '12.2', '36.0', '.340', '29.2', '51.4', '.569', '18.3', '23.6', '.777', '9.8', '32.3', '42.1', '25.3', '7.3', '5.1', '15.1', '20.8', '113.5'], [0, '4', '24.2', '6.6', '218', '241.7', '43.0', '91.8', '.469', '10.5', '30.9', '.341', '32.5', '60.9', '.533', '15.8', '21.2', '.747', '12.0', '31.1', '43.0', '26.9', '7.0', '3.9', '15.6', '20.2', '112.4', '2', '60', '243.3', '.484', '11.0', '31.3', '.351', '30.0', '53.4', '.562', '19.5', '24.9', '.784', '9.7', '34.1', '43.8', '24.3', '6.3', '4.0', '13.5', '22.6', '112.5'], [1, '2', '27.9', '6.6', '216', '243.3', '39.4', '83.3', '.473', '14.8', '40.6', '.364', '24.6', '42.8', '.575', '19.5', '26.0', '.749', '8.0', '30.7', '38.7', '22.4', '6.5', '3.7', '12.4', '20.7', '113.0', '4', '59', '241.7', '.509', '12.4', '31.5', '.394', '33.6', '58.9', '.570', '18.2', '23.6', '.772', '10.7', '33.4', '44.2', '26.5', '8.3', '4.9', '14.0', '18.6', '122.6'], [0, '3', '23.0', '6.6', '202', '242.6', '43.6', '92.5', '.471', '12.2', '33.5', '.364', '31.4', '59.0', '.532', '18.6', '23.1', '.803', '11.4', '32.4', '43.7', '24.7', '8.3', '4.9', '13.5', '21.4', '117.9', '5', '60', '241.3', '.479', '11.7', '32.3', '.362', '31.7', '58.3', '.544', '18.7', '24.2', '.774', '11.6', '31.9', '43.5', '24.1', '7.8', '4.8', '13.2', '21.2', '117.2'], [1, '5', '26.8', '6.6', '215', '241.3', '42.3', '89.2', '.475', '14.1', '38.9', '.362', '28.3', '50.3', '.562', '18.8', '23.9', '.788', '11.8', '32.9', '44.7', '25.7', '6.4', '4.9', '15.2', '20.6', '117.6', '3', '57', '242.6', '.470', '12.7', '35.4', '.358', '29.0', '53.4', '.544', '20.2', '25.8', '.781', '12.1', '34.5', '46.5', '25.4', '7.4', '5.5', '16.9', '20.1', '116.2']]
"""

for i in inputs:
	counter = 0
	for j in i:
		counter += 1
		i[counter-1] = float(j)

"""
bias = 110
weights = np.random.rand(49, 1)"""
counter = 0

"""for i in weights:
	counter += 1
	g = random.randint(0, 1)
	weights[counter - 1] = weights[counter - 1] * (1/1000)
	if g == 1:
		weights[counter - 1] = weights[counter - 1] * -1
"""
"""results = [116,107]"""
"""results = [116,107, 114,106,112,100]
inputs = [[0.0, 2.0, 29.4, 6.6, 219.0, 61.0, 241.2, 40.3, 85.8, 0.469, 12.7, 33.5, 0.378, 27.6, 52.3, 0.528, 18.3, 23.5, 0.777, 9.9, 33.6, 43.5, 22.9, 6.8, 4.6, 14.0, 19.5, 111.4, 3.0, 60.0, 241.7, 85.7, 0.467, 11.4, 31.7, 0.359, 28.7, 54.0, 0.531, 19.8, 25.1, 0.791, 10.4, 32.6, 42.9, 23.6, 7.5, 4.0, 15.0, 20.3, 111.3], [1.0, 3.0, 27.9, 6.5, 216.0, 60.0, 241.7, 41.7, 89.6, 0.465, 12.3, 32.6, 0.378, 29.3, 57.1, 0.514, 17.1, 21.5, 0.793, 11.9, 32.0, 43.9, 27.2, 7.4, 5.0, 14.2, 21.0, 112.7, 2.0, 61.0, 241.2, 87.1, 0.47, 12.2, 33.6, 0.364, 28.7, 53.6, 0.536, 17.0, 22.4, 0.759, 9.9, 33.1, 43.0, 24.5, 7.6, 4.2, 13.0, 19.5, 111.1], [0.0, 3.0, 26.4, 6.7, 213.0, 58.0, 240.9, 42.0, 86.6, 0.485, 11.4, 31.8, 0.359, 30.6, 54.8, 0.558, 18.3, 23.2, 0.786, 9.4, 34.7, 44.0, 25.3, 6.9, 5.4, 14.1, 19.1, 113.6, 2.0, 61.0, 241.2, 88.7, 0.47, 12.8, 34.8, 0.368, 28.9, 53.9, 0.537, 19.6, 26.0, 0.752, 11.6, 32.9, 44.4, 25.6, 8.2, 4.0, 15.9, 20.1, 115.8], [1.0, 2.0, 25.4, 6.6, 218.0, 61.0, 241.2, 42.8, 87.0, 0.492, 11.9, 33.5, 0.356, 30.9, 53.5, 0.577, 18.2, 23.5, 0.773, 9.1, 32.3, 41.4, 25.5, 8.1, 5.3, 15.7, 21.8, 115.7, 3.0, 58.0, 240.9, 90.1, 0.464, 11.7, 32.8, 0.357, 30.1, 57.2, 0.526, 18.0, 22.4, 0.802, 10.8, 32.2, 43.0, 23.8, 6.8, 4.7, 12.3, 19.6, 113.3], [0.0, 1.0, 29.6, 6.6, 224.0, 58.0, 242.2, 41.8, 90.1, 0.463, 14.4, 40.0, 0.359, 27.4, 50.1, 0.546, 16.9, 22.9, 0.738, 11.6, 37.6, 49.2, 24.7, 6.6, 5.0, 15.0, 18.4, 114.8, 3.0, 59.0, 242.1, 87.9, 0.469, 13.0, 36.7, 0.354, 28.3, 51.2, 0.552, 17.9, 22.7, 0.786, 9.5, 34.1, 43.6, 25.9, 6.7, 5.0, 14.7, 18.9, 113.4], [1.0, 3.0, 27.5, 6.6, 215.0, 59.0, 242.1, 42.3, 87.0, 0.486, 10.3, 28.8, 0.359, 32.0, 58.3, 0.549, 18.1, 22.3, 0.812, 8.5, 34.3, 42.9, 24.1, 7.5, 4.5, 13.9, 19.5, 113.1, 1.0, 58.0, 242.2, 92.2, 0.453, 11.6, 33.5, 0.346, 30.2, 58.8, 0.514, 16.5, 21.2, 0.779, 10.6, 33.4, 44.1, 22.8, 7.1, 4.1, 12.0, 19.1, 111.6]]
""""""results = [125,131,113,123,109,120,124,134,126,101]"""
"""inputsForTraining = [[0.0, 1.0, 27.3, 6.6, 222.0, 58.0, 243.4, 41.7, 88.1, 0.473, 15.9, 42.2, 0.376, 25.8, 45.9, 0.563, 18.4, 22.3, 0.826, 9.5, 35.6, 45.1, 26.3, 6.2, 5.3, 13.5, 19.0, 117.7, 1.0, 57.0, 242.2, 41.9, 0.454, 11.6, 33.5, 0.346, 30.3, 58.7, 0.516, 16.5, 21.2, 0.779, 10.5, 33.4, 43.9, 22.9, 7.2, 4.2, 12.1, 19.1, 111.8], [1.0, 1.0, 29.6, 6.6, 224.0, 57.0, 242.2, 41.8, 90.2, 0.464, 14.3, 39.9, 0.359, 27.5, 50.3, 0.547, 16.9, 23.0, 0.737, 11.7, 37.5, 49.2, 24.7, 6.6, 4.9, 15.1, 18.4, 114.9, 1.0, 58.0, 243.4, 90.2, 0.466, 11.6, 32.9, 0.353, 30.4, 57.4, 0.53, 16.2, 20.8, 0.776, 9.5, 34.2, 43.7, 22.8, 6.6, 3.9, 12.6, 19.6, 111.8], [0.0, 4.0, 23.2, 6.7, 224.0, 59.0, 241.3, 40.1, 85.1, 0.472, 10.7, 30.6, 0.35, 29.4, 54.5, 0.54, 19.9, 25.4, 0.787, 9.9, 32.6, 42.6, 22.7, 7.1, 4.6, 15.2, 20.3, 110.9, 5.0, 59.0, 241.7, 40.6, 0.49, 12.4, 33.5, 0.371, 28.2, 49.3, 0.571, 18.8, 23.7, 0.794, 9.3, 33.0, 42.3, 26.0, 6.0, 4.6, 16.6, 20.7, 112.5], [1.0, 5.0, 25.8, 6.7, 217.0, 59.0, 241.7, 41.5, 90.9, 0.456, 10.9, 32.3, 0.336, 30.6, 58.5, 0.523, 19.5, 24.9, 0.782, 12.7, 30.1, 42.8, 23.3, 9.3, 5.3, 11.8, 20.5, 113.3, 4.0, 59.0, 241.3, 87.1, 0.475, 12.9, 37.2, 0.346, 28.5, 49.9, 0.571, 18.1, 23.2, 0.78, 9.8, 32.2, 42.1, 25.7, 7.8, 5.0, 14.5, 20.4, 113.7], [0.0, 1.0, 25.4, 6.6, 212.0, 57.0, 241.3, 43.2, 87.4, 0.494, 13.2, 36.3, 0.365, 29.9, 51.1, 0.585, 19.9, 24.8, 0.802, 9.1, 32.7, 41.8, 26.8, 6.9, 3.3, 14.0, 19.8, 119.5, 2.0, 59.0, 241.7, 40.1, 0.467, 11.4, 31.6, 0.36, 28.7, 54.1, 0.53, 19.7, 25.0, 0.789, 10.4, 32.5, 42.9, 23.5, 7.5, 4.1, 15.0, 20.4, 111.2], [1.0, 2.0, 27.9, 6.5, 216.0, 59.0, 241.7, 41.6, 89.6, 0.465, 12.3, 32.6, 0.379, 29.3, 57.1, 0.514, 17.2, 21.6, 0.793, 12.0, 32.1, 44.0, 27.2, 7.3, 5.0, 14.2, 20.9, 112.8, 1.0, 57.0, 241.3, 88.9, 0.493, 11.8, 32.1, 0.367, 32.0, 56.8, 0.564, 17.8, 22.4, 0.793, 9.7, 32.3, 42.0, 25.8, 7.4, 4.2, 14.4, 20.9, 117.2], [0.0, 4.0, 27.2, 6.5, 209.0, 58.0, 242.2, 43.1, 90.1, 0.479, 16.6, 43.0, 0.386, 26.5, 47.1, 0.563, 15.8, 20.0, 0.788, 9.9, 33.8, 43.7, 29.9, 7.1, 3.7, 16.4, 22.1, 118.6, 3.0, 60.0, 241.3, 40.9, 0.47, 12.2, 33.6, 0.364, 28.7, 53.5, 0.536, 17.1, 22.5, 0.759, 9.9, 33.2, 43.1, 24.4, 7.5, 4.3, 12.9, 19.4, 111.2], [1.0, 3.0, 29.4, 6.6, 219.0, 60.0, 241.3, 40.3, 85.9, 0.469, 12.7, 33.5, 0.378, 27.6, 52.4, 0.527, 18.2, 23.4, 0.775, 9.9, 33.6, 43.5, 22.8, 6.8, 4.7, 14.0, 19.5, 111.4, 4.0, 58.0, 242.2, 90.1, 0.474, 12.8, 35.3, 0.363, 29.9, 54.8, 0.546, 20.2, 26.0, 0.777, 10.6, 33.3, 43.8, 25.6, 7.8, 4.1, 14.7, 18.5, 118.5], [0.0, 3.0, 26.4, 6.7, 213.0, 57.0, 240.9, 42.0, 86.4, 0.485, 11.4, 31.7, 0.358, 30.6, 54.7, 0.559, 18.3, 23.4, 0.785, 9.3, 34.6, 43.9, 25.3, 6.8, 5.4, 14.1, 19.2, 113.6, 4.0, 58.0, 240.9, 42.1, 0.484, 12.0, 32.5, 0.37, 30.1, 54.5, 0.551, 18.9, 24.0, 0.787, 10.2, 31.2, 41.4, 26.0, 7.5, 4.2, 13.3, 21.4, 115.0], [1.0, 4.0, 25.6, 6.6, 215.0, 58.0, 240.9, 40.8, 84.6, 0.482, 13.0, 34.8, 0.374, 27.8, 49.8, 0.557, 20.3, 25.2, 0.803, 9.9, 31.7, 41.6, 24.2, 6.3, 4.3, 14.6, 20.6, 114.9, 3.0, 57.0, 240.9, 90.0, 0.465, 11.8, 32.9, 0.359, 30.1, 57.1, 0.527, 17.9, 22.4, 0.8, 10.7, 32.1, 42.8, 23.9, 6.8, 4.7, 12.2, 19.7, 113.5]]
"""
"""weights = [[ 0.7938378 ],
 [ 0.58481567],
 [ 0.728147  ],
 [ 0.43653874],
 [-0.41798524],
 [ 0.51142136],
 [-0.20288431],
 [-0.27380628],
 [ 0.26317975],
 [ 0.4220772 ],
 [ 0.54216738],
 [ 0.59086408],
 [ 0.69902406],
 [ 0.19842979],
 [-0.09348921],
 [ 0.84141365],
 [ 0.38429408],
 [ 0.64623996],
 [ 0.38634015],
 [ 0.13583365],
 [ 0.22605342],
 [ 0.05850765],
 [-0.00185731],
 [ 0.87666616],
 [ 0.20026259],
 [ 0.47448059],
 [ 0.30942885],
 [ 0.20621059],
 [ 0.90594373],
 [ 0.69856901],
 [-0.83601962],
 [-0.03149503],
 [ 0.97003407],
 [ 0.60852127],
 [ 0.64393377],
 [ 0.48466526],
 [ 0.4024259 ],
 [-0.06615311],
 [ 0.87007942],
 [ 0.76746178],
 [ 0.76716104],
 [ 0.61744718],
 [ 0.63190336],
 [-0.03250032],
 [ 0.21764705],
 [ 0.29942914],
 [ 0.49235175],
 [ 0.45100924],
 [ 0.13797242],
 [ 0.12773567],
 [ 0.22200706]]"""
"""
weights = [[ 2.28655339e-01],
 [ 5.01369670e-01],
 [-6.75407789e-02],
 [ 7.75463437e-01],
 [-1.14641841e+00],
 [-9.14031610e-01],
 [ 2.58243981e-01],
 [ 4.55542363e-02],
 [ 5.95059687e-01],
 [ 5.44068477e-01],
 [ 5.83277460e-01],
 [ 2.06046677e-01],
 [ 1.89772992e-01],
 [-2.43957281e-01],
 [ 6.57116953e-01],
 [ 4.33304235e-01],
 [ 8.72328328e-01],
 [ 9.21519516e-01],
 [ 5.13357459e-01],
 [ 4.44002586e-01],
 [ 1.74431892e-02],
 [ 4.51086005e-01],
 [ 9.08540143e-01],
 [ 4.08841174e-01],
 [ 5.35913393e-01],
 [ 1.29979080e-01],
 [ 1.77847645e-01],
 [ 3.73321148e-01],
 [ 3.68772410e-01],
 [-5.21468670e-01],
 [ 7.00985276e-01],
 [ 8.04567752e-01],
 [ 4.93750711e-01],
 [ 8.39216714e-01],
 [ 3.00853019e-01],
 [ 2.86591589e-01],
 [ 4.45773612e-01],
 [ 4.56233599e-01],
 [-3.88527209e-03],
 [ 6.28344381e-01],
 [ 1.71182373e-01],
 [ 2.22685231e-01],
 [ 3.95280599e-01],
 [-1.39749425e-01],
 [-3.35510184e-02],
 [ 6.06567482e-01],
 [ 5.71740715e-01],
 [ 2.67025589e-01],
 [ 2.89144516e-01],
 [ 7.69998979e-01],
 [ 2.91715934e-01],
 [ 3.22449600e-01],
 [ 3.58295965e-02],
 [ 8.17031581e-01],
 [ 9.50389335e-01],
 [ 4.37662921e-01],
 [ 4.59714316e-01],
 [ 1.83783178e-01],
 [ 6.65852485e-01],
 [ 4.11969898e-01],
 [ 6.75745658e-01],
 [ 1.11248718e-02],
 [ 9.80493292e-01],
 [ 6.62345853e-01],
 [ 5.48714068e-01],
 [ 9.96270939e-01],
 [ 6.14922224e-01],
 [ 8.33684281e-01],
 [ 4.53536026e-01],
 [ 8.43368183e-01],
 [ 9.46431012e-01],
 [ 5.84139439e-01],
 [ 7.18473566e-01],
 [ 1.49138445e-01],
 [ 2.42297509e-01],
 [ 5.13615705e-02],
 [ 3.63018031e-01],
 [ 5.28117154e-01],
 [ 8.21719785e-01],
 [ 6.74885328e-01],
 [ 8.37655689e-01],
 [ 7.39640446e-01],
 [ 6.03362928e-02],
 [ 6.70560559e-01],
 [ 2.33357377e-01],
 [ 7.21461818e-02],
 [ 8.25641249e-01],
 [ 8.03852177e-01],
 [ 4.21156927e-01],
 [ 5.56378497e-01],
 [ 3.02134525e-02],
 [ 8.35482614e-01],
 [ 1.55411108e-01],
 [ 5.70733205e-01],
 [ 8.63631240e-01],
 [ 4.74713715e-01],
 [ 2.00834507e-01],
 [-3.04783178e-02],
 [ 9.01146230e-02],
 [ 5.92082771e-01],
 [ 6.14820198e-01],
 [ 3.78543529e-01],
 [ 2.06742344e-01],
 [ 8.70406621e-01],
 [ 1.13455283e-02],
 [ 1.77075156e-01],
 [ 3.68917688e-01],
 [ 6.05318863e-01],
 [ 9.39083992e-01],
 [ 8.14971659e-01],
 [ 7.53377744e-01],
 [ 3.12053783e-01],
 [ 5.66488043e-01],
 [ 4.12139891e-01],
 [ 6.53169844e-01],
 [ 5.31859142e-01],
 [ 5.61178099e-01],
 [ 8.31053044e-02],
 [ 1.48522825e-01],
 [ 4.07660431e-01],
 [ 2.14692723e-01],
 [ 6.28735385e-01],
 [ 4.91265517e-01],
 [ 9.02588974e-01],
 [ 2.56876076e-01],
 [ 9.69352668e-01],
 [ 3.02563040e-01],
 [ 5.96344140e-01],
 [ 4.53414437e-01],
 [ 6.69996512e-03],
 [ 8.05032886e-01],
 [ 7.90996925e-01],
 [ 5.40083836e-01],
 [ 9.36965959e-01],
 [ 5.07849706e-02],
 [ 5.42701720e-01],
 [ 5.53281609e-02],
 [ 2.71155456e-01],
 [ 3.73320958e-04],
 [ 8.84638206e-01],
 [ 3.81920719e-01],
 [ 8.16250001e-01],
 [ 5.61685465e-01],
 [ 1.54552085e-01],
 [-4.53093154e-02],
 [-1.73050194e-01],
 [ 1.06628142e-01],
 [ 4.65858651e-01],
 [ 8.64964457e-01],
 [ 4.29732195e-01],
 [ 9.67611948e-01],
 [ 9.00082273e-01],
 [ 4.11712948e-02],
 [ 5.50087248e-01],
 [ 2.86890259e-01],
 [ 6.76521285e-01],
 [ 5.22276087e-01],
 [ 2.32392873e-02],
 [ 3.71297498e-01],
 [ 1.49905890e-01],
 [ 6.49252488e-01],
 [ 9.02653397e-01],
 [ 3.22170179e-01],
 [ 3.87399523e-02],
 [ 9.01552951e-01],
 [ 6.05581712e-01],
 [ 6.29587735e-01],
 [ 8.82117167e-01],
 [ 2.85543072e-01],
 [-6.59177336e-02],
 [-5.21274152e-02],
 [ 3.70862040e-01],
 [ 2.00093679e-01],
 [ 1.43938548e-01],
 [ 5.60308667e-01],
 [ 3.30429245e-01],
 [ 4.47448600e-01],
 [ 9.82989312e-01],
 [ 9.34106356e-01],
 [ 5.88064147e-01],
 [ 1.00645483e-04],
 [ 4.73403822e-01],
 [ 9.14776693e-01],
 [ 2.84770095e-01],
 [ 3.08779270e-01],
 [ 5.80794188e-01],
 [ 7.21783517e-02],
 [ 8.91186967e-01],
 [ 7.26251108e-01],
 [ 1.70722697e-01],
 [ 7.30526295e-01],
 [ 6.09427527e-01],
 [ 5.44643477e-01],
 [ 8.43807974e-01],
 [ 6.15284639e-01],
 [ 6.43112291e-01],
 [ 6.70353393e-01],
 [ 6.26524252e-01],
 [ 3.96855021e-02],
 [ 3.54366171e-02],
 [ 8.99111082e-01],
 [ 5.06718975e-01],
 [ 5.67835862e-01],
 [ 5.78899052e-01],
 [ 4.09769537e-01],
 [ 5.87502392e-01],
 [ 8.49142311e-02],
 [ 1.44620573e-02],
 [ 6.90026114e-01],
 [ 7.41704543e-01],
 [ 6.97403978e-02],
 [ 8.77148286e-01],
 [ 3.88639220e-01],
 [ 3.74204869e-01],
 [ 6.01641816e-01],
 [ 7.46681186e-01],
 [ 7.85565878e-01],
 [ 6.25890146e-01],
 [ 2.22976054e-01],
 [ 8.79527242e-01],
 [ 1.78817203e-01],
 [ 5.17223886e-01],
 [ 7.83186203e-01],
 [ 9.17884227e-01],
 [ 6.52125297e-01],
 [ 2.00677421e-01],
 [ 7.94592531e-01],
 [ 1.13923188e-01],
 [ 1.93137613e-01],
 [ 5.76715116e-01],
 [ 2.39085156e-01],
 [ 8.27465331e-02],
 [ 2.12635226e-01],
 [ 3.30959849e-01],
 [ 5.61975986e-01],
 [ 4.66747065e-01],
 [ 4.07001077e-01],
 [ 8.92756316e-01],
 [ 6.66525844e-01],
 [ 7.83165308e-01],
 [ 6.56706398e-01],
 [ 7.88809418e-01],
 [ 5.19600438e-01],
 [ 8.30811439e-02],
 [ 7.39271056e-02],
 [ 7.13532189e-01],
 [ 1.81895580e-02],
 [ 8.40239104e-01],
 [ 7.02474940e-01],
 [ 4.95893455e-01],
 [ 7.43854207e-01],
 [ 8.96667100e-01],
 [ 8.59908040e-01],
 [ 3.01985686e-01],
 [ 1.80223531e-01],
 [ 2.67150093e-02],
 [ 3.73652131e-03],
 [ 6.51161620e-01],
 [ 4.83149437e-01],
 [ 6.06209732e-01],
 [ 6.54598120e-01],
 [ 6.99209146e-02],
 [ 4.96102138e-01],
 [ 6.70592716e-01],
 [ 9.70787254e-01],
 [ 8.10470866e-01],
 [ 8.06677275e-01],
 [ 4.51197019e-01],
 [ 1.74058215e-01],
 [ 6.57380507e-01],
 [ 9.86564209e-01],
 [ 4.17048203e-01],
 [ 4.54248229e-01],
 [ 8.43638858e-01],
 [ 3.55624015e-01],
 [ 5.18303710e-01],
 [ 5.94305711e-01],
 [ 8.27597380e-01],
 [ 5.35629428e-01],
 [ 6.93430979e-01],
 [ 5.03063286e-01],
 [ 7.05113511e-01],
 [ 7.86677730e-01],
 [ 6.94958532e-01],
 [ 8.09774937e-01],
 [ 5.05751608e-01],
 [ 7.86499942e-01],
 [ 1.70656769e-01],
 [ 3.28209103e-01]]"""
"""
 
bias = 110
"""
"""count = 0
for i in range(99000):
	count = 0
	for i in inputs:
		count += 1
		back(inputs[count-1],results[count-1],weights,bias)
		


print(weights,bias)"""
"""print(relu(np.dot(inputs[0], weights) + bias), relu(np.dot(inputs[1], weights) + bias))"""

"""results = [115,109,142,138,106,108,105,110,110,115,116,142,119,120]
count = 0
for i in range(99000):
	count = 0
	for i in inputs:
		count += 1
		back(inputs[count-1],results[count-1],weights,bias)

print(weights, bias)"""

weights = [[ 1.00657559],
 [ 0.37112949],
 [ 0.60681323],
 [ 0.81477103],
 [-0.1315721 ],
 [-0.54891767],
 [ 0.6154639 ],
 [ 0.33357062],
 [ 0.39110564],
 [ 0.49790981],
 [ 1.31177101],
 [ 0.21038817],
 [-0.39293644],
 [-0.51032287],
 [ 0.22060853],
 [ 0.13401639],
 [-0.40416959],
 [ 0.90594801],
 [-0.26994568],
 [-0.16635895],
 [-0.05844039],
 [ 0.73948526],
 [ 0.37904023],
 [ 0.32169084],
 [-0.34886177],
 [ 0.44690206],
 [-0.130133  ],
 [ 0.14467585],
 [ 0.60286803],
 [ 0.01672887],
 [ 0.31929833],
 [ 0.48593724],
 [-0.96534859],
 [ 0.77199047],
 [ 1.09990936],
 [ 0.62895081],
 [ 0.40995949],
 [-0.04242227],
 [-0.38083646],
 [ 0.34406546],
 [ 0.44209639],
 [-0.03725852],
 [ 0.41334805],
 [ 0.27257437],
 [ 0.23897422],
 [ 0.59795425],
 [ 0.57032044],
 [ 0.27893557],
 [-0.28906152]]


"""print(teamList)"""
"""inputs = [[0, '1', '26.5', '6.6', '224', '240.8', '44.0', '86.1', '.511', '12.2', '30.9', '.394', '31.8', '55.2', '.576', '16.9', '22.5', '.752', '9.9', '32.9', '42.8', '29.1', '7.6', '4.5', '15.0', '19.2', '117.1', '2', '62', '242.8', '.465', '11.4', '30.9', '.368', '27.5', '52.6', '.523', '17.2', '22.1', '.777', '9.4', '30.9', '40.3', '22.9', '7.3', '4.2', '15.1', '20.9', '106.3'], [1, '2', '25.4', '6.6', '220', '242.8', '41.2', '84.4', '.488', '11.4', '31.4', '.362', '29.9', '53.0', '.564', '17.9', '23.0', '.779', '9.7', '32.2', '41.9', '24.9', '7.1', '4.4', '13.8', '18.7', '111.7', '1', '60', '240.8', '.480', '11.5', '33.1', '.348', '30.1', '53.6', '.561', '18.0', '23.6', '.763', '9.8', '30.3', '40.0', '25.7', '7.8', '4.4', '13.8', '19.9', '112.7'], [0, '1', '27.4', '6.6', '222', '243.8', '42.0', '88.4', '.475', '16.0', '42.2', '.379', '26.0', '46.2', '.563', '18.3', '22.2', '.826', '9.6', '35.5', '45.2', '26.5', '6.3', '5.3', '13.5', '19.0', '118.3', '4', '61', '240.8', '.477', '12.6', '33.7', '.375', '29.5', '54.7', '.540', '20.5', '25.4', '.809', '12.2', '33.5', '45.7', '26.4', '7.9', '5.1', '15.7', '20.0', '117.5'], [1, '4', '24.5', '6.6', '210', '240.8', '41.2', '89.5', '.460', '13.9', '38.3', '.363', '27.2', '51.1', '.533', '18.6', '23.4', '.796', '10.1', '31.4', '41.5', '26.5', '8.0', '5.8', '15.2', '21.3', '114.9', '1', '60', '243.8', '.467', '11.8', '33.1', '.355', '30.4', '57.1', '.532', '16.1', '20.8', '.777', '9.5', '34.0', '43.5', '23.0', '6.6', '3.9', '12.7', '19.6', '112.2'], [0, '5', '24.3', '6.6', '219', '242.1', '39.7', '87.4', '.455', '11.8', '33.2', '.356', '27.9', '54.1', '.516', '20.9', '27.0', '.773', '10.9', '31.4', '42.3', '22.8', '7.2', '3.8', '15.0', '22.4', '112.2', '4', '60', '241.3', '.475', '12.9', '37.1', '.348', '28.3', '49.8', '.569', '18.1', '23.2', '.780', '9.8', '32.4', '42.1', '25.7', '7.8', '5.1', '14.6', '20.4', '113.5'], [1, '4', '23.2', '6.7', '224', '241.3', '40.1', '85.3', '.470', '10.7', '30.6', '.351', '29.4', '54.6', '.538', '19.9', '25.3', '.787', '10.0', '32.7', '42.6', '22.8', '7.1', '4.6', '15.2', '20.3', '110.9', '5', '60', '242.1', '.491', '12.2', '33.7', '.361', '31.5', '55.1', '.571', '20.2', '25.7', '.788', '11.0', '34.0', '45.0', '25.7', '7.3', '5.5', '14.0', '21.7', '119.7'], [0, '1', '24.5', '6.6', '220', '240.9', '43.2', '92.2', '.469', '11.2', '32.8', '.343', '32.0', '59.4', '.539', '18.3', '25.3', '.720', '12.9', '34.9', '47.8', '25.2', '8.3', '6.1', '14.2', '20.3', '115.9', '2', '58', '242.2', '.470', '11.1', '32.6', '.342', '29.0', '52.8', '.549', '18.9', '24.0', '.786', '9.8', '32.3', '42.1', '23.8', '6.7', '4.9', '14.9', '19.9', '110.4'], [1, '2', '28.4', '6.6', '225', '242.2', '40.5', '84.1', '.481', '12.7', '33.0', '.384', '27.8', '51.2', '.544', '20.6', '24.9', '.829', '8.6', '32.0', '40.6', '25.1', '7.9', '4.8', '13.7', '20.5', '114.3', '1', '58', '240.9', '.449', '13.0', '36.4', '.357', '27.4', '53.5', '.511', '18.4', '23.5', '.783', '11.1', '33.0', '44.0', '26.5', '7.1', '5.4', '15.3', '21.1', '112.2'], [0, '3', '25.8', '6.6', '216', '242.5', '42.2', '88.1', '.479', '10.8', '30.3', '.356', '31.4', '57.8', '.544', '19.6', '25.1', '.780', '11.0', '33.1', '44.1', '25.7', '8.5', '4.2', '15.0', '20.8', '114.8', '5', '60', '241.7', '.490', '12.5', '33.4', '.372', '28.1', '49.4', '.570', '18.8', '23.7', '.794', '9.3', '33.1', '42.3', '26.0', '6.0', '4.6', '16.6', '20.7', '112.4'], [1, '5', '25.8', '6.7', '217', '241.7', '41.5', '90.9', '.457', '10.8', '32.3', '.335', '30.7', '58.6', '.523', '19.5', '24.9', '.783', '12.7', '30.2', '42.9', '23.2', '9.3', '5.3', '11.9', '20.5', '113.4', '3', '60', '242.5', '.474', '12.2', '35.9', '.339', '29.3', '51.5', '.569', '18.4', '23.6', '.778', '9.8', '32.3', '42.2', '25.1', '7.4', '5.1', '15.1', '20.8', '113.5'], [0, '4', '24.2', '6.6', '218', '241.7', '43.1', '91.8', '.469', '10.5', '30.8', '.342', '32.5', '60.9', '.534', '15.8', '21.2', '.746', '12.0', '31.1', '43.1', '27.0', '7.0', '3.9', '15.6', '20.3', '112.5', '2', '61', '243.3', '.485', '11.0', '31.1', '.352', '30.1', '53.6', '.562', '19.4', '24.8', '.783', '9.7', '34.1', '43.8', '24.4', '6.2', '3.9', '13.5', '22.7', '112.6'], [1, '2', '27.9', '6.6', '216', '243.3', '39.5', '83.3', '.474', '14.9', '40.6', '.367', '24.6', '42.7', '.576', '19.6', '26.2', '.750', '7.9', '30.7', '38.6', '22.4', '6.6', '3.8', '12.3', '20.7', '113.5', '4', '60', '241.7', '.510', '12.6', '31.7', '.397', '33.4', '58.6', '.570', '18.4', '23.8', '.772', '10.6', '33.4', '44.0', '26.5', '8.4', '5.0', '13.9', '18.6', '122.9'], [0, '4', '23.0', '6.6', '202', '243.0', '43.6', '92.8', '.470', '12.1', '33.5', '.361', '31.5', '59.3', '.531', '18.6', '23.2', '.802', '11.5', '32.4', '43.9', '24.7', '8.3', '4.8', '13.5', '21.4', '117.9', '3', '61', '241.6', '.478', '11.6', '32.4', '.359', '31.8', '58.5', '.543', '18.8', '24.2', '.774', '11.7', '32.0', '43.7', '24.1', '7.8', '4.8', '13.1', '21.2', '117.3'], [1, '3', '26.8', '6.6', '215', '241.6', '42.3', '89.3', '.474', '14.1', '39.0', '.360', '28.3', '50.3', '.562', '18.9', '23.9', '.790', '11.9', '33.0', '44.9', '25.7', '6.4', '5.0', '15.3', '20.8', '117.6', '4', '58', '243.0', '.469', '12.7', '35.6', '.356', '29.0', '53.3', '.544', '20.2', '25.8', '.782', '12.1', '34.6', '46.7', '25.4', '7.4', '5.6', '16.9', '20.2', '116.3'], [0, '4', '27.1', '6.5', '209', '242.1', '43.1', '90.4', '.477', '16.6', '43.1', '.384', '26.5', '47.2', '.561', '15.8', '20.0', '.788', '10.0', '33.7', '43.7', '29.8', '7.1', '3.7', '16.3', '22.1', '118.5', '5', '60', '242.9', '.470', '12.7', '36.6', '.346', '31.7', '57.6', '.550', '16.8', '21.8', '.771', '11.3', '34.4', '45.7', '25.9', '7.7', '5.3', '12.7', '21.3', '118.1']]
for i in inputs:
	counter = 0
	for j in i:
		counter += 1
		i[counter-1] = float(j)"""
"""inputs = [[0, '5', '28.5', '6.5', '212', '242.9', '43.2', '89.8', '.481', '10.5', '31.0', '.337', '32.7', '58.8', '.557', '20.2', '26.1', '.774', '9.7', '35.9', '45.7', '25.2', '6.5', '4.5', '14.0', '18.5', '117.0', '1', '59', '240.8', '.448', '13.0', '36.5', '.356', '27.3', '53.5', '.511', '18.3', '23.4', '.783', '11.1', '33.0', '44.1', '26.4', '7.1', '5.4', '15.3', '21.0', '111.9'], [1, '1', '24.5', '6.6', '220', '240.8', '43.3', '92.2', '.469', '11.3', '32.9', '.343', '32.0', '59.3', '.539', '18.1', '25.1', '.721', '12.8', '35.0', '47.8', '25.2', '8.4', '6.0', '14.2', '20.1', '115.9', '5', '61', '242.9', '.470', '12.8', '36.8', '.347', '31.4', '57.4', '.548', '16.7', '21.7', '.771', '11.3', '34.4', '45.7', '25.8', '7.6', '5.3', '12.8', '21.3', '117.9'], [0, '3', '26.4', '6.7', '213', '240.8', '41.8', '86.3', '.484', '11.5', '31.9', '.359', '30.3', '54.4', '.558', '18.1', '23.1', '.783', '9.3', '34.5', '43.8', '25.3', '6.8', '5.3', '14.3', '19.1', '113.0', '2', '61', '242.0', '.478', '11.8', '33.8', '.349', '31.1', '56.1', '.555', '19.2', '23.8', '.807', '10.9', '34.4', '45.2', '25.5', '7.5', '5.0', '14.4', '19.9', '117.0'], [1, '2', '24.9', '6.6', '209', '242.0', '44.2', '92.1', '.480', '10.7', '30.4', '.353', '33.5', '61.8', '.542', '17.9', '21.8', '.818', '10.6', '33.3', '43.9', '24.6', '7.0', '4.9', '12.8', '19.0', '116.9', '3', '60', '240.8', '.465', '11.7', '32.7', '.357', '30.2', '57.2', '.527', '17.8', '22.2', '.802', '10.8', '32.2', '43.0', '23.7', '6.9', '4.6', '12.3', '19.6', '113.2'], [0, '1', '29.6', '6.6', '224', '242.1', '41.8', '90.2', '.463', '14.4', '40.2', '.359', '27.4', '50.0', '.547', '16.8', '22.8', '.738', '11.6', '37.7', '49.3', '24.6', '6.5', '5.0', '14.9', '18.4', '114.9'], [], [0, '3', '27.5', '6.6', '215', '242.0', '42.4', '86.9', '.488', '10.3', '28.8', '.359', '32.1', '58.2', '.552', '18.1', '22.3', '.809', '8.6', '34.4', '43.0', '24.1', '7.5', '4.5', '13.8', '19.4', '113.2', '5', '62', '241.6', '.489', '12.4', '33.3', '.373', '28.1', '49.7', '.567', '18.6', '23.4', '.793', '9.4', '33.3', '42.7', '26.0', '6.0', '4.6', '16.5', '20.7', '112.2'], [1, '5', '25.8', '6.7', '217', '241.6', '41.3', '90.9', '.454', '10.7', '32.1', '.335', '30.5', '58.8', '.519', '19.4', '24.9', '.780', '12.6', '30.3', '42.9', '23.1', '9.2', '5.3', '11.8', '20.3', '112.7', '3', '61', '242.0', '.467', '12.9', '36.7', '.350', '28.1', '50.9', '.551', '17.7', '22.7', '.782', '9.5', '33.9', '43.4', '25.8', '6.7', '4.9', '14.7', '19.0', '112.4'], [0, '5', '22.5', '6.6', '214', '240.8', '39.8', '88.4', '.449', '10.8', '33.2', '.325', '29.0', '55.3', '.524', '19.4', '25.7', '.754', '13.2', '33.3', '46.5', '22.4', '7.2', '4.9', '16.8', '20.7', '109.7', '1', '62', '241.2', '.480', '11.5', '33.3', '.347', '30.1', '53.6', '.562', '18.0', '23.5', '.765', '9.7', '30.5', '40.2', '25.6', '7.8', '4.4', '13.7', '19.8', '112.8'], [1, '1', '26.6', '6.6', '225', '241.2', '43.9', '86.3', '.509', '12.1', '31.1', '.391', '31.8', '55.2', '.576', '16.9', '22.5', '.752', '9.9', '33.1', '43.0', '29.1', '7.5', '4.4', '15.0', '19.1', '117.0', '5', '60', '240.8', '.478', '14.7', '39.3', '.373', '27.5', '48.9', '.562', '19.5', '24.4', '.798', '10.5', '31.1', '41.7', '25.7', '9.0', '6.0', '13.4', '21.3', '118.3'], [0, '1', '25.4', '6.6', '212', '242.1', '43.6', '87.7', '.497', '13.4', '36.4', '.368', '30.2', '51.3', '.589', '20.1', '25.1', '.800', '9.2', '32.8', '42.0', '27.0', '7.1', '3.3', '14.2', '19.9', '120.7', '5', '60', '242.9', '.470', '12.8', '35.8', '.358', '29.0', '53.1', '.545', '20.2', '25.9', '.781', '12.2', '34.7', '46.9', '25.5', '7.3', '5.5', '16.9', '20.3', '116.6'], [1, '5', '23.0', '6.6', '202', '242.9', '43.5', '92.8', '.469', '12.2', '33.7', '.363', '31.3', '59.1', '.530', '18.6', '23.2', '.800', '11.5', '32.3', '43.9', '24.7', '8.3', '4.7', '13.4', '21.4', '117.8', '1', '60', '242.1', '.494', '12.2', '32.5', '.374', '31.8', '56.5', '.563', '17.9', '22.6', '.795', '9.6', '32.2', '41.8', '26.0', '7.5', '4.1', '14.6', '21.1', '118.1'], [0, '4', '24.5', '6.6', '210', '240.8', '41.3', '89.6', '.461', '14.0', '38.4', '.364', '27.3', '51.3', '.533', '18.5', '23.2', '.795', '10.1', '31.5', '41.6', '26.6', '8.0', '5.8', '15.1', '21.4', '115.0', '2', '62', '243.2', '.484', '10.9', '31.2', '.349', '30.2', '53.7', '.562', '19.5', '24.9', '.782', '9.8', '34.2', '44.0', '24.4', '6.3', '3.9', '13.5', '22.6', '112.5'], [1, '2', '27.9', '6.6', '216', '243.2', '39.5', '83.4', '.473', '15.0', '40.7', '.368', '24.5', '42.7', '.573', '19.5', '26.0', '.749', '7.9', '30.8', '38.8', '22.4', '6.5', '3.8', '12.4', '20.7', '113.4', '4', '62', '240.8', '.476', '12.5', '33.6', '.373', '29.5', '54.8', '.539', '20.7', '25.6', '.810', '12.2', '33.6', '45.9', '26.2', '7.8', '5.2', '15.6', '20.0', '117.4'], [0, '4', '24.2', '6.6', '218', '241.6', '43.0', '91.8', '.468', '10.5', '30.9', '.340', '32.5', '61.0', '.533', '15.9', '21.2', '.747', '11.9', '31.1', '43.0', '26.9', '6.9', '3.9', '15.5', '20.3', '112.3', '2', '62', '241.6', '.476', '11.6', '32.4', '.358', '31.7', '58.6', '.542', '18.7', '24.2', '.775', '11.7', '32.0', '43.6', '24.1', '7.7', '4.8', '13.1', '21.2', '117.0'], [1, '2', '26.8', '6.6', '215', '241.6', '42.3', '89.4', '.474', '14.0', '38.9', '.360', '28.3', '50.5', '.561', '18.9', '24.0', '.790', '11.9', '33.1', '45.0', '25.8', '6.4', '5.1', '15.4', '20.7', '117.6', '4', '61', '241.6', '.509', '12.5', '31.6', '.397', '33.4', '58.7', '.569', '18.4', '23.8', '.772', '10.7', '33.5', '44.2', '26.6', '8.3', '5.0', '13.9', '18.5', '122.9'], [0, '3', '25.4', '6.6', '218', '241.2', '42.8', '87.1', '.491', '12.0', '33.7', '.356', '30.8', '53.5', '.576', '17.9', '23.3', '.768', '9.0', '32.4', '41.4', '25.5', '8.1', '5.4', '15.7', '21.7', '115.5'], [], [], []]"""

"""for i in inputs:
	counter = 0
	for j in i:
		counter += 1
		i[counter-1] = float(j)"""
bias = 110
counter = 0
for i in inputs:
	counter += 1
	try:
		print(teamList[counter-1])
		print(relu(np.dot(i, weights) + bias))
	except:
		print("e")

"""print(relu(np.dot(inputs[0], weights) + bias))"""
