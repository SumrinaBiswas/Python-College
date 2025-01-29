#Write a Python function that takes a list and returns a new list with unique elements of the first list.
li=[]
n=int(input('enter the number of the list: '))
for i in range(n):
    li.append(int(input("Enter the no : ")))
print("Actual list")
print(li)
s=set(li)
print(list(s))
