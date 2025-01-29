# 6.2 Write a Python program to reverse a tuple.

user_input = input("Enter elements of the tuple separated by spaces: ")
user_tuple = tuple(map(int,user_input.split()))
r=tuple(reversed(user_tuple))
print("Original Tuple:", user_tuple)
print("Reversed tuple :",r)