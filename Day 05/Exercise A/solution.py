total, rules, series = 0, {}, []

with open("code.txt") as file:
    for line in file:
        if "|" in line:
            temp = line.strip().split("|")
            
            assert len(temp) == 2
            
            if temp[0] not in rules.keys():
                rules[temp[0]] = [temp[1]]
            else:
                rules[temp[0]].append(temp[1])
        elif "," in line:
            series.append(line.strip().split(","))

for serie in series:
    i, correct = 0, True
    
    while i < len(serie) and correct:
        j, k = i + 1, i - 1
        
        while j < len(serie) and correct:
            if serie[i] in rules.keys() and serie[j] not in rules[serie[i]]:
                correct = False
            
            j += 1
        
        while k >= 0 and correct:
            if serie[i] in rules.keys() and serie[k] in rules[serie[i]]:
                correct = False
            
            k -= 1
        
        i += 1
    
    if correct:
        assert len(serie) % 2 == 1
        
        total += int(serie[int((len(serie) - 1) / 2)])

print(total)