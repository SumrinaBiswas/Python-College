n=int(input('range :'))
li=[]
for i in range(n):
    li.append(input('string :'))
print(li)
m=li[0]
c = len(m)  # Initialize c with its length
for i in range(len(li)):
    if(len(m)<len(li[i])):
        m=li[i]
        c=len(m)
print(m)
print(c)