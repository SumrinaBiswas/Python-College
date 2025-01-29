#Write programs using nested loops to produce the following patterns:
#A
#A B
#A B C
#A B C D
#A B C D E
#A B C D E F
n=int(input('line :'))
for i in range(1,n+1):
    for j in range(ord('A'),ord('A')+i):        # ASCII value conversion=> ord func
        print(chr(j),end=' ')                   #printing char
    print('\n')