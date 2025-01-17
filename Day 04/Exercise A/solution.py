import numpy  as np

sone, stwo, a, total = 'XMAS', 'SAMX', [], 0

with open("code.txt") as file:
    for line in file:
        a.append([c for c in line.strip()])

a = np.array(a)

for r in range(len(a)):
    for c in range(len(a[r])):
        # Check horizontal:
        if c + 3 < len(a[r]):
            temp = a[r][c] + a[r][c+1] + a[r][c+2] + a[r][c+3]
            
            if temp == sone or temp == stwo:
                total += 1
        
        # Check negative diagonal:
        if c + 3 < len(a[r]) and  r + 3 < len(a):
            temp = a[r][c] + a[r+1][c+1] + a[r+2][c+2] + a[r+3][c+3]
            
            if temp == sone or temp == stwo:
                total += 1
        
        # Check vertical:
        if r + 3 < len(a):
            temp = a[r][c] + a[r+1][c] + a[r+2][c] + a[r+3][c]
            
            if temp == sone or temp == stwo:
                total += 1
        
        # Check positive diagonal:
        if  c - 3 >= 0 and  r + 3 < len(a):
            temp = a[r+3][c-3] + a[r+2][c-2] + a[r+1][c-1] + a[r][c]
            
            if temp == sone or temp == stwo:
                total += 1

print(total)