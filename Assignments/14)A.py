# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them
#alphabetically.


def sort():
    s=input('hypen separaed string: ').split('-')
    w=sorted(s)                 # return as list
    result='-'.join(w)     # Concatenate any number of strings., return as string format
    return result
print('sorted string: ',sort())