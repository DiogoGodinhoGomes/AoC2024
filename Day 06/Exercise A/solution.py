index, floor, start, unique = 0, [], None, set()

idir, dirs = 0, [[-1, 0], [0, 1], [1, 0], [0, -1]]

with open("code.txt") as file:
    for line in file:
        floor.append([c for c in line.strip()])
        
        try:            
            start = (index, floor[-1].index("^"))
            
            floor[-1][start[1]] = 'X'
        except:
            True
        
        index += 1

inmap, current = True, start

while inmap:
    unique.add(current)
    
    n = (current[0] + dirs[idir][0], current[1] + dirs[idir][1])
    
    if n[0] < 0 or n[1] < 0 or n[0] >= len(floor) or n[1] >= len(floor[n[0]]):
        inmap = False
        
        break
    elif floor[n[0]][n[1]] == '#':
        idir = (idir + 1) % len(dirs)
    else:
        current = n
        
        floor[n[0]][n[1]] = 'X'

print(len(unique))