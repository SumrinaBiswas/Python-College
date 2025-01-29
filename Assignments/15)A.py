# A) Write a Python script to check whether a number is an Armstrong number or not.
import math
n=int(input('enter no : '))
def count(x):
    c=0
    while(x!=0):
        c=c+1
        x=x//10
    return c
def armstrong(p):
    y=p
    q=0
    t=count(p)
    while(p!=0):
        rem=p%10
        q=q+pow(rem,t)
        p=p//10
    if(q==y):
        return 1
    else:
        return 0
m=armstrong(n)
if(m==1):
    print('armstrong :',n)
else:
    print('not armstrong :',n)
    
    