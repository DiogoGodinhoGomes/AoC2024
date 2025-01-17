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

def find(mapa, start, end, dirs, mxm):
    find, poss, paths = True, [[True, "E", 0, cp.deepcopy(start)]], []

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
                            
                            poss[i][2] += 1
                            
                            key = list(np.array(poss[i][-1]) - np.array(poss[i][-2]))
                            
                            key = list(dirs.keys())[list(dirs.values()).index((key[0], key[1]))]
                            
                            if key != poss[i][1]:
                                poss[i][2] += 1000
                            
                            poss[i][1] = cp.deepcopy(key)
                        
                        else:
                            poss.append(cp.deepcopy(poss[i]))
                            
                            poss[-1].append(temp[j])
                            
                            poss[-1][2] += 1
                            
                            key = list(np.array(poss[-1][-1]) - np.array(poss[-1][-2]))
                            
                            key = list(dirs.keys())[list(dirs.values()).index((key[0], key[1]))]
                            
                            if key != poss[-1][1]:
                                poss[-1][2] += 1000
                            
                            poss[-1][1] = cp.deepcopy(key)
                
                else:
                    poss[i][0] = False
            
            if poss[i][0]:
                find = True
        
        for e in poss[::-1]:
            if (e[0] == False and e[-1] != end) or e[2] > mxm:
                poss.remove(e)
    
    for path in poss:
        if path[-1] == end:
            paths.append(path)
    
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
    cntn, unused, mdrs, mscr = True, set(), [], []

    unused.add((start[0], start[1]))

    for i, r in enumerate(mapa):
        mdrs.append(["."] * len(r))
        mscr.append([-10] * len(r))
        
        for j, e in enumerate(r):
            if e == "#":
                mdrs[i][j] = "#"

    mdrs[start[0]][start[1]], mscr[start[0]][start[1]] = "E", 0

    while cntn and len(unused) > 0:
        mnm, cur = -1, [-1, -1]
        
        for e in unused:
            if (mscr[e[0]][e[1]] <= mnm or mnm < 0):
                mnm = mscr[e[0]][e[1]]
                
                cur = [e[0], e[1]]
        
        for d in dirs.keys():
            inc, tmp = 1, [cur[0] + dirs[d][0], cur[1] + dirs[d][1]]
            
            if mapa[tmp[0]][tmp[1]] != "#":
                if mdrs[cur[0]][cur[1]] != d:
                    inc += 1000
                
                if mscr[tmp[0]][tmp[1]] < 0 or mscr[cur[0]][cur[1]] + inc < mscr[tmp[0]][tmp[1]]:
                    mdrs[tmp[0]][tmp[1]], mscr[tmp[0]][tmp[1]] = d, mscr[cur[0]][cur[1]] + inc
                    
                    unused.add((tmp[0], tmp[1]))
        
        unused.remove((cur[0], cur[1]))
        
        if (end[0], end[1]) in unused:
            cntn = False

    return mscr[end[0]][end[1]], mdrs, mscr

def tiles(dirs, mscr, start, end, mxm):
    for i in range(len(mscr)):
        for j in range(len(mscr[i])):
            if mscr[i][j] > mxm:
                mscr[i][j] = -10
            elif mscr[i][j] > 0:
                mscr[i][j] %= 1000
    
    cntn, paths = True, [[(end[0], end[1])]]
    
    while cntn:
        i, up, cntn = 0, len(paths), False
        
        while i < up:
            j, opt, cur = 0, [], paths[i][-1]
            
            for d in dirs.keys():
                tmp = (cur[0] + dirs[d][0], cur[1] + dirs[d][1])
                
                if mscr[tmp[0]][tmp[1]] >= 0 and mscr[tmp[0]][tmp[1]] < mscr[cur[0]][cur[1]]:
                    opt.append(tmp)
            
            while j < len(opt):
                if j == len(opt) - 1:
                    paths[i].append(opt[j])
                else:
                    paths.append(cp.deepcopy(paths[i]))
                    
                    paths[-1].append(opt[j])
                
                j += 1
            
            i += 1
        
        for p in paths:
            if p[-1] != (start[0], start[1]):
                cntn = True
    
    p = len(paths) - 1
    
    while p >= 0:
        total = len(paths[p]) - 1
        
        paths[p].append((start[0], start[1] - 1))
        
        i, d = 2, [paths[p][1][0] - paths[p][0][0], paths[p][1][1] - paths[p][0][1]]
        
        while i < len(paths[p]):
            n = [paths[p][i][0] - paths[p][i - 1][0], paths[p][i][1] - paths[p][i - 1][1]]
            
            if n[0] != d[0] or n[1] != d[1]:
                d = cp.deepcopy(n)
                
                total += 1000
            
            i += 1
        
        if total != mxm:
            paths.remove(paths[p])
        
        p -= 1
    
    tiles = set()
    
    for p in paths:
        p.pop()
        
        for e in p:
            tiles.add(e)
    
    return tiles