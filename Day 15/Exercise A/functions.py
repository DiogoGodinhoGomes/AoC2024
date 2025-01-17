import copy as cp

def read(filename):
    start, mapa, inst = [-1, -1], [], ""
    
    with open(filename) as file:
        i = 0
        
        for line in file:
            temp = line.strip()
            
            if len(temp) > 0:
                if "@" in temp:
                    start = [i, temp.find("@")]
                
                if temp[0] == "#":
                    mapa.append([c for c in temp])
                else:
                    inst += temp
            
            i += 1
    
    assert start[0] > 0 and start [1] > 0
    
    for r in mapa:
        for c in r:
            assert c in ["#", ".", "O", "@"]
    
    for c in inst:
        assert c in ["^", ">", "v", "<"]
    
    dtnr = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    
    return start, mapa, inst, dtnr

def move(start, mapa, inst, dtnr):
    for c in inst:
        i, pos, seq = 0, cp.deepcopy(start), []
        
        while mapa[pos[0]][pos[1]] in ["@", "O"]:
            i += 1
            
            pos[0] += dtnr[c][0]
            pos[1] += dtnr[c][1]
            
            seq.append(mapa[pos[0]][pos[1]])
        
        if "#" not in seq:
            mapa[start[0]][start[1]] = "."
            
            start[0] += dtnr[c][0]
            start[1] += dtnr[c][1]
            
            mapa[start[0]][start[1]] = "@"
            
            if "O" in seq:
                mapa[pos[0]][pos[1]] = "O"
    
    return mapa

def total(mapa):
    total = 0

    for i, r in enumerate(mapa):
        for j, c in enumerate(r):
            if c == "O":
                total += 100 * i + j
    
    return total