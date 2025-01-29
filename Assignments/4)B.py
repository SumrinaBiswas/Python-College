# Remove all duplicates characters from a given string in Python
#Examples:
#Input : abcabcde
#Output : abcde

n=input('Enter string: ')
s=set(n)
result=""       # initializing string
for i in s:
    result=result+i    # no idx value is required i is denoting every string
print(result)
