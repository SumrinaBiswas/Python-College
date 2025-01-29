'''A) Generate the average marks(CGPA) of 10 section then plot it using suitable graph.'''
import random
import matplotlib.pyplot as plt
x=['s1','s2','s3','s4','s5','s6']
y=[]
for i in range(len(x)):
    y.append(random.randint(5,10))
plt.bar(x,y)
plt.show()