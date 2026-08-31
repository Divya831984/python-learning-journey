# Day 3 Practice - Control Flow
# Run this file to practice today's concepts

print("=== Day 3 Practice: Control Flow - if/else Statements ===\n")

# Exercise 1: Basic if Statement
print("Exercise 1: Basic if Statement")
print("-" * 30)

number = 5
if number > 0:
    print("The number is positive")

number = -3
if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")

# Exercise 2: if-else Statement
print("\nExercise 2: if-else Statement")
print("-" * 30)

number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 3: if-elif-else Chain
print("\nExercise 3: if-elif-else Chain")
print("-" * 30)

score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")

# Test with different scores
for test_score in [95, 75, 55]:
    if test_score >= 90:
        test_grade = 'A'
    elif test_score >= 80:
        test_grade = 'B'
    elif test_score >= 70:
        test_grade = 'C'
    elif test_score >= 60:
        test_grade = 'D'
    else:
        test_grade = 'F'
    print(f"Score: {test_score}, Grade: {test_grade}")

# Exercise 4: Nested Conditions
print("\nExercise 4: Nested Conditions")
print("-" * 30)

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need to get a license")
else:
    print("You are too young to drive")

# Test different scenarios
test_cases = [
    (25, True),   # Can drive
    (25, False),  # Needs license
    (16, True),   # Too young
    (16, False)   # Too young
]

for test_age, test_license in test_cases:
    if test_age >= 18:
        if test_license:
            result = "Can drive"
        else:
            result = "Needs license"
    else:
        result = "Too young"
    print(f"Age: {test_age}, License: {test_license} -> {result}")

# Exercise 5: Logical Operators
print("\nExercise 5: Logical Operators")
print("-" * 30)

username = "admin"
password = "secret123"
is_active = True

if username == "admin" and password == "secret123" and is_active:
    print("Login successful")
else:
    print("Login failed")

# Test different login scenarios
login_tests = [
    ("admin", "secret123", True),   # Success
    ("admin", "wrongpass", True),    # Wrong password
    ("user1", "secret123", True),   # Wrong username
    ("admin", "secret123", False),   # Inactive account
]

for test_user, test_pass, test_active in login_tests:
    if test_user == "admin" and test_pass == "secret123" and test_active:
        result = "Login successful"
    else:
        result = "Login failed"
    print(f"User: {test_user}, Active: {test_active} -> {result}")

# Exercise 6: Ternary Operator
print("\nExercise 6: Ternary Operator")
print("-" * 30)

temperature = 35
weather = "hot" if temperature > 30 else "moderate"
print(f"Temperature: {temperature}, Weather: {weather}")

number = 8
parity = "even" if number % 2 == 0 else "odd"
print(f"Number: {number}, Parity: {parity}")

# Test ternary with different values
for temp in [25, 35, 15]:
    temp_weather = "hot" if temp > 30 else "moderate"
    print(f"Temp: {temp} -> {temp_weather}")

# Bonus: ATM Machine
print("\nBonus: ATM Machine")
print("-" * 30)

def atm_machine(pin, balance, amount):
    correct_pin = "1234"
    
    if pin == correct_pin:
        if amount <= balance:
            balance -= amount
            return f"Withdrawal successful. New balance: ${balance}"
        else:
            return "Insufficient funds"
    else:
        return "Wrong PIN"

# Test cases
print(atm_machine("1234", 1000, 500))   # Success
print(atm_machine("1234", 1000, 1500))  # Insufficient funds
print(atm_machine("9999", 1000, 500))   # Wrong PIN

print("\n=== Practice Complete ===")
print("Review the concepts and try the assessment!")
