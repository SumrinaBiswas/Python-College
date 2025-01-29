# B) Write a program to take N (N &gt; 20) as an input from the user. Print numbers from
#11 to N. When the number N is a multiple of 3, print &quot;Tipsy&quot;, when it is a multiple of 7,
#print &quot;Topsy&quot;. When it is a multiple of both, print &quot;TipsyTopsy

n=int(input('range(>20): '))
li=[]
li1=[]
li2=[]
li3=[]
for i in range(11,n):
    li.append(i)
    if(i%3==0 and i%7==0):
        li1.append(f'{i} : TipsyTopsy')
    elif(i%3==0 ):
        li2.append(f'{i}: Tipsy')
    elif(i%7==0):
        li3.append(f'{i} : Topsy')
    
print(li)
print(li1)
print(li2)
print(li3)
