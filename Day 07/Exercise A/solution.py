import numpy as np
import itertools as it

total, lines = 0, []

with open("code.txt") as file:
    for line in file:
        lines.append([int(c) for c in line.replace(":", " ").strip().split()])

for l in lines:
    pos = list(it.product([0, 1], repeat = len(l) - 2))
    
    totals = np.ones(len(pos)) * l[1]
    
    for i in range(len(totals)):
        for j in range(len(pos[i])):
            if pos[i][j] == 0:
                totals[i] += l[j + 2]
            elif pos[i][j] == 1:
                totals[i] *= l[j + 2]
        
    if sum(totals == l[0]) > 0:
        total += l[0]

print(total)