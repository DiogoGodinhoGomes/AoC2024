import numpy  as np

a, total, valid = [], 0, ['SSMM', 'MSSM', 'MMSS', 'SMMS']

with open("code.txt") as file:
    for line in file:
        a.append([c for c in line.strip()])

a = np.array(a)

for r in range(1, len(a) - 1):
    for c in range(1, len(a[r]) - 1):
        if a[r][c] == 'A':
            f = ''.join([a[r-1][c-1], a[r-1][c+1], a[r+1][c+1], a[r+1][c-1]])
            
            if f in valid:
                total += 1

print(total)