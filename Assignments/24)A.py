x,y,z=0,0,0
li=[]
n=int(input('enter the no of employee'))
for i in range(n):
    a=li.append(int(input('enter the age :')))
for i in range(n):
    if(li[i]>=26 and li[i]<=35):
        x +=1
    elif(li[i]>=36 and li[i]<=45):
        y +=1
    elif(li[i]>=46 and li[i]<=55):
        z +=1
    else:
        print("invalid :",li[i])
print('No of 1st gr:',x)
print('No of 2nd gr:',y)
print('No of 3rd gr:',z)



