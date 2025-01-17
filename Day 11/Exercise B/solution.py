blinks, total, oldd, newd = 75, 0, {}, {}

with open("code.txt") as file:
    for line in file:
        seq = [int(c) for c in line.strip().split()]

for i in seq:
    if i not in oldd.keys():
        oldd[i] = 0
    
    oldd[i] += 1

for i in oldd.keys():
    total += oldd[i]

print(0, total)

for n in range(blinks):
    i, total, lst = 0, 0, list(oldd.keys())
    
    while i < len(lst):
        l = len(str(lst[i]))
        
        if lst[i] == 0:
            if lst[i] + 1 not in newd.keys():
                newd[lst[i] + 1] = 0
            
            newd[lst[i] + 1] += oldd[lst[i]]
            
        elif l % 2 == 0:
            if int(str(lst[i])[int(l / 2):]) not in newd.keys():
                newd[int(str(lst[i])[int(l / 2):])] = 0
            
            newd[int(str(lst[i])[int(l / 2):])] += oldd[lst[i]]
            
            if int(str(lst[i])[:int(l / 2)]) not in newd.keys():
                newd[int(str(lst[i])[:int(l / 2)])] = 0
            
            newd[int(str(lst[i])[:int(l / 2)])] += oldd[lst[i]]
        else:
            if lst[i] * 2024 not in newd.keys():
                newd[lst[i] * 2024] = 0
            
            newd[lst[i] * 2024] += oldd[lst[i]]
        
        i += 1
    
    oldd = newd
    
    newd = {}
    
    for i in oldd.keys():
        total += oldd[i]
    
    print(n + 1, total)