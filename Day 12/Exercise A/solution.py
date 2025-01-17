import functions as fc

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

mapa, plots = fc.getPlots("code.txt", dirs)

plots = fc.getMeasures(mapa, plots, dirs)

print(fc.getTotal(plots))