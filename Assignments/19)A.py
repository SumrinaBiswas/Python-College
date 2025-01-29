'''A) Write a Python Program to print the Prime Factors of an Integer.'''

def prime(n):
    flag=0
    for i in range(2,n//2+1):
        if(n%i==0):
            flag=1
            break
        
    if(flag==0):
        return 1
    else:
        return 0
li=[]
m=int(input('range :'))
for i in range(1,m):
    if(m%i==0):
        li.append(i)
print(' factor :',li)
li1=[]
for j in (li):
    c=prime(j)
    if(c==1):
        li1.append(j)
print(li1)