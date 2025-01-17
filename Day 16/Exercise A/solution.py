import functions as fc

mapa, start, end, dirs = fc.read("code.txt")

result = fc.result(mapa, start, end, dirs)

print(result)