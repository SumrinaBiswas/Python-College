# Write a python program to find out the palindromic prime numbers between a range.

def palindrome(n):
    s=0
    p=n
    while(n>0):
        rem=n%10
        s=s*10+rem
        n=n//10
    if(p==s):
        return 1
    else: 
        return 0

x=int(input('enter the range : '))
li=[]
li1=[]
def prime_no():
    for i in range(1,x):
        flag=0
        for j in range(2,(i//2)+1):
            if(i%j==0):
                flag=1
            else:
                flag=0
        if(flag==0):
            li.append(i)
            y=palindrome(i)
            if(y==1):
                li1.append(i)
    print('prime : ',li)
    print('prime and palindrome:',li1)   
  
    return (li1)
prime_no()
            

        