import numpy as np

table = []

with open("code.txt") as code:
        for line in code:
            table.append([int(a) for a in line.strip().split()])

first, second = {}, {}

for i in np.array(table)[:,0]:
    if i in first:
        first[i] += 1
    else:
        first[i] = 1

for i in np.array(table)[:,1]:
    if i in second:
        second[i] += 1
    else:
        second[i] = 1

total = 0

for i in first.keys():
    if i in second.keys():
        total += i * first[i] * second[i]

print(total)