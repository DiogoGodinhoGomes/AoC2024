import functions as fc

mapa = fc.getMapa("code.txt")

paths = fc.getInitialPoints(mapa)

paths = fc.getPaths(mapa, paths)

scores = fc.getScores(paths)

total = fc.getTotal(scores)

print(total)