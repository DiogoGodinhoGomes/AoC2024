import copy as cp
import numpy as np

def read(filename):
    i, start, end, mapa = 0, [-1, -1], [-1, -1], []

    dirs = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}

    with open(filename) as file:
        for line in file:
            mapa.append([c for c in line.strip()])
            
            if "S" in mapa[-1]:
                start = [i, mapa[-1].index("S")]
            
            if "E" in mapa[-1]:
                end = [i, mapa[-1].index("E")]
            
            i += 1

    assert start[0] >= 0 and start[1] >= 0 and end[0] >= 0 and end[1] >= 0

    return mapa, start, end, dirs

def find(mapa, start, end, dirs):
    find, poss, paths = True, [[True, cp.deepcopy(start)]], []

    while find:
        find = False
        
        for i in range(len(poss)):
            if poss[i][-1] == end:
                poss[i][0] = False
            else:
                temp = []
                
                for key in dirs.keys():
                    pos = np.array(poss[i][-1]) + np.array(dirs[key])
                    
                    if mapa[pos[0]][pos[1]] != "#" and list(pos) not in poss[i]:
                        temp.append(list(pos))
                
                if len(temp) > 0:
                    for j in range(len(temp)):
                        if j == len(temp) - 1:
                            poss[i].append(temp[j])
                        else:
                            poss.append(cp.deepcopy(poss[i]))
                            
                            poss[-1].append(temp[j])
                else:
                    poss[i][0] = False
            
            if poss[i][0]:
                find = True
        
        for e in poss[::-1]:
            if e[0] == False and e[-1] != end:
                poss.remove(e)
        
        print(len(poss))
    
    for path in poss:
        if path[-1] == end:
            paths.append(path[1:])
    
    return paths

def score(paths):
    scores = []

    for path in paths:
        score = len(path) - 1
        
        path.insert(0, [13, 0])
        
        temp = np.array(path)[1:] - np.array(path)[:-1]
        
        for i in range(len(temp) - 1):
            if list(temp[i + 1]) != list(temp[i]):
                score += 1000
        
        scores.append(score)

    return min(scores)

def result(mapa, start, end, dirs):
    cntn, used, unused, mdrs, mscr = True, set(), set(), [], []

    unused.add((start[0], start[1]))

    for i, r in enumerate(mapa):
        mdrs.append(["."] * len(r))
        mscr.append([0] * len(r))
        
        for j, e in enumerate(r):
            if e == "#":
                mdrs[i][j], mscr[i][j] = "#", -1

    mdrs[start[0]][start[1]] = "E"

    while cntn and len(unused) > 0:    
        mnm, cur = -1, [-1, -1]
        
        for e in unused:
            if (mscr[e[0]][e[1]] <= mnm or mnm < 0) and e not in used:
                mnm = mscr[e[0]][e[1]]
                
                cur = [e[0], e[1]]
        
        for d in dirs.keys():
            tmp = [cur[0] + dirs[d][0], cur[1] + dirs[d][1]]
            
            if mapa[tmp[0]][tmp[1]] != "#" and (tmp[0], tmp[1]) not in used:
                mdrs[tmp[0]][tmp[1]] = d
                
                mscr[tmp[0]][tmp[1]] = mscr[cur[0]][cur[1]] + 1
                
                if mdrs[cur[0]][cur[1]] != d:
                    mscr[tmp[0]][tmp[1]] += 1000
                
                unused.add((tmp[0], tmp[1]))
        
        unused.remove((cur[0], cur[1]))
        
        used.add((cur[0], cur[1]))
        
        if (end[0], end[1]) in unused:
            cntn = False

    return mscr[end[0]][end[1]]