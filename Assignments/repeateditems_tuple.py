#Write a Python program to find the repeated items of a tuple.

def repeated(tup1):
    tup2=tup1
    li=[]
    #print(tup2)
    
    for i in range(0,len(tup1)):
        flag=0
        a=tup1[i]
       
        
        for i in range(0,len(tup1)):
            if(a==tup2[i]):
                flag=flag+1
                        
        if(flag>=2):
            li.append(a)
            print("a is :",a)
            print("Repeated time :",flag)

    return tuple(li)
u=input("Enter elems separated by spaces : ")
tup=tuple(map(int,u.split()))
print("Original tuple:",tup)
print('repeated elems are : ',repeated(tup))
