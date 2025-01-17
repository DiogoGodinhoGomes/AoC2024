import numpy as np
from PIL import Image as Im
import matplotlib.pyplot as plt

num, x, y, velo, posi, rslt, vrcs = 11000, 103, 101, [], [], [], []

with open("code.txt") as file:
    for line in file:
        temp = [int(c) for c in line.strip().replace("p=","").replace("v=",",").split(",")]
        
        posi.append((temp[1], temp[0]))
        
        velo.append((temp[3], temp[2]))

for time in range(num + 1):
    grid, image = np.zeros((x, y), dtype = np.uint8), np.zeros((x, y, 3), dtype = np.uint8)
    
    for i in range(len(posi)):
        new_x, new_y = (posi[i][0] + time * velo[i][0]) % x, (posi[i][1] + time * velo[i][1]) % y
        
        if grid[new_x][new_y] == 0:
            grid[new_x][new_y] += 1
            
            image[new_x][new_y] = [255, 255, 255]
    
    grid, hx, hy = np.array(grid), int((x - 1) / 2), int((y - 1) / 2)

    on, tw, th, fr = np.sum(grid[:hy,:hx]), np.sum(grid[:hy,hx+1:]), np.sum(grid[hy+1:,hx+1:]), np.sum(grid[hy+1:,:hx])
    
    rslt.append(on * tw * th * fr)
    
    vrcs.append(np.var(grid))
    
    if on * tw * th * fr < 140000000:
        im = Im.fromarray(image, "RGB")
        
        im.save(str(time) + ".png")

plt.scatter(range(num + 1), rslt)

plt.show()