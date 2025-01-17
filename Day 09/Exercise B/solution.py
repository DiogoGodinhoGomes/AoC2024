import numpy as np

orig, temp, index = [], [], 0

with open("code.txt") as file:
    for line in file:
        orig = [int(c) for c in line.strip()]

for i in range(len(orig)):
    if i % 2 == 0:
        if orig[i] > 0:
            temp.append([index, orig[i]])
        
        index += 1
    else:
        if orig[i] > 0:
            temp.append([-1, orig[i]])

index, temp = temp[-1][0], np.array(temp)

while index > 0:
    num = list(np.where(temp[:,0] == index)[0])[0]
    
    value, length = temp[num][0], temp[num][1]
    
    if value >= 0:
        pos = list(np.where((temp[:,0] == -1) & (temp[:,1] >= length))[0])
        
        if len(pos) > 0:
            place = pos[0]
            
            if place < num:
                space = temp[place][1]
                
                temp[place] = [value, length]
                
                temp[num] = [-1, length]
                
                if  space > length:
                    temp = np.insert(temp, place + 1, [-1, space - length], axis = 0)
    
    index -= 1

index, total = 0, 0

for elem in temp:
    for j in range(elem[1]):
        if elem[0] > 0:
            total += elem[0] * index
        
        index += 1

print(total)