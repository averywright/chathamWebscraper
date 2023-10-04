import pandas as pd
import numpy as np

totality = []
df = pd.read_excel(r'/Users/averywright/PycharmProjects/pythonProject/Copy of Chatham_Baseball_Data.xlsx')
df = df.values
for i in range(0,3442):
    row = df[i, :]
    data_list = row.astype(str).tolist()
    totality.append(data_list)
# Print the resulting list

filtered_data = [arr for arr in totality if '-' not in arr]

"""print(filtered_data)"""

grouped_data = {}

for arr in totality:
    pitcher_name = arr[0]
    pitch_type = arr[4]
    key = (pitcher_name, pitch_type)

    if key not in grouped_data:
        grouped_data[key] = []

    grouped_data[key].append(arr)

print(grouped_data)


# Print the grouped data
for key, value in grouped_data.items():
    counter = 0
    for arr in value:
        print(arr)
        counter += 1
"""
final = {}
place = np.zeros(28)
for keys in grouped_data:
    count = 0
    for i in grouped_data[keys]:
        count += 1
        counter = 0
        for k in i:
            counter += 1
            try:
                place[counter-1] += float(k)
            except:
                pass
    counter = 0
    for i in place:
        counter += 1
        place[counter-1] = float(i / count)
    final[keys] = [place,count]

lastly = {}
for keys in final:
    lastly[keys[0]] = []

for i in lastly:
    for j in final:
        if j[0] == i:
            lastly[i].append(final[j])

reference = []
for i in lastly:
    counter = 0
    for k in (lastly[i]):
        counter += (k[1])
    reference.append(counter)

averaged = []
counter = 0
conclude = {}
for i in lastly:
    conclude[i] = np.zeros(28)
    counter += 1
    for k in lastly[i]:
        conclude[i] += k[0] * k[1]/reference[counter-1]


count = 0
for i in conclude:
    count += 1
    counter = 0
    for j in conclude[i]:
        counter += 1

        conclude[i][counter-1] = format(j, 'f')

print(conclude)"""