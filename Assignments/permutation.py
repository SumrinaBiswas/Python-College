#Write a python program to show the permutation and combination of an inputted List.
from itertools import permutations, combinations

li=[]
n=int(input('enter the number of the list: '))
for i in range(n):
    li.append(int(input("Enter the no : ")))
print("Actual list")
print(li)
s=set(li)
a=int(input('range : '))
p=permutations(li,a)
print(p)