import numpy as np
import matplotlib.pyplot as plt
import sys
#histogram and barchart

x = np.random.rand(10)
y = np.random.rand(10)
plt.scatter(x, y,  s=10, marker='x')
plt.xlabel("ex")
plt.ylabel("why")
plt.title("Scatter Brains")
plt.show()
plt.savefig("foo.png")
