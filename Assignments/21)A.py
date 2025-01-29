'''A) write a program to input a list of numbers and test if a number is equal to the sum
of the cubes of its digits. Print that new list and find the smallest and greatest element
of that list.'''

import math
li=[]
li1=[]
def add(n):
    c=0
    p=n
    while(p>0):
        rem=p%10
        c=c+pow(rem,3)
        p=p//10
    return c
x=int(input("enter the size:"))
for i in range(x):
    li.append(int(input('enter elem :')))
print('list :',li)
for i in range (x):
    y=add(li[i])
    if(y==li[i]):
        li1.append(li[i])
print('new list ',li1)
print('max :',max(li1))
print('min :',min(li1))
        
        