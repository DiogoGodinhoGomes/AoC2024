i, total, corr, machines = 0, 0, 1 * 10000000000000, []

with open("code.txt") as file:
    for line in file:
        new = line.replace(":"," ").replace(","," ").replace("+"," ").replace("-"," ").replace("="," ").strip().split()
        
        if len(new) > 0:
            if i % 3 == 0:
                assert new[0] == "Button" and new[1] == "A" and new[2] == "X" and new[4] == "Y"
                
                machine = [int(new[3]), 0, 0, int(new[5]), 0, 0]
            elif i % 3 == 1:
                assert new[0] == "Button" and new[1] == "B" and new[2] == "X" and new[4] == "Y"
                
                machine[1], machine[4] = int(new[3]), int(new[5])
            elif i % 3 == 2:
                assert new[0] == "Prize" and new[1] == "X" and new[3] == "Y"
                
                machine[2], machine[5] = int(new[2]) + corr, int(new[4]) + corr
                
                machines.append(machine)
            
            i += 1

for m in machines:
    if m[3] / m[0] != m[4] / m[1]:
        x, y = None, (m[3] * m[2] - m[5] * m[0])/(m[3] * m[1] - m[4] * m[0])
        
        if round(y, 10) == round(y, 0):
            x = (1.0 / m[0]) * (m[2] - m[1] * y)
            
            if round(x, 10) == round(x, 0):
                total += 3 * x + y
    
    elif m[3] / m[0] == m[5] / m[2]:
        print("Multiple solutions! -->", m)
    else:
        print("No solutions! -->", m)

assert round(total, 10) == round(total, 0)

print(int(total))