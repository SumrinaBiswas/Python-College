# Write a python program to convert a decimal number to a number of a given base b.

def rev(n):
    c=0
    while(n!=0):
        r=n%10
        c=c*10+r
        n=n//10
    return(c)   
b=int(input('enter base:'))
m=int(input("decimal no :"))
p=m
s=0
while(m!=0):
    rem=m%b
    s=s*10+rem
    m=m//b
x=rev(s)
if(s>=b):
    print("converted no : ",x)
else:
    print('les than base')
    