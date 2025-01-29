# A) Write a program to take a year as input and check If it is a leap year or not.

n=int(input("Enter year :"))
if(n%4==0 and n%100!=0):
    print(n,"Leap year")
else:
    if(n%400==0) :
        print(n,"Leap year")
    else:
        print(n,"not Leap year")