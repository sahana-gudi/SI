# SI
# Simple Interest Calculator

def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

# Input from user
P = float(input("Enter the Principal amount (P): "))
R = float(input("Enter the Rate of interest (R): "))
T = float(input("Enter the Time period in years (T): "))

# Calculate SI
simple_interest = calculate_simple_interest(P, R, T)

# Display result
print(f"\nSimple Interest = {simple_interest:.2f}")
