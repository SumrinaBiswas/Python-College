#Write a Python program to create set difference.

def difference(t1,t2):
    print(f"1st tupple :{t1}\n2nd tuple :{t2}")
    a=set(t1)
    b=set(t2)
    t3=tuple(a.difference(b))
    return(t3)
u=input("Enter elems separated by spaces for tup1 : ")
tup1=tuple(map(int,u.split()))
print("tuple1:",tup1)
v=input("Enter elems separated by spaces for tup2 : ")
tup2=tuple(map(int,v.split()))
print("tuple2:",tup2)
print('new tuple :',difference(tup1,tup2))
    