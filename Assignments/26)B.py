'''B) Take the five marks of a student for a particular subject. Display the data graphically
using suitable graphs.'''
import matplotlib.pyplot as plt
import numpy as np
student={}
n=int(input('no of sub:'))
for i in range (n):
    sub=input('Sub : ')
    m=int(input('marks: '))
    student[sub]=m
print('data for one student:',student)
plt.xlabel('subject')
plt.ylabel('marks')
x=student.keys()
y=student.values()
plt.plot(x,y)
plt.bar(x,y)
plt.show()