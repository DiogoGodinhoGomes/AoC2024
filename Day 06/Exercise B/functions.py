def getFloor(filename):
    index, floor = 0, []
    
    with open(filename) as file:
        for line in file:
            floor.append([c for c in line.strip()])
            
            try:            
                n = (index, floor[-1].index("^"), 0)
                
                floor[-1][n[1]] = 'X'
            except:
                True
            
            index += 1
    
    return floor, n


def getPath(floor, n, dirs):
    inmap, inloop, path, idir = True, False, [n], 0

    while inmap and not inloop:    
        n = (path[-1][0] + dirs[idir][0], path[-1][1] + dirs[idir][1], idir)
        
        if n[0] < 0 or n[1] < 0 or n[0] >= len(floor) or n[1] >= len(floor[n[0]]):
            inmap = False
            
            break
        elif floor[n[0]][n[1]] == '#':
            idir = (idir + 1) % len(dirs)
            
            path.append((path[-1][0], path[-1][1], idir))
        else:        
            floor[n[0]][n[1]] = 'X'
            
            if n not in path:
                path.append(n)
            else:
                inloop = True
    
    return path, inmap, inloop