# Write a short program to input a digit and print it in words.

def word(n):
    li=['zero','one','two','three','four','five','six','seven','eight','nine']
    print(f'{n} : ',li[n])
    return
a=int(input("enter digit: "))
word(a)