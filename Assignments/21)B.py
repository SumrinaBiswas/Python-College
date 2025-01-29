'''B) Write Python programs to sum the given sequences up to n terms: 2/9 - 5/13 + 8/17…'''

import math

n=int(input('range : '))
c=0
for i in range(1,n+1):
    c=c+(pow(-1,(i-1)))*((3*i-1)/(4*i+5))
print('\naddition : ',c)