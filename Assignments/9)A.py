# Write a python program to take an input list and removes the element at index 4

# and add it to the 2nd position and also, at the end of the list.

n=int(input("range : "))
li=[]
for i in range (n):
    li.append(int(input("Enter data : ")))
print('Original : ',li)
p=int(input('enter position to be deleted: '))
q=int(input('enter adding position: '))
li.remove(li[p-1])              # as idx val starts with 0, idx=position-1
li.insert(q-1,li[p-1])

print('new list :',li)

