n1=int(input('enter 1st elem: '))
n2=int(input('enter 2nd elem: '))
i=1
while(i<=n1 and i<=n2):
    if(n1%i==0 and n2%i==0):
        gcd=i
    i +=1
lcd= (n1*n2)//gcd
print('gcd is : ',gcd)
print('lcd is: ',lcd)