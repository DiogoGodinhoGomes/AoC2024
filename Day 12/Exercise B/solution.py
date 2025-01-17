import functions as fc

# 896340 is too high!

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

mapa = fc.getMapa("code.txt")

plots = fc.getPlots(mapa, dirs)

plots = fc.getNewMeasures(mapa, plots, dirs)

print(fc.getTotal(plots))