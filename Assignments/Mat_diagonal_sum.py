#Write a python program to create a 3X3 Matrix randomly and calculate the sum of the diagonal elements.
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
sum=0
for i in range(m):
    for j in range(n):
        if(i==j):
            sum=sum+arr1[i][j]
print("Diagonal sum:",sum)
    