import numpy as np
import matplotlib.pyplot as plt
import sys
#histogram and barchart

population_ages = [22, 55, 62, 45, 31, 21, 22, 5, 10, 44, 102, 91, 96, 33, 24, 26, 65, 75, 80, 81, 83, 74, 57, 76] 
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)
plt.show()
