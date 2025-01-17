import numpy as np

blinks = 25

with open("code.txt") as file:
    for line in file:
        seq = np.array([int(c) for c in line.strip().split()])

print(0, len(seq))

for n in range(blinks):
    i = 0
    
    while i < len(seq):
        l = len(str(seq[i]))
        
        if seq[i] == 0:
            seq[i] += 1
        elif l % 2 == 0:        
            seq = np.insert(seq, i + 1, int(str(seq[i])[int(l / 2):]))
            
            seq[i] = int(str(seq[i])[:int(l / 2)])
            
            i += 1
        else:
            seq[i] *= 2024
        
        i += 1
    
    print(n + 1, len(seq))