# B) Print the following pattern using Python program
  #  1
   # 2 1
   # 4 2 1
   # 8 4 2 1
   # 16 8 4 2 1
   # 32 16 8 4 2 1
   # 64 32 16 8 4 2 1
import math
n=int(input('enter line: '))
for i in range(n):
    
    for j in range(i+1,0,-1):           # for decreasing indexing and step =-1, so indexing start with i+1
        print(pow(2,(j-1)),end=' ')     # as indexing starts with i+1, so j will be decreased by 1
        
    print('\n')
    
   
   