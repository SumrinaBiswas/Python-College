'''A) Write a program to display the maximum and minimum values from the specified
range of indexes of list.'''
n=int(input('range :'))
li=[]
for i in range(n):
    li.append(int(input('elem :')))
print('List : ',li)
m=int(input('index  :'))
c=li[0]
d=li[0]
for i in range(0,m+1):
    if(c<li[i]):
        c=li[i]
        idx=i
    if(d>li[i]):
        d=li[i]
        idx2=i
    
print(f'{c} : {idx}')
print(f'{d} : {idx2}')

    