import numpy as np
import matplotlib.pyplot as plt
import sys
#histogram and barchart
days = [1, 2, 3, 4, 5]
sleeping = [8, 7, 6, 10, 7]
eating =   [3, 3, 2, 3, 3]
working =  [8, 9, 8, 7, 7]
playing =  [5, 5, 8, 4, 7]

slices = [7, 2, 2, 13]
activities = ['Sleeping', 'Eating', 'Working', 'Playing']
cols = ['c', 'm', 'r', 'y']
plt.pie(slices, 
  labels=activities, 
  colors=cols, 
  startangle=90, 
  shadow=True, 
  explode=(0, 0.1, 0, 0),
  autopct='%1.1f%%')
#plt.legend()
plt.title("Time Spent Per Day")
plt.show()
#plt.savefig("foo.png")
