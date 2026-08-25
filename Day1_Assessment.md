# Day 1 Assessment - Python Basics (30 Minutes)

## Instructions
- Complete all exercises in order
- Time limit: 30 minutes
- Write your solutions in a Python file or interactive environment
- No external resources allowed during assessment

## Exercise 1: Variable Creation (5 minutes)
Create variables for the following information:
- Your first name
- Your last name
- Your age
- Your height in feet (as a decimal)
- Whether you know how to swim (boolean)

Print all variables with descriptive messages.

## Exercise 2: Data Type Identification (5 minutes)
For each of the following values, write the data type and use `type()` to verify:
1. `42`
2. `3.14`
3. `"Hello World"`
4. `True`
5. `'100'`

## Exercise 3: Type Conversion (8 minutes)
Perform the following conversions:
1. Convert the string `"25"` to an integer and add 10
2. Convert the float `3.7` to an integer
3. Convert the integer `100` to a string
4. Convert the string `"45.5"` to a float
5. Convert the boolean `True` to an integer

Print the results of each conversion.

## Exercise 4: Practical Application (7 minutes)
Create a simple program that:
- Takes a string number (e.g., `"15"`) as input
- Converts it to an integer
- Multiplies it by 2
- Converts the result back to a string
- Prints a message like "Double of 15 is 30"

## Exercise 5: Debugging (5 minutes)
Fix the following code (identify and correct 3 errors):
```python
2nd_place = "Silver"
class = "History 101"
age = "twenty-five"
age_int = int(age)
```

## Bonus Challenge (Time Permitting)
Create a program that stores information about a book:
- Title (string)
- Author (string)
- Number of pages (integer)
- Price (float)
- Is available (boolean)

Print a formatted message with all book details.

## Self-Check
After completing the assessment, ask yourself:
- Can I create variables with proper naming?
- Do I understand the difference between data types?
- Can I convert between data types correctly?
- Did I complete all exercises within 30 minutes?

## Solutions (Check after completing)
*Do not look at solutions until you've completed the assessment*

### Exercise 1 Solution
```python
first_name = "John"
last_name = "Doe"
age = 25
height = 5.9
can_swim = True

print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Can swim: {can_swim}")
```

### Exercise 2 Solution
```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello World"))  # <class 'str'>
print(type(True))      # <class 'bool'>
print(type('100'))     # <class 'str'>
```

### Exercise 3 Solution
```python
# 1. String to integer + add 10
result1 = int("25") + 10
print(f"Result 1: {result1}")  # 35

# 2. Float to integer
result2 = int(3.7)
print(f"Result 2: {result2}")  # 3

# 3. Integer to string
result3 = str(100)
print(f"Result 3: {result3}")  # "100"

# 4. String to float
result4 = float("45.5")
print(f"Result 4: {result4}")  # 45.5

# 5. Boolean to integer
result5 = int(True)
print(f"Result 5: {result5}")  # 1
```

### Exercise 4 Solution
```python
num_str = "15"
num_int = int(num_str)
doubled = num_int * 2
result_str = str(doubled)
print(f"Double of {num_str} is {result_str}")
```

### Exercise 5 Solution
```python
# Error 1: Variable name can't start with number
second_place = "Silver"

# Error 2: 'class' is a keyword
course = "History 101"

# Error 3: Can't convert "twenty-five" to int directly
age = 25
age_int = int(age)
```

### Bonus Challenge Solution
```python
title = "The Great Gatsby"
author = "F. Scott Fitzgerald"
pages = 180
price = 12.99
is_available = True

print(f"Book: {title}")
print(f"Author: {author}")
print(f"Pages: {pages}")
print(f"Price: ${price}")
print(f"Available: {is_available}")
```

## Assessment Criteria
- All exercises completed: Excellent
- 4/5 exercises completed: Good
- 3/5 exercises completed: Needs review
- Less than 3/5: Review Day 1 material before proceeding
