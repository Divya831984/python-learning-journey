# Day 2 Bonus Challenge: Simple Calculator
# Takes two numbers and an operator as input
# Performs the calculation
# Handles division by zero
# Returns the result or an error message

def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operator == '%':
        return a % b
    elif operator == '**':
        return a ** b
    else:
        return "Error: Invalid operator"

# Test cases
print("=== Bonus Challenge: Simple Calculator ===")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
print(f"2 ** 3 = {calculator(2, 3, '**')}")
print(f"10 % 3 = {calculator(10, 3, '%')}")
print(f"10 $ 5 = {calculator(10, 5, '$')}")
