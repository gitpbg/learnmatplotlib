import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1, 10, 1)
x2 = np.arange(1, 10, 1)
y2 = 3*x2 + 33

plt.plot(x, 3*x*x*x - 2 * x*x + 4 * x - 5, label='cubic')
plt.plot(x2, y2, label='linear')
# titles and labels
plt.xlabel('Domain')
plt.ylabel('Range')

plt.title('Basic Plotting\nCheck it out')

plt.legend()

plt.show()
