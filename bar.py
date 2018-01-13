import numpy as np
import matplotlib.pyplot as plt
import sys
#histogram and barchart

x = np.arange(1, 10, 2)
print(x)
y = 10*np.random.rand(5)
x2 = np.arange(0, 10, 2)
y2 = 10*np.random.rand(5)

plt.bar(x, y, label='bars1', color='blue')
plt.bar(x2, y2, label='bars2', color='purple')

plt.xlabel('x')
plt.ylabel('y')
plt.title("Interesting BarChart")
plt.legend()
plt.show()
