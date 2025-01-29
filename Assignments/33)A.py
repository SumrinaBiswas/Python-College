
n=int(input('no of line:'))
for i in range(1,n+1):
    x=1
    for j in range(n-i):
        print(end=' ')
    for k in range(i): 
        print(x,end=' ')
        x=x+1
    print('\n')
for i in range(1,n):
    v=1
    for j in range(i):
        print(end=' ')
    for k in range(n-i):
        print(v,end=' ')
        v=v+1
    print('\n')