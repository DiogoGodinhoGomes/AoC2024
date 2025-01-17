import numpy as np

with open("excode.txt") as file:
    for line in file:
        print(np.array(line))