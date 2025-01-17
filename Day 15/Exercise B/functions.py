import copy as cp

def read(filename):
    start, mapa, inst = [-1, -1], [], ""
    
    with open(filename) as file:
        i = 0
        
        for line in file:
            if len(line.strip()) > 0:
                if line.strip()[0] == "#":
                    temp = ""
                    
                    for c in line.strip():
                        if c == "O":
                            temp += "[]"
                        elif c == "@":
                            temp += "@."
                        else:
                            temp += 2 * c
                    
                    if "@" in temp:
                        start = [i, temp.find("@")]
                    
                    mapa.append([c for c in temp])
                else:
                    inst += line.strip()
            
            i += 1
    
    assert start[0] > 0 and start [1] > 0
    
    for r in mapa:
        for c in r:
            assert c in ["#", ".", "[", "]", "@"]
    
    for c in inst:
        assert c in ["^", ">", "v", "<"]
    
    dtnr = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    
    return start, mapa, inst, dtnr

def move(start, mapa, inst, dtnr):
    for c in inst:
        i, pos, seq = 0, cp.deepcopy(start), []
        
        if c == ">" or c == "<":
            while mapa[pos[0]][pos[1]] in ["@", "[", "]"]:
                i += 1
                
                pos[1] += dtnr[c][1]
                
                seq.append(mapa[pos[0]][pos[1]])
            
            if "#" not in seq:
                mapa[start[0]][start[1]] = "."
                
                start[1] += dtnr[c][1]
                
                mapa[start[0]][start[1]] = "@"
                
                pos = cp.deepcopy(start)
                
                for e in seq[:-1]:
                    pos[1] += dtnr[c][1]
                    
                    mapa[pos[0]][pos[1]] = cp.deepcopy(e)
        
        else:
            can, check = True, True
            
            seq.append([pos])
            
            while check and can:
                temp, check = [], False
                
                for e in seq[-1]:
                    pos = cp.deepcopy(e)
                    
                    pos[0] += dtnr[c][0]
                    
                    if mapa[pos[0]][pos[1]] == "#":
                        can = False
                        
                    elif mapa[pos[0]][pos[1]] != ".":
                        check = True
                        
                        if cp.deepcopy(pos) not in temp:
                            temp.append(cp.deepcopy(pos))
                        
                        if mapa[pos[0]][pos[1]] == "[":
                            pos[1] += 1
                            
                            assert mapa[pos[0]][pos[1]] == "]"
                            
                        elif mapa[pos[0]][pos[1]] == "]":
                            pos[1] -= 1
                            
                            assert mapa[pos[0]][pos[1]] == "["
                        
                        if cp.deepcopy(pos) not in temp:
                            temp.append(cp.deepcopy(pos))
                
                if check and can:
                    seq.append(temp)
            
            if can:
                for e in seq[::-1]:
                    for p in e:
                        mapa[p[0] + dtnr[c][0]][p[1]] = cp.deepcopy(mapa[p[0]][p[1]])
                        
                        if mapa[p[0] + dtnr[c][0]][p[1]] == "@":
                            start[0] += dtnr[c][0]
                        
                        mapa[p[0]][p[1]] = "."
    
    return mapa

def total(mapa):
    total = 0
    
    for i, r in enumerate(mapa):
        for j, c in enumerate(r):
            if c == "[":
                total += 100 * i + j
    
    return total