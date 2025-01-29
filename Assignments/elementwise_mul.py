#Write a python program to perform the elements-wise multiplication of two 3X3 Matrices.
import numpy as np
def matx(m,n):
    a=input()
    b=list(map(int,a.split()))
    arr=np.array(b)
    arr=arr.reshape(m,n)
    print("Matrix is :")
    return(arr)

m=int(input('enter row no:'))
n=int(input('enter coloumn no:'))
print("1st matx elem: ")
arr1=matx(m,n)
print('Matrix1\n',arr1)
print("2nd matx elem: ")
arr2=matx(m,n)
print('Matrix2:\n',arr2)
li=[]
c=[[0 for i in range(m)] for y in range (n)] # eg. for 3x3 matrix c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (m):
    for j in range (n):
        c[i][j]=arr1[i][j]*arr2[i][j]
print(c)
