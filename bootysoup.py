"""for i in headers:
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
	print(team1,team2)for i in headers:


"""
print(len([0, '2', '29.4', '6.6', '219', '241.2', '40.3', '85.8', '.469', '12.7', '33.5', '.378', '27.6', '52.3', '.528', '18.3', '23.5', '.777', '9.9', '33.6', '43.5', '22.9', '6.8', '4.6', '14.0', '19.5', '111.4', '3', '60', '241.7', '.467', '11.4', '31.7', '.359', '28.7', '54.0', '.531', '19.8', '25.1', '.791', '10.4', '32.6', '42.9', '23.6', '7.5', '4.0', '15.0', '20.3', '111.3', 32, 34.2, 2.7702, 6.0192000000000005, 0.15766200000000002, 1.026, 2.6334000000000004, 0.130644, 1.7442, 3.3516000000000004, 0.17852400000000002, 0.18639000000000003, 1.4022, 1.6074000000000002, 0.298908, 0.2394, 1.8468000000000002, 2.0862, 1.8126, 0.513, 0.10260000000000001, 1.1286, 0.9234000000000001, 7.968600000000001, 31, 32.4, 2.6244, 5.2488, 0.161028, 0.5508, 1.4256000000000002, 0.12312000000000001, 2.0736000000000003, 3.8232000000000004, 0.17528400000000002, 0.177876, 1.3932, 1.62, 0.28188, 0.3888, 1.62, 2.0088, 1.296, 0.4536, 0.162, 0.486, 0.4536, 7.160400000000001, 25, 29.4, 1.176, 1.9109999999999998, 0.18139799999999998, 0.0, 0.0, 0.0, 1.176, 1.9109999999999998, 0.18228, 0.18139799999999998, 0.6468, 0.9114, 0.20550599999999997, 0.9701999999999998, 1.9991999999999999, 2.9694, 0.3234, 0.1176, 0.3822, 0.49979999999999997, 0.8525999999999999, 2.9987999999999997, 33, 28.7, 1.3201999999999998, 3.0708999999999995, 0.12340999999999999, 0.574, 1.4924, 0.10905999999999999, 0.7462, 1.5784999999999998, 0.13718599999999997, 0.149814, 0.3444, 0.4305, 0.22386, 0.1435, 1.0905999999999998, 1.2054, 0.5166, 0.1722, 0.1148, 0.2296, 0.6314, 3.5301, 29, 25.8, 1.4706000000000001, 3.0185999999999997, 0.125388, 0.516, 1.2384, 0.107586, 0.9546000000000001, 1.7544, 0.13803, 0.147834, 0.9288000000000001, 1.161, 0.20769, 0.10320000000000001, 0.6966000000000001, 0.7998000000000001, 0.46440000000000003, 0.20640000000000003, 0.0774, 0.41280000000000006, 0.516, 4.386, 32, 25.7, 1.0536999999999999, 2.5186, 0.107426, 0.3855, 1.0794000000000001, 0.08995, 0.6682, 1.4392, 0.120533, 0.126701, 0.3084, 0.3341, 0.237468, 0.1028, 0.4626, 0.5654, 0.8995, 0.1799, 0.0257, 0.4626, 0.4626, 2.8013000000000003, 34, 24.0, 0.6, 1.7999999999999998, 0.07992, 0.36, 0.96, 0.09, 0.24, 0.84, 0.06863999999999999, 0.10392, 0.84, 0.96, 0.21, 0.0, 0.48, 0.48, 1.2, 0.24, 0.24, 0.0, 0.12, 2.4, 26, 23.5, 0.846, 1.5979999999999999, 0.122905, 0.235, 0.5874999999999999, 0.09212, 0.611, 1.0105, 0.14053, 0.13982499999999998, 0.2585, 0.3525, 0.18165499999999998, 0.235, 0.6579999999999999, 0.8929999999999999, 0.517, 0.1175, 0.0705, 0.235, 0.423, 2.162, 32, 22.2, 0.9101999999999999, 2.1978, 0.09057599999999999, 0.222, 0.7104, 0.06726599999999999, 0.6882, 1.4874, 0.101898, 0.101454, 0.5105999999999999, 0.7325999999999999, 0.151182, 0.0888, 0.5105999999999999, 0.5994, 1.1544, 0.1776, 0.0888, 0.5327999999999999, 0.3774, 2.5308, 34, 21.7, 0.434, 1.0633000000000001, 0.08853599999999999, 0.3255, 0.8462999999999999, 0.082026, 0.1085, 0.1953, 0.116746, 0.12173700000000001, 0.1085, 0.15189999999999998, 0.14300300000000002, 0.1953, 0.7161, 0.9114, 0.3255, 0.13019999999999998, 0.15189999999999998, 0.15189999999999998, 0.4557, 1.2803]))