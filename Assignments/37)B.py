'''B) Generate marks of two students for 6 unit tests randomly then compare the result using
suitable graph.'''
import numpy as np
import matplotlib.pyplot as plt
d={}
def dic(d):
    n=(int(input('range :')))
    for i in range(n):
        k=input('Test:')
        v=int(input('marks:'))
        d[k]=v
    return d
student1={}
student2={}
p=dic(student1)
q=dic(student2)
a=p.values()
b=q.values()
c=p.keys()
plt.xlabel('sub')
plt.ylabel('marks')
plt.title('Student test result')
plt.plot(a)                                                     #'''plotting graph for two student in one graph'''
plt.plot(b)
plt.show()
