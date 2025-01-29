# Election results of India for the year 2000 is published. Out of 400 seats, &#39;ABC’ got 180, ‘XYZ’ got 200 and ‘MNP’ got the rest. Display the result using suitable graphical tools.
import matplotlib.pyplot as plt
li1=[]
li2=[]
n=int(input("Total seat :"))
m=int(input("enter no of party:"))
for i in range(m):
    li1.append(input("party name: "))
for i in range(m-1):
    li2.append(int(input("seat count : ")))
li2.append(n-(li2[0]+li2[1]))
print(li2)
plt.xlabel('party')
plt.ylabel('seat')
plt.bar(li1,li2)
plt.show()