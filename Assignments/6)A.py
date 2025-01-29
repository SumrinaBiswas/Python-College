# A)Write a program to convert centigrade to Fahrenheit and reverse also.

def centi(c):
    f=((c*9)/5)+32
    return f
def faren(f):
    c=((f-32)*5)/9
    return c
c=float(input('enter centigrate : '))
print('farenhite value of c :',centi(c))
f=float(input('enter farenhite : '))
print('centigrate of faren',faren(f))