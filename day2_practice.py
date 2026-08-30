# Day 2 Practice - Operators and Expressions
# Run this file to practice today's concepts

print("=== Day 2 Practice: Operators and Expressions ===\n")

# Exercise 1: Arithmetic Operations
print("Exercise 1: Arithmetic Operations")
print("-" * 30)

a = 15
b = 4

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Exercise 2: Comparison Operators
print("\nExercise 2: Comparison Operators")
print("-" * 30)

age = 25
score = 85
name = "Alice"

print(f"Age > 18: {age > 18}")
print(f"Score between 80-90: {score >= 80 and score <= 90}")
print(f"Name before 'Bob': {name < 'Bob'}")
print(f"Age == 25 AND score > 80: {age == 25 and score > 80}")
print(f"Age < 30 OR score > 90: {age < 30 or score > 90}")

# Exercise 3: Logical Operators
print("\nExercise 3: Logical Operators")
print("-" * 30)

print(f"True and False or True: {True and False or True}")
print(f"not True or not False: {not True or not False}")
print(f"True and (False or True): {True and (False or True)}")
print(f"(not True) and (not False): {(not True) and (not False)}")
print(f"False or (True and False) or True: {False or (True and False) or True}")

# Exercise 4: Bitwise Operations
print("\nExercise 4: Bitwise Operations")
print("-" * 30)

a = 12  # Binary: 1100
b = 10  # Binary: 1010

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")
print(f"a & b (AND): {a & b} (binary: {bin(a & b)})")
print(f"a | b (OR): {a | b} (binary: {bin(a | b)})")
print(f"a ^ b (XOR): {a ^ b} (binary: {bin(a ^ b)})")
print(f"a << 1 (left shift): {a << 1} (binary: {bin(a << 1)})")
print(f"a >> 2 (right shift): {a >> 2} (binary: {bin(a >> 2)})")

# Exercise 5: Operator Precedence
print("\nExercise 5: Operator Precedence")
print("-" * 30)

print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")
print(f"10 - 2 ** 2 * 3 = {10 - 2 ** 2 * 3}")
print(f"5 + 3 * 2 ** 2 = {5 + 3 * 2 ** 2}")
print(f"8 / 4 / 2 = {8 / 4 / 2}")

# Exercise 6: Practical Application
print("\nExercise 6: Number Properties Checker")
print("-" * 30)

def check_number(number):
    if number == 0:
        return "Zero"
    elif (number & 1) == 0:  # Bitwise check for even
        return "Even"
    else:
        return "Odd"

test_numbers = [0, 4, 7, -2, 15]
for num in test_numbers:
    print(f"{num} is {check_number(num)}")

# Bonus: Simple Calculator
print("\nBonus: Simple Calculator")
print("-" * 30)

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

print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
print(f"2 ** 3 = {calculator(2, 3, '**')}")

print("\n=== Practice Complete ===")
print("Review the concepts and try the assessment!")
