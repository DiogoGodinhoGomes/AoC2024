def read(filename):
    rgtr, pgrm, program = [0, 1, 2, 3, 4, 5, 6, 7], [], ""
    
    dtnr = {0: "adv", 1: "bxl", 2: "bst", 3: "jnz", 4: "bxc", 5: "out", 6: "bdv", 7: "cdv"}
    
    with open(filename) as file:
        for line in file:
            if len(line.strip()) > 0:
                if "A:" in line:
                    rgtr[4] = int(line.strip().split()[-1])
                elif "B:" in line:
                    rgtr[5] = int(line.strip().split()[-1])
                elif "C:" in line:
                    rgtr[6] = int(line.strip().split()[-1])
                else:
                    pgrm = [int(c) for c in line.strip().replace(",", " ").split()[1:]]
    
    for c in pgrm:
        program += str(c) + ","
    
    return rgtr, pgrm, dtnr, program[:-1]

def string(rgtr, pgrm):
    i, out, string = 0, [], ""

    while i < len(pgrm):
        instr, value = pgrm[i], pgrm[i + 1]
        
        i += 2
        
        match instr:
            case 0:
                assert value != len(rgtr) - 1
                
                rgtr[4] = int(rgtr[4] / pow(2, rgtr[value]))
            
            case 1:
                rgtr[5] = rgtr[5] ^ value
            
            case 2:
                assert value != len(rgtr) - 1
                
                rgtr[5] = rgtr[value] % len(rgtr)
            
            case 3:
                if rgtr[4] > 0:
                    i = value
            
            case 4:
                rgtr[5] = rgtr[5] ^ rgtr[6]
            
            case 5:
                assert value != len(rgtr) - 1
                
                out.append(rgtr[value] % len(rgtr))
            
            case 6:
                rgtr[5] = int(rgtr[4] / pow(2, rgtr[value]))
            
            case 7:
                rgtr[6] = int(rgtr[4] / pow(2, rgtr[value]))

    for e in out:
        string += str(e) + ","

    return string[:-1]