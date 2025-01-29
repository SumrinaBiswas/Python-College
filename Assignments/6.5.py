#Copy element 44 and 55 from the following tuple into a new tuple tuple1 = (11, 22, 33, 44, 55, 66)
def copy(tup1):
    li=[]
    
    a=int(input('Enter the no to be copied : '))
    for i in range (a) :
        b=int(input("enter the elems :"))
        #print(li.append(b))
        for i in range (0,len(tup1)):
            if(b==tup1[i]):
                li.append(b)
    return(tuple(li))

u=input("Enter elems separated by spaces : ")
tup=tuple(map(int,u.split()))
print("Original tuple:",tup)
print("copied elems : ",copy(tup))
