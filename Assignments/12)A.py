# Write a python program to find the Twins primes between a range( Twin primes are
#pairs of prime numbers that have just one number between them: 5 and 7, 11 and 13,and 29 and 31)
x=int(input('range : '))
li=[]

def prime(i):
            flag=0
            for j in range(2,(i//2)+1):
                if(i%j==0):
                    flag=1
                else:
                    flag=0
            if(flag==0):
                return 1
            else:
                return 0

for i in range (1,x):
    if(prime(i)and prime(i+2)):
        li.append(f'{i} and {i+2}')
print('twin prime: ',li)           
