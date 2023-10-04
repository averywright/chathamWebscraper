import itertools
repeater =5
g = (["".join(seq) for seq in itertools.product("01", repeat=repeater)])
count = 0
for i in g:
    printer = True
    counter = 0

    for j in i:

        counter += 1
        if counter < repeater-1:
            if j == '1' and i[counter] == '1' and i[counter+1] == '1':
                printer = False

                break
    if printer:
        count += 1
        print(i)

print(count)
