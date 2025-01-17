total, active = 0, 1

with open("code.txt") as file:
    for line in file:
        for i in range(len(line) - 6):            
            if line[i : i + 4] == 'do()':
                active = 1
            elif line[i : i + 7] == 'don\'t()':
                active = 0
            elif line[i : i + 4] == 'mul(':
                close = line[i : i + 12].find(')')
                
                comma = line[i : i + 12].find(',')
                
                if close >= 0 and comma >= 0:
                    temp = line[i + 4 : i + close].strip().split(',')
                    
                    assert len(temp) == 2
                    
                    total += int(temp[0]) * int(temp[1]) * active

print(total)