'''B) i. Write a program to compare two equal sized lists and print the first index where
they differ.'''
n=int(input('range : '))
li=[]
li1=[]
for i in range(n):
    li.append(int(input('enter elem: ')))
for i in range(n):
    li1.append(int(input('enter elem: ')))
li2=[]
for i in range (n):
    if(li[i]!=li1[i]):
        print('differ at',i)