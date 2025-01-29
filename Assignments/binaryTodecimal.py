def binarytodecimal(b):
    i=0
    decimal=0
    while(b!=0):
        n=b%10
        if(n==0):
            i +=1
        else:
            decimal=decimal+ pow(2,i)
            i +=1
        b=b//10
        
    return decimal
a=int(input('enter any binary no:'))
p=(binarytodecimal(a))
print('equivalent decimal no:',p)

