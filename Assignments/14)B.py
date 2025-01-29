#5.5 Write a Python program to check if each number is prime in a given list of numbers. Return True if
#all numbers are prime otherwise False.

li=[]
def main(li):
    l=[]
    
    for i in li:
        flag = 0
        for n in range(2,(i//2)+1):
            if(i%n==0):
                flag =1
        if(flag==1):
             print(f"{i}is not a prime no")
                
        else:
            print(f"{i} prime no")
a=int(input("Enter the range of list: "))
for i in range (a):
    li.append(int (input("enter the no")))
print("Actual list")
print(li)
main(li)

