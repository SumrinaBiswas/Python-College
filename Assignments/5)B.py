# Write a Python script to print all Prime numbers between 1 to n.

p=int(input('enter the range : '))
li=[]
def prime_no():
    for i in range(1,p):
        flag=0
        for j in range(2,(i//2)+1):
            if(i%j==0):
                flag=1
            else:
                flag=0
        if(flag==0):
            li.append(i)
    return (li)
print('prime no in 1 to n : ',prime_no())       
        