def reverse(num):
    num
    s=0
    while(num>0):
        
        
        r=num%10
        s=s*10 +r
        num=num//10
    return s
   
li=[]
a=int(input('enter the no of list:'))
for i in range (a):

    li.append(int(input('enter the elem :')))
print('the list is :')
for i in range(len(li)):
    print(li[i])
for i in range(len(li)):
    n=li[i]
    b=(reverse(li[i]))
    print('rev no is',b)
    if(n==b):
        print(n,'palindrome no')
    else:
        print(n,'not palindrome')