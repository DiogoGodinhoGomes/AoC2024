import copy as cp

def getMapa(filename):
    mapa= []
    
    with open(filename) as file:
        for line in file:
            mapa.append([c for c in line.strip()])
    
    return mapa

def getInitialPoints(mapa):
    paths = []
    
    for row in range(len(mapa)):
        for col in range(len(mapa[row])):
            if mapa[row][col] == "0":
                paths.append([True, (row, col)])
    
    return paths

def getPaths(mapa, paths):
    processing, dirs = True, [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while processing:
        l = len(paths)
        
        for e in range(l):
            if paths[e][0]:
                i, fut = 0, []
                
                for pos in dirs:
                    c = (paths[e][-1][0] + pos[0], paths[e][-1][1] + pos[1])
                    
                    if c[0] >= 0 and c[1] >= 0 and c[0] < len(mapa) and c[1] < len(mapa[c[0]]):
                        if int(mapa[c[0]][c[1]]) == len(paths[e]) - 1:
                            fut.append(c)
                
                while i < len(fut):
                    if i < len(fut) - 1:
                        paths.append(cp.deepcopy(paths[e]))
                        
                        paths[-1].append(fut[i])
                    else:
                        paths[e].append(fut[i])
                    
                    i += 1
                
                if len(fut) == 0 or len(paths[e]) == 11:
                    paths[e][0] = False
        
        i, processing = 0, False
        
        while i < len(paths) and not processing:
            if paths[i][0]:
                processing = True
            
            i += 1
    
    return paths

def getScores(paths):
    scores = {}

    for elem in paths:
        if len(elem) == 11:
            if elem[1] not in scores.keys():
                scores[elem[1]] = set()
            
            scores[elem[1]].add(elem[-1])
    
    return scores

def getTotal(scores):
    total = 0
    
    for elem in scores.keys():
        total += len(scores[elem])
    
    return total