'''B) Write a Python program using a function to check whether a given number is an
ugly number. In the number system, ugly numbers are positive numbers whose only
prime factors are 2, 3 or 5. First 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12. By
convention, 1 is included.'''
def factor(n):
    li=[]
    for i in range(1,n+1):
        if(n%i==0):
            li.append(i)
    return li
x=int(input('no :'))
c=factor(x)
print('prime factor:',c)
for i in (c):
    if(c[i]>=2 and c[i]<=5 and c[i]!=4):
        print(f'{x} is ugly no')
        break
    else:
        print(f'{x} is not ugly no\n')
           
    
    