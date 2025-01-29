# A) Python program to check if a given string is binary string or not
n1 = int(input('Enter a number: '))
fl = 0

for digit in str(n1):
    if digit not in ['0', '1']:
        fl = 1
        break

if fl == 0:
    print('Binary')
else:
    print('Not binary')
