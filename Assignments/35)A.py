
li=[]
li1=[]
n=int(input('range :'))
for i in range(n):
    li.append(int(input('elem :')))
print('list1 :',li)
for i in range(n):
    li1.append(int(input('elem :')))
print('list1 :',li1)
a=set(li)
b=set(li1)
c=a.union(b)
d=a.intersection(b)
print('union :',list(c))
print('intersection',list(d))