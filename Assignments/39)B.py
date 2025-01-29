'''B) Delete the second column from a given array and insert the new column in its place.'''
import numpy as np
n=int(input('rrow :'))
m=int(input('col :'))
b=list(map(int,input('elem :').split(' ')))
arr=np.array(b)
arr=arr.reshape(n,m)
print(arr)

arr=np.delete(arr,1,axis=1)
print(arr)
elem=np.array([10,11,12])
arr=np.insert(arr,1,elem,axis=1)
print(arr)