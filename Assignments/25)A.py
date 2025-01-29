'''A) Write programs to find the sum of the following series:
x - x^2 /2! + x^3 /3! - x^4 /4! + x^5 /5! - x^6 /6! (Input x)'''
import math
def fact(n):
    c=1
    for i in range (1,n+1):
        c=c*i
    return c
v=fact(5)
print(v)
x=int(input('x= '))
m=int(input('range :'))
s=0
for i in range (1,m+1):
    s=(pow((-1),(i-1)))*(pow(x,i)/fact(i))
print(s)
        