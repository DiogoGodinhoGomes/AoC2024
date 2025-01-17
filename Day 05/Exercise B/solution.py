import functions as fc

values, rules, inver, series = fc.getInfo("code.txt")

total, incorrect = fc.getCorrectTotal(rules, series)

corrected, updated = [], 0

for serie in incorrect:
    corrected.append(fc.getSerieSorted(serie, rules))

for elem in corrected:
    assert len(elem) % 2 == 1
    
    updated += int(elem[int((len(elem) - 1) / 2)])

print(updated)