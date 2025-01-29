# Write a Python script to check whether a number is a Perfect number or not.

n=int(input('enter no :'))
p=n
c=0
for i in range(1,n-1):
    if(n%i==0):
        c=c+i
if(p==c):
    print('perfect no: ',p)
else:
    print('not perfect : ',p)