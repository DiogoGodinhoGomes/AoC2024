import numpy as np

table = []

with open("code.txt") as code:
        for line in code:
            table.append([int(a) for a in line.strip().split()])

first, second = np.sort(np.array(table)[:,0]), np.sort(np.array(table)[:,1])

print(sum(np.abs(first - second)))