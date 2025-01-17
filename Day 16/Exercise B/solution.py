import functions as fc

# 587 IS TOO HIGH!

mapa, start, end, dirs = fc.read("code.txt")

mxm, mdrs, mscr = fc.result(mapa, start, end, dirs)

tiles = fc.tiles(dirs, mscr, start, end, mxm)

print(len(tiles))