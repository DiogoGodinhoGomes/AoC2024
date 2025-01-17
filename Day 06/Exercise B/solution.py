import copy as cp
import functions as fc

# 1679 is too low!

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

floor, n = fc.getFloor("code.txt")

path, inmap, inloop = fc.getPath(floor, n, dirs)

assert (inmap == False and inloop == False)

spots = set()

for i in range(len(path)):
    n = (path[i][0] + dirs[path[i][2]][0], path[i][1] + dirs[path[i][2]][1])
    
    if n[0] >= 0 and n[1] >= 0 and n[0] < len(floor) and n[1] < len(floor[n[0]]) and floor[n[0]][n[1]] != '#' and n not in spots:
        nfloor = cp.deepcopy(floor)
        
        nfloor[n[0]][n[1]] = '#'
        
        npath, inmap, inloop = fc.getPath(nfloor, path[0], dirs)
        
        if inloop:
            spots.add(n)
    
    print(i, len(spots))