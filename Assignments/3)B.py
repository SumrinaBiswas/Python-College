# B) Display electricity consumption of a customer for 12 months using suitable
#      graphical tools.
import matplotlib.pyplot as plt
import numpy as np
import random

x=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
y=[]
for i in (x):
    y.append(random.randint(100,1000))

plt.xlabel('Month')
plt.ylabel('Bills')
plt.plot(x,y)
plt.show()
