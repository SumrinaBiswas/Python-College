# B) Write a Python function that accepts a string and calculate the number of uppercase letters and lowercase letters.

s=input("enter string : ")
c=0
p=0
for i in s:                         # not ddeclare range becoz int and string is not comparable
    if(i>='A' and i<='Z'):
        c=c+1
    elif(i>='a' and i<='z'):
        p=p+1
print('no of upppercase : ',c)
print('no of lowercase : ',p)