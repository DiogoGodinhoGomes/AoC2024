import copy as cp

def getMapa(filename):
    mapa = []
    
    with open(filename) as file:
        for line in file:
            mapa.append([c for c in line.strip()])
            
    return mapa

def getPlots(mapa, dirs):
    plots, gone = [], []
    
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

    return plots

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

def getNewPlots(mapa, source, dirs):
    nmapa, index, minr, minc, maxr, maxc = [], 0, len(mapa), len(mapa[0]), 0, 0
    
    for e in source[3]:
        minr, minc, maxr, maxc = min(minr, e[0]), min(minc, e[1]), max(maxr, e[0]), max(maxc, e[1])
    
    for j in range(maxr - minr + 3):
        nmapa.append(["."] * (maxc - minc + 3))
    
    for e in source[3]:
        nmapa[e[0] - minr + 1][e[1] - minc + 1] = source[0]
    
    nplots = getPlots(nmapa, dirs)[1:]
    
    for k in range(1, len(nplots)):
        nplots[k][0] = str(index)
        
        for e in nplots[k][3]:
            nmapa[e[0]][e[1]] = str(index)
        
        index += 1
    
    return nmapa, nplots

def getNewMeasures(mapa, plots, dirs):
    for i in range(len(plots)):
        plots[i][1] = len(plots[i][3])
        
        nmapa, nplots = getNewPlots(mapa, plots[i], dirs)
        
        sides = 0
        
        for e in nplots:
            r, seq, nseq, start = 0, [], [], [-1, -1, 1]
            
            while r < len(nmapa) and (start[0] < 0 or start[1] < 0):
                if e[0] in nmapa[r]:
                    start = [r, nmapa[r].index(e[0]), 1]
                
                r += 1
            
            assert start[0] >= 0 and start[1] >= 0  and len(start) == 3
            
            seq.append(start)
            
            while len(seq) == 1 or seq[-1] != seq[0]:
                c = cp.deepcopy(seq[-1])
                
                if c[-1] == 0:
                    m, n = [c[0] - 1, c[1] - 1], [c[0] - 1, c[1]]
                elif c[-1] == 1:
                    m, n = [c[0] - 1, c[1] + 1], [c[0], c[1] + 1]
                elif c[-1] == 2:
                    m, n = [c[0] + 1, c[1] + 1], [c[0] + 1, c[1]]
                elif c[-1] == 3:
                    m, n = [c[0] + 1, c[1] - 1], [c[0], c[1] - 1]
                else:
                    assert False
                
                if nmapa[m[0]][m[1]] == e[0]:
                    seq.append([m[0], m[1], (c[-1] - 1) % len(dirs)])
                elif nmapa[m[0]][m[1]] != e[0] and nmapa[n[0]][n[1]] == e[0]:
                    seq.append([n[0], n[1], c[-1]])
                else:
                    seq.append([c[0], c[1], (c[-1] + 1) % len(dirs)])
            
            seq.pop(-1)
            
            for w in seq:
                if len(nseq) == 0 or w[2] != nseq[-1]:
                    nseq.append(w[2])
            
            if nseq[0] == nseq[-1]:
                nseq.pop(-1)
            
            sides += len(nseq)
        
        plots[i][2] = sides
        
        '''
        for z in nmapa:
            print(z)
        
        print("Type:", plots[i][0])
        print("Area:", plots[i][1])
        print("Side:", plots[i][2])
        print("Cost:", plots[i][1] * plots[i][2])
        print()
        '''
    
    return plots

def getTotal(plots):
    total = 0

    for p in plots:
        total += p[1] * p[2]

    return total