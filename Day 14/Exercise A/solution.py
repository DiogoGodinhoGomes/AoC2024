import numpy as np

# 104609262 is too low!

time, x, y, velo, posi, grid = 100, 101, 103, [], [], []

with open("code.txt") as file:
    for line in file:
        temp = [int(c) for c in line.strip().replace("p=","").replace("v=",",").split(",")]
        
        posi.append((temp[1], temp[0]))
        
        velo.append((temp[3], temp[2]))

for i in range(y):
    grid.append([0] * x)

for i in range(len(posi)):
    new_x, new_y = (posi[i][0] + time * velo[i][0]) % y, (posi[i][1] + time * velo[i][1]) % x
    
    grid[new_x][new_y] += 1

grid, hx, hy = np.array(grid), int((x - 1) / 2), int((y - 1) / 2)

on, tw, th, fr = np.sum(grid[:hy,:hx]), np.sum(grid[:hy,hx+1:]), np.sum(grid[hy+1:,hx+1:]), np.sum(grid[hy+1:,:hx])

print(on * tw * th * fr)