import numpy as np
import matplotlib.pyplot as plt
import sys
#histogram and barchart
days = [1, 2, 3, 4, 5]
sleeping = [8, 7, 6, 10, 7]
eating =   [3, 3, 2, 3, 3]
working =  [8, 9, 8, 7, 7]
playing =  [5, 5, 8, 4, 7]

#
# Hack to add legend to stackplot
#
plt.plot([], [], color='m', label='sleeping', linewidth=5)
plt.plot([], [], color='c', label='eating', linewidth=5)
plt.plot([], [], color='r', label='working', linewidth=5)
plt.plot([], [], color='b', label='playing', linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'b'])

#plt.xlabel("ex")
#plt.ylabel("why")
plt.legend()
plt.title("Time Spent Per Day")
plt.show()
#plt.savefig("foo.png")
