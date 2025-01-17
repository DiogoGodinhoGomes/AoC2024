import numpy as np

table, total = [], 0

with open("code.txt") as code:
        for line in code:
            table.append([int(a) for a in line.strip().split()])

for elem in table:
    analysis = np.array(elem)[1:] - np.array(elem)[:-1]
    
    if analysis[0] < 0:
        analysis *= -1
    
    if False not in (analysis > 0) * (analysis < 4):
        total += 1
    else:
        check = False
        
        for i in range(len(elem)):
            temp = elem[:i] + elem[i + 1:]
            
            analysis = np.array(temp)[1:] - np.array(temp)[:-1]
            
            if analysis[0] < 0:
                analysis *= -1
            
            if False not in (analysis > 0) * (analysis < 4):
                check = True
                
                break
        
        if check:
            total += 1

print(total)