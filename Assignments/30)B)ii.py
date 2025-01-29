''' Write a program to reverse a list without using another list or in-built function.'''
n=int(input('range : '))
li=[]
li1=[]
for i in range(n):
    li.append(int(input('enter elem: ')))
print('list : ',li)
k=0
for i in range(n-1,0,-1):
    li1.append(li[i])
li1.append(li[0])  
print('new list:',li1)
