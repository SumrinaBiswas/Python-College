'''B) Write a program that takes any two lists L and M of the same size and adds their elements together to form a new list N whose elements are sums of the corresponding
elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should
equal [4,6,13].'''

n=int(input('range :'))
M=[]
L=[]
N=[]
for i in range(n):
    M.append(int(input('data_1 : ')))
for i in range(n):
    L.append(int(input('data_2 : ')))
print('M= ',M)
print('L= ',L)
for i in range(n):
    N.append(M[i]+L[i])
print('N= ',N)
