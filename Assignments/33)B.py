def no_pyd(n):
    for i in range(1,n+1):
        x=1
        for j in range(n-i):
            print(' ',end=' ')
        for k in range(i):
            print(x,' ',end=' ')
            x=x+1
        print()
    for i in range(1,n+1):
        x=1
        for j in range(i):
            print(' ',end=' ')
        for k in range(n-i):
             print(x,' ', end =' ')
             x=x+1
        print()
            
a=int(input('enter the no of lines:'))
print(no_pyd(a))