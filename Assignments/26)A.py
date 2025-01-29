'''A) Write a program to calculate the amount payable after simple and compound
interest.'''
def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    amount_payable = principal + simple_interest
    return amount_payable

def calculate_compound_interest(principal, rate, time):
    compound_interest = principal * ((1 + rate / 100) ** time - 1)
    amount_payable = principal + compound_interest
    return amount_payable

# Input values
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (%): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate and display results for simple interest
simple_interest_result = calculate_simple_interest(principal_amount, interest_rate, time_period)
print(f"\nAmount payable after simple interest: {(simple_interest_result)}")

# Calculate and display results for compound interest
compound_interest_result = calculate_compound_interest(principal_amount, interest_rate, time_period)
print(f"Amount payable after compound interest: {(compound_interest_result)}")
