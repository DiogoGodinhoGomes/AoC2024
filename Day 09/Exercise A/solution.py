orig, temp, index = [], [], 0

# 91111740342 is too low!

with open("code.txt") as file:
    for line in file:
        orig = [int(c) for c in line.strip()]

for i in range(len(orig)):
    if i % 2 == 0:
        temp += [index] * orig[i]
        
        index += 1
    else:
        temp += ["."] * orig[i]

dots = [temp.index(".")]

while "." in temp[dots[-1] + 1:]:
    dots.append(temp[dots[-1] + 1:].index(".") + (dots[-1] + 1))

values, index = [], len(temp) - 1

while index >= 0:
    if temp[index] != ".":
        values.append(index)
    
    index -= 1

index, total, series = 0, 0, []

for i in range(len(values)):
    if i not in dots:
        total += i * int(temp[i])
        
        series.append(temp[i])
    else:
        total += i * int(temp[values[index]])
        
        series.append(temp[values[index]])
        
        index += 1
    
    print(round(i * 100.0 / len(values), 2), "%")

print("\nTotal:", total)