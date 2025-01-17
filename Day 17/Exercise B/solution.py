import functions as fc

rgtr, pgrm, dtnr, program = fc.read("excode.txt")

i = 0

while fc.string([0, 1, 2, 3, i, 5, 6, 7], pgrm) != program:
    i += 1

print(i)