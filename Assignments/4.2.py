def length(word):
    count =0
    str=[]
    for i in str:
        count += 1
    return count
s=[]
a=input('Enter the words :')
print(a)
#for i in (0,a):
   # s.append(input('enter the word: '))
word=a.split()
w=length(word)%2
if(w==0):
    print(word,'','is a even length word')
