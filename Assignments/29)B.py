import numpy as np

def mat(m,n):
    b=list(map(int,input('no :').split(' ')))
    c=np.array(b)
    c=c.reshape(m,n)
    return c
m=int(input('row '))
n=int(input('col '))
mat1=mat(m,n)
print(mat1)
s=0
for i in range(m):
    for j in range (n):
        if(i==j):
            s=s+mat1[i][j]
print(s)