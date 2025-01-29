#Write a python program to perform the addition of two 3X3 Matrices.

import numpy as np
a=input("enter the array elem :")
b=list(map(int,a.split()))
arr1=np.array(b)
arr1=arr1.reshape(3,3)
print(arr1)

a1=input("enter the array elem :")
b1=list(map(int,a1.split()))
arr2=np.array(b1)
arr2=arr2.reshape(3,3)
print(arr2)

arr3=np.add(arr1,arr2)
print("Added Matrix:\n",arr3)
