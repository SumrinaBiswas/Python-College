'''34. A) Write a program to input N numbers and then print the largest and
second largest number.'''
n=int(input('range :'))
li=[]
for i in range(n):
    li.append(int(input('elem :')))
print(li)
a=max(li)
max2=li[0]
b=li.sort()
print(f'max : {li[-1]}\nmax2 : {li[-2]}')