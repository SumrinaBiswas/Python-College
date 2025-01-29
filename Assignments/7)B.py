# B) Write a Python function that takes a list and returns a new list with unique elements of the first list.

n=int(input('range of list:'))
li=[]
for i in range(n):
    li.append(int(input('Enter data :')))
print('original list : ',li)
s=list(set(li))
print('new list :',s)