
#wrong
def factorial(n):
    fact =1
    for i in range(1,n):
        fact=fact*i
    return fact
        
def series(x,n):
    sum=0
    for i in range(1,n):
        x=((((-)pow(-1,i))*pow(x,i)))/factorial(i)
        sum=sum+x
    return sum
a=int(input('enter the no:'))
b=int(input('no of terms:'))
print('result is:',series(a,b))



