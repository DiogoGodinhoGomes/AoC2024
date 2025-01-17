import numpy as np
import itertools as it

mapa, ants, nodes, final = [], dict(), set(), []

with open("code.txt") as file:
    for line in file:
        mapa.append([c for c in line.strip()])

for row in range(len(mapa)):
    for col in range(len(mapa[row])):
        if mapa[row][col] != ".":
            if mapa[row][col] not in ants.keys():
                ants[mapa[row][col]] = [(row, col)]
            else:
                ants[mapa[row][col]].append((row, col))

for i in ants.keys():
    for j in list(it.combinations(ants[i], 2)):
        t, v = np.array(j[0]), np.array(j[1]) - np.array(j[0])
        
        while t[0] >= 0 and t[1] >= 0 and t[0] < len(mapa) and t[1] < len(mapa[t[0]]):
            nodes.add(tuple(t))
            
            t -= v
        
        t = np.array(j[0])
        
        while t[0] >= 0 and t[1] >= 0 and t[0] < len(mapa) and t[1] < len(mapa[t[0]]):
            nodes.add(tuple(t))
            
            t += v

print(len(nodes))