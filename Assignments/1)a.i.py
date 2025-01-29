#Take a string of length greater than 2, return a string except 1 st and last characters.

s1=input("Enter a string : ")
if(len(s1)>2):
    print("New string : ",s1[1:len(s1)-1])
else:
    print("length is not greater than 2:",len(s1))