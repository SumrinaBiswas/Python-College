#6.4 Write a Python program to create a symmetric difference of two sets.

def difference(t1,t2):
    
    a=set(t1)
    b=set(t2)
    c=a.union(b)
    d=a.intersection(b)
    t3=tuple(c.difference(d))
    print('union :',c)
    print('intersection :',d)
    return(t3)
u=input("Enter elems separated by spaces for tup1 : ")
tup1=tuple(map(int,u.split()))
print("tuple1:",tup1)
v=input("Enter elems separated by spaces for tup2 : ")
tup2=tuple(map(int,v.split()))
print("tuple2:",tup2)
print('new tuple :',difference(tup1,tup2))