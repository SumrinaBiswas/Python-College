# B) Python program to check if a string has at least one letter and one number
#Examples:
#Input: welcome2ourcountry34
#Output: True
#Input: stringwithoutnum
#Output: False

def check_string(str):
    letter_flag = False
    number_flag = False
    for char in str:
        if char.isalpha():
            letter_flag = True
        if char.isdigit():
            number_flag = True
    return letter_flag and number_flag      # true and true =true
s=input('string : ')
print(check_string(s))
