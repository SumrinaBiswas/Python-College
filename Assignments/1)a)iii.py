#Write a python program to take 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.

s1=input("Enter 1st string : ")
s2=input("Enter 2nd string : ")
def mid(s):
    mid=len(s)//2
    return(mid)
print("new string : ",s1[0:mid(s1)]+s2+s1[mid(s2)+1:len(s1)])