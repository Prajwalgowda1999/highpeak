import sys

f = open("input.txt","r")
readText = f.read()
f.close()

lst = readText.split('\n')
costs = {}

for i in lst:
    if len(i.split(':')) == 2:
        if i.split(':')[0] == "Number of employees":
            num_emp = int(i.split(':')[1])
        elif i.split(':')[1] != '':
            costs[i.split(':')[0]] = int(i.split(':')[1])

costs = dict(sorted(costs.items(), key=lambda item: item[1]))

map_keys = {}
i = 1
for k, v in costs.items():
    map_keys[i] = k
    i += 1

#---------Selecting first num_emp from list with least cost diff------------
min_cst = float('inf')
min_i = -1
for i in range(1, len(costs) - num_emp):
    if min_cst > costs[map_keys[i+num_emp-1]] - costs[map_keys[i]]:
        min_cst = costs[map_keys[i+num_emp-1]] - costs[map_keys[i]]
        min_i = i
    
f = open("output.txt", "w")
f.write("The goodies selected for distribution are:\n")
for i in range(min_i, min_i+num_emp):
    f.write("\n" + map_keys[i]+ ": " + str(costs[map_keys[i]]))
f.write("\n")
x = "\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(min_cst)
f.write(x)
f.close()
