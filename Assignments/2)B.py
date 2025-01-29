# Plot the curve O(n) and O(n^2).
import numpy as np
import math
import matplotlib.pyplot as plt

x=np.arange(0,120)
y1=x
y2=pow(x,2)

plt.xlabel('values')
plt.ylabel('Operations')
plt.title('0(n) vs 0(n^2)')
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

