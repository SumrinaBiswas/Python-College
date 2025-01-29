# Write a python program to find the mean and median of a set of elements.

li=[]
n=int(input("no of data : "))
for i in range (n):
    li.append(int(input("enter data : ")))
print(li)
s=0
for i in range (n):
    s=s+li[i]
print("sum of elems : ",s)
mean=(s/(len(li)))
print('mean is :',mean)

print('lemgth of lis:',len(li))
def bubble(li):
    for i in range(0,len(li)):
        for j in range(0,(len(li)-i-1)):
            if(li[j]>li[j+1]):
                temp=li[j]
                li[j]=li[j+1]
                li[j+1]=temp
    return li
print(bubble(li))
median=li[len(li)//2]       # middle value of a sorted dataset
print('median is : ',median)