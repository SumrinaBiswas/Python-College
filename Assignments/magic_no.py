def magic_number(num):
    """Check if a number is a magic number"""
    n = num  # Store original number
    
    while num > 9:  # Keep summing digits until a single-digit is obtained
        s = 0
        while num > 0:
            s += num % 10  # Add last digit to sum
            num //= 10  # Remove last digit
        num = s  # Update num to the sum
    
    if num == 1:
        print(f"{n} is a Magic Number")
    else:
        print(f"{n} is NOT a Magic Number.")

# Taking input from the user
num = int(input("Enter a number: "))
magic_number(num)

