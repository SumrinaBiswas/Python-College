def find_string(rank, length):
    result = []
    available_chars = list('abcdefghijklmnopqrstuvwxyz ')

    # Decrement rank as the index starts from 0
    rank -= 1

    # Iterate through each position in the string
    for i in range(length - 1, -1, -1):
        # Compute the index of the character at the current position
        index = rank // factorial(i)

        # Update the result with the selected character
        result.append(available_chars [index])

        # Remove the selected character from available_chars
        available_chars.pop(index)

        # Update the remaining rank
        rank %= factorial(i)

    # Reverse the result to get the correct order
    result.reverse()

    return ''.join(result)

# Function to calculate factorial
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# Input rank and length
rank = int(input("Enter rank: "))
length = int(input("Enter length: "))

# Find and print the string
result = find_string(rank, length)
print("String:", result)