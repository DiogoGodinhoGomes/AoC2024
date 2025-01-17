def getInfo(filename):
    values, rules, inver, series = set(), {}, {}, []

    with open(filename) as file:
        for line in file:
            if "|" in line:
                temp = line.strip().split("|")
                
                assert len(temp) == 2
                
                for val in temp:
                    values.add(val)
                
                if temp[0] not in rules.keys():
                    rules[temp[0]] = [temp[1]]
                else:
                    rules[temp[0]].append(temp[1])
                
                if temp[1] not in inver.keys():
                    inver[temp[1]] = [temp[0]]
                else:
                    inver[temp[1]].append(temp[0])
                
            elif "," in line:
                series.append(line.strip().split(","))
    
    return list(values), rules, inver, series

def getCorrectTotal(rules, series):
    total, incorrect = 0, []
    
    for serie in series:
        i, check = 0, True
        
        while i < len(serie) and check:
            j, k = i + 1, i - 1
            
            while j < len(serie) and check:
                if serie[i] in rules.keys() and serie[j] not in rules[serie[i]]:
                    check = False
                
                j += 1
            
            while k >= 0 and check:
                if serie[i] in rules.keys() and serie[k] in rules[serie[i]]:
                    check = False
                
                k -= 1
            
            i += 1
        
        if check:
            assert len(serie) % 2 == 1
            
            total += int(serie[int((len(serie) - 1) / 2)])
            
        else:
            incorrect.append(serie)

    return total, incorrect

def getSerieSorted(values, rules):
    for rule in rules.keys():
        for val in rules[rule]:
            if val in values and rule in values:
                irule, ival = values.index(rule), values.index(val)
                
                if irule > ival:
                    values = values[:ival] + [values[irule]] + values[ival:irule] + values[irule+1:]
    
    return values