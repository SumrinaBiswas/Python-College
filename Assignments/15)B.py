# B) Write a Python function to check whether a string is a pangram or not. Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : “The quick brown fox jumps over the lazy dog”

def pangram(s):
    alpha_set=set('abcdefghijklmnopqrstuvwxyz')
    v=set(s.lower())                    # create lowercase of alphabet
    if(alpha_set.issubset(v)):
        return 1
    
st=input('enter string :')
x=pangram(st)
if(x==1):
    print(f'{st} : pangram')
else:
    print(f'{st} : not pangram')
    
