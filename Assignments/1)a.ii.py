#Take 2 strings, s1, and s2 return a new string made of the first, middle and last char of each input string.

s1=input("Enter 1st string : ")
s2=input("Enter 2nd string : ")
def mid(s):
     mid=len(s)//2

     return(mid)

print("new string : ",s1[0]+s2[0]+s1[mid(s1)]+s2[mid(s2)]+s1[-1]+s2[-1])