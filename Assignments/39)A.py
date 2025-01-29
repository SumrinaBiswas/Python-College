'''39. A) Python program to accept the strings which contains all vowels
Examples :
Input : ABeeIghiObhkUul
Output : Accepted'''

s = input('Enter a string:')
a = set(s.lower())
b = {'a', 'e', 'i', 'o', 'u'}
c=a.intersection(b)
if b==c:
    print('Accepted')
else:
    print('Not Accepted')
