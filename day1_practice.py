# Day 1 Practice - Python Basics
# Run this file to practice today's concepts

print("=== Day 1 Practice: Python Basics ===\n")

# Exercise 1: Creating Variables
print("Exercise 1: Creating Variables")
print("-" * 30)

# Create your variables here
first_name = "Your Name"
last_name = "Last Name"
age = 25
height = 5.9
can_swim = True

print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Can swim: {can_swim}")

# Exercise 2: Data Types
print("\nExercise 2: Data Types")
print("-" * 30)

values = [42, 3.14, "Hello World", True, '100']
for value in values:
    print(f"Value: {value}, Type: {type(value)}")

# Exercise 3: Type Conversion
print("\nExercise 3: Type Conversion")
print("-" * 30)

# String to integer + add 10
result1 = int("25") + 10
print(f"int('25') + 10 = {result1}")

# Float to integer
result2 = int(3.7)
print(f"int(3.7) = {result2}")

# Integer to string
result3 = str(100)
print(f"str(100) = '{result3}'")

# String to float
result4 = float("45.5")
print(f"float('45.5') = {result4}")

# Boolean to integer
result5 = int(True)
print(f"int(True) = {result5}")

# Exercise 4: Practical Application
print("\nExercise 4: Practical Application")
print("-" * 30)

num_str = "15"
num_int = int(num_str)
doubled = num_int * 2
result_str = str(doubled)
print(f"Double of {num_str} is {result_str}")

# Exercise 5: Debugging Practice
print("\nExercise 5: Debugging Practice")
print("-" * 30)

# Fixed version of the buggy code
second_place = "Silver"  # Fixed: can't start with number
course = "History 101"   # Fixed: 'class' is a keyword
age = 25                 # Fixed: use number instead of word
age_int = int(age)

print(f"Second place: {second_place}")
print(f"Course: {course}")
print(f"Age: {age}")
print(f"Age as integer: {age_int}")

print("\n=== Practice Complete ===")
print("Review the concepts and try the assessment!")
