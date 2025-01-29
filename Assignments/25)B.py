'''B) Write a program to move all duplicate values in a list to the end of the list.'''

l =[]
s=input('enter string:')
l=list(s.split(' '))
print('list :',l)
dedup = []
dup = []
for i in l:
    if i not in dedup:
        dedup.append(i)
    else:
        dup.append(i)

m = dedup + dup
print('update :',dedup)
print('dup:',dup)
print("Modified List:")
print(m)