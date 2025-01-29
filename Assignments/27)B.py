'''B) Read two matrices and add them. Store the matrices and result in a file.'''
import numpy as np
def mat(m,n):
    a=input()
    s=list(map(int,a.split()))
    b=np.array(s)
    b=b.reshape(m,n)
    return b
m=int(input('enter row no:'))
n=int(input('enter coloumn no:'))
print("1st matx elem: ")
arr1=mat(m,n)
print('Matrix2\n',arr1)
print("2nd matx elem: ")
arr2=mat(m,n)
print('Matrix2\n',arr2)
arr3=np.add(arr1,arr2)
print("add: ",arr3)
f=open('27_B.txt','w')
f.write(f'matrix1: {arr1} , matrix2: {arr2} , add: {arr3}')
