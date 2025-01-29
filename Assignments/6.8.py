#Below are the two lists convert it into the dictionary
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]

keys=[]
values=[]
for i in range (0,3):
    keys.append(input("Enter keys :"))
    values.append(int(input("Enter values:")))
print(keys)
print(values)
d=dict(zip(keys,values))
print(d)

