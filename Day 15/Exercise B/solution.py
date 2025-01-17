import functions as fc

start, mapa, inst, dtnr = fc.read("code.txt")

mapa = fc.move(start, mapa, inst, dtnr)

print(fc.total(mapa))