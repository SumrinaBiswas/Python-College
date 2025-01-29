# A) Write a Python program to print every integer between 1 and n divisible by m. Also report whether the number that is divisible by m is even or odd.

def e_o(x):
    if(x%2==0):
        return 1
    else:
        return 0
n=int(input('range :'))
m=int(input('checking data :'))
li1=[]
li2=[]
li3=[]
for i in range(1,n):
    if(i%m==0):
        li1.append(i)
        s=e_o(i)
        if(s==1):
            li2.append(i)
        else:
            li3.append(i)
print('divisible list ',li1)
print('even list :',li2)
print('odd list :',li3)