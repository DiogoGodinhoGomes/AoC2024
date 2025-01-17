def getPlots(filename, dirs):
    mapa, plots, gone = [], [], []
    
    with open(filename) as file:
        for line in file:
            mapa.append([c for c in line.strip()])

    for r in range(len(mapa)):
        for c in range(len(mapa[r])):
            if (r, c) not in gone:
                typ, unused, used = mapa[r][c], [(r, c)], []
                
                while len(unused) > 0:
                    cr, cc = unused[-1][0], unused[-1][1]
                    
                    unused.pop(-1)
                    
                    for d in dirs:
                        nr, nc = cr + d[0], cc + d[1]
                        
                        if nr >= 0 and nc >= 0 and nr < len(mapa) and nc < len(mapa[nr]):
                            if mapa[nr][nc] == typ and (nr, nc) not in unused and (nr, nc) not in used:
                                unused.append((nr, nc))
                    
                    used.append((cr, cc))
                
                gone += used
                
                plots.append([typ, 0, 0, used])

    assert len(gone) == len(mapa) * len(mapa[0])

    return mapa, plots

def getMeasures(mapa, plots, dirs):
    for i in range(len(plots)):
        dtnr, total = {}, 0
        
        plots[i][1] = len(plots[i][3])
        
        for e in plots[i][3]:
            n = 0
            
            for d in dirs:
                r, c = e[0] + d[0], e[1] + d[1]
                
                if r >= 0 and c >= 0 and r < len(mapa) and c < len(mapa[r]) and (r, c) in plots[i][3]:
                    n += 1
            
            if len(dirs) - n not in dtnr.keys():
                dtnr[len(dirs) - n] = 0
            
            dtnr[len(dirs) - n] += 1
        
        for k in dtnr.keys():
            total += k * dtnr[k]
        
        plots[i][2] = total
    
    return plots

def getTotal(plots):
    total = 0

    for p in plots:
        total += p[1] * p[2]

    return total