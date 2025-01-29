
n1=int(input('no 1 :'))
n2=int(input('no-2:'))
if(n1<n2):
    c=n1
else:
    c=n2
print(c)
for i in range(1,c+1):
        if(n1%i==0 and n2%i==0):
            gcd=i
lcm=(n1*n2)//gcd
print(gcd,lcm)