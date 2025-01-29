'''A) Create a matrix randomly then sort it with respect to 2 nd row.'''
import numpy as np

# User input for the dimensions of the matrix
n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

# Create a random matrix
b=list(map(int,input('elem :').split(' ')))
arr=np.array(b)
arr=arr.reshape(n,m)
print(arr)

# Sort the matrix with respect to the second row
sorted_indices = np.argsort(arr[1, :])
sorted_matrix = arr[:, sorted_indices]

print("Sorted Matrix with respect to the second row:")
print(sorted_matrix)