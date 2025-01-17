import numpy as np
import itertools as it

index, total, lines = 0, 0, []

with open("code.txt") as file:
    for line in file:
        lines.append([int(c) for c in line.replace(":", " ").strip().split()])

for l in lines:
    pos = list(it.product([0, 1, 2], repeat = len(l) - 2))
    
    totals = np.ones(len(pos)) * l[1]
    
    for i in range(len(totals)):
        for j in range(len(pos[i])):
            if pos[i][j] == 0:
                totals[i] += l[j + 2]
            elif pos[i][j] == 1:
                totals[i] *= l[j + 2]
            elif pos[i][j] == 2:
                totals[i] = int(str(int(totals[i])) + str(int(l[j + 2])))
        
        if totals[i] == l[0]:
            total += l[0]
            
            break
    
    index += 1
    
    print(index, "of", len(lines))

print(total)