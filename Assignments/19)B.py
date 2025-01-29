'''B)Write a Python script to find all roots of a quadratic equation 2 for
all possible combinations of a, b and c.'''
import math
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(f'eq : {a}x^2+{b}x+{c}')
d=(b**2)/(4*a*c)
if(d==0):
    x=(-b)/(2*a)
    print("equal real sol: ",x)
elif(d>0):
    x1=((-b)+math.sqrt(d))/(2*a)
    x2=((-b)-math.sqrt(d))/(2*a)    
    print(f'x1 = {x1}, x2={x2}')
elif(d<0):
    x1=((-b)+math.sqrt(d))/(2*a)
    x2=((-b)-math.sqrt(d))/(2*a)    
    print(f'x1 = {x1}, x2={x2}')