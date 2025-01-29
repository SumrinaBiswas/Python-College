#B) Write a python program to find the last position of a substring “Emma” in a given string.

def find_last_position(input_string, substring):
    # Using rfind() to find the last position of the substring
    last_position = input_string.rfind(substring)

    return last_position

# Example usage:
input_str = input("Example :")
substring_to_find = input('To find :')
last_position = find_last_position(input_str, substring_to_find)

print("Original String:", input_str)
print(f"Last position of '{substring_to_find}': {last_position}")
