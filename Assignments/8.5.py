#Write a python program to find row wise maximum and column wise minimum element(s).

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
r_max=np.amax(arr1,0)   #row-wisw max
r_min=np.amin(arr1,1)   #col wise min
print(r_max)
print(r_min)