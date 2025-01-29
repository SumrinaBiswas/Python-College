'''A) Write a Python script to create a Simple Calculator on user choice.'''

n1=int(input('enter no 1 :'))
n2=int(input('enter no 2: '))
while(1):
    print('\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n')
    ch=int(input('enter ch :'))
    if(ch==1):
        print('addition :',n1+n2)
        break
    elif(ch==2):
        print('substraction :',n1-n2)
        break
    elif(ch==3):
        print('multiplication :',n1*n2)
        break
    elif(ch==4):
        print('division :',n1/n2)
        break