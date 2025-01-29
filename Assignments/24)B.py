'''B) Write programs as per following specifications: &#39;&#39;Print the length of the longest
string in the list of strings str_list. Precondition : the list will contain at least one
element.'''

li=[]
n=int(input('range:'))
for i in range(n):
    li.append(input('enter string :'))
print('list :',li)
largelen=0
l_idx=0
for i in range(len(li)):
    length=len(li[i])
    if(largelen<length):
        largelen=length
        l_idx=i
print(li[l_idx])

# ALT
n=int(input('range :'))
li=[]
for i in range(n):
    li.append(input('string :'))
print(li)
m=li[0]
for i in range(len(li)):
    if(len(m)<len(li[i])):
        m=li[i]
        c=len(m)
print(m)
print(c)