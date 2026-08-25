# Day 1 Assessment - My Solutions
# Write your code below for each exercise

# Exercise 1: Variable Creation (5 minutes)
# Create variables for the following information:
# - Your first name
# - Your last name
# - Your age
# - Your height in feet (as a decimal)
# - Whether you know how to swim (boolean)
# Print all variables with descriptive messages.

# Write your code here:

first_name = "divya" 
last_name = "nagaraj" 
age = 42 
height = 5.0 
can_swim = True  # or False if you can't swim
print(f"Name {first_name} {last_name} whose Age is {age} with Height {height} can swim {can_swim}")

print(type(42))
print(type(3.14))
print(type("Hello World"))
print(type(True))
print(type('100'))

#42 → <class 'int'> ✓
#3.14 → <class 'float'> ✓
#"Hello World" → <class 'str'> ✓
#True → <class 'bool'> ✓
#'100' → <class 'str'> ✓

x = "25"
y = int(x) + 10
print(f"Convert \"25\" to integer and add 10 and the result is {y}")

m = 3.7
n = int(m) 
print(f"Convert 3.7 to integer and the result is {n}")

s = 100
p = str(s)
print(f"Convert 100 to string and the result is {p}")

a = "45.5"
b = float(a)
print(f"Convert \"45.5\" to float and the result is {b}")

k = True
l = int(k)
print(f"Convert True to integer and the result is {l}")

#"25" → integer + 10 = 35 ✓
#3.7 → integer = 3 ✓ (truncates decimal)
#100 → string = "100" ✓
#"45.5" → float = 45.5 ✓
#True → integer = 1 ✓

s = "15"
num = str(int(s) * 2)
print(f"Double of {s} is {num}")

second_place = "Silver"  # Fixed: can't start with number
course = "History 101"   # Fixed: 'class' is a keyword
age = 25                 # Fixed: use number instead of word
age_int = int(age)