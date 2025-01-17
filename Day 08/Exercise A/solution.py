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
        v = np.array(j[1]) - np.array(j[0])
        
        nodes.add(tuple(np.array(j[0]) - v))
        
        nodes.add(tuple(np.array(j[1]) + v))

for n in sorted(list(nodes)):
    if n[0] >= 0 and n[1] >= 0 and n[0] < len(mapa) and n[1] < len(mapa[0]):
        final.append(n)

print(len(final))