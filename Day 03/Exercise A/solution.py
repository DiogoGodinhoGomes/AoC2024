total = 0

with open("code.txt") as file:
    for line in file:
        for i in range(len(line) - 3):
            if line[i : i + 4] == 'mul(':
                close = line[i : i + 12].find(')')
                
                comma = line[i : i + 12].find(',')
                
                if close >= 0 and comma >= 0:
                    temp = line[i + 4 : i + close].strip().split(',')
                    
                    assert len(temp) == 2
                    
                    total += int(temp[0]) * int(temp[1])


print(total)