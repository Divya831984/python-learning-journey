# Day 2 Assessment - Operators and Expressions (30 Minutes)

## Instructions
- Complete all exercises in order
- Time limit: 30 minutes
- Write your solutions in Python
- No external resources allowed during assessment

## Exercise 1: Arithmetic Operations (5 minutes)
Write a program that:
- Takes two numbers as input (e.g., 15 and 4)
- Performs all arithmetic operations (+, -, *, /, //, %, **)
- Prints the results with descriptive labels

## Exercise 2: Comparison Operators (5 minutes)
Given the variables:
```python
age = 25
score = 85
name = "Alice"
```
Write comparison expressions to check:
1. If age is greater than 18
2. If score is between 80 and 90 (inclusive)
3. If name comes before "Bob" alphabetically
4. If age is equal to 25 AND score is greater than 80
5. If age is less than 30 OR score is greater than 90

## Exercise 3: Logical Operators (5 minutes)
Evaluate the following expressions and explain the results:
1. `True and False or True`
2. `not True or not False`
3. `True and (False or True)`
4. `(not True) and (not False)`
5. `False or (True and False) or True`

## Exercise 4: Bitwise Operations (5 minutes)
Given the numbers a = 12 (binary: 1100) and b = 10 (binary: 1010):
1. Calculate a & b (bitwise AND)
2. Calculate a | b (bitwise OR)
3. Calculate a ^ b (bitwise XOR)
4. Calculate a << 1 (left shift by 1)
5. Calculate a >> 2 (right shift by 2)

## Exercise 5: Operator Precedence (5 minutes)
Evaluate the following expressions without using Python:
1. `2 + 3 * 4`
2. `(2 + 3) * 4`
3. `10 - 2 ** 2 * 3`
4. `5 + 3 * 2 ** 2`
5. `8 / 4 / 2`

## Exercise 6: Practical Application (5 minutes)
Write a function that:
- Takes a number as input
- Returns "Even" if the number is even
- Returns "Odd" if the number is odd
- Returns "Zero" if the number is 0
- Use bitwise operators for the even/odd check

## Bonus Challenge (Time Permitting)
Create a simple calculator that:
- Takes two numbers and an operator as input
- Performs the calculation
- Handles division by zero
- Returns the result or an error message

## Self-Check
After completing the assessment, ask yourself:
- Can I explain operator precedence?
- Do I understand short-circuit evaluation?
- Can I use bitwise operators for practical problems?
- Did I complete all exercises within 30 minutes?

## Solutions (Check after completing)

### Exercise 1 Solution
```python
a = 15
b = 4

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
```

### Exercise 2 Solution
```python
age = 25
score = 85
name = "Alice"

# 1. If age is greater than 18
print(age > 18)  # True

# 2. If score is between 80 and 90 (inclusive)
print(score >= 80 and score <= 90)  # True

# 3. If name comes before "Bob" alphabetically
print(name < "Bob")  # True

# 4. If age is equal to 25 AND score is greater than 80
print(age == 25 and score > 80)  # True

# 5. If age is less than 30 OR score is greater than 90
print(age < 30 or score > 90)  # True
```

### Exercise 3 Solution
```python
# 1. True and False or True
# Evaluation: (True and False) or True = False or True = True

# 2. not True or not False
# Evaluation: (not True) or (not False) = False or True = True

# 3. True and (False or True)
# Evaluation: True and (False or True) = True and True = True

# 4. (not True) and (not False)
# Evaluation: False and True = False

# 5. False or (True and False) or True
# Evaluation: False or False or True = True
```

### Exercise 4 Solution
```python
a = 12  # Binary: 1100
b = 10  # Binary: 1010

# 1. a & b (bitwise AND)
# 1100 & 1010 = 1000 = 8
print(a & b)  # 8

# 2. a | b (bitwise OR)
# 1100 | 1010 = 1110 = 14
print(a | b)  # 14

# 3. a ^ b (bitwise XOR)
# 1100 ^ 1010 = 0110 = 6
print(a ^ b)  # 6

# 4. a << 1 (left shift by 1)
# 1100 << 1 = 11000 = 24
print(a << 1)  # 24

# 5. a >> 2 (right shift by 2)
# 1100 >> 2 = 11 = 3
print(a >> 2)  # 3
```

### Exercise 5 Solution
```python
# 1. 2 + 3 * 4
# Evaluation: 2 + (3 * 4) = 2 + 12 = 14

# 2. (2 + 3) * 4
# Evaluation: 5 * 4 = 20

# 3. 10 - 2 ** 2 * 3
# Evaluation: 10 - (2 ** 2) * 3 = 10 - 4 * 3 = 10 - 12 = -2

# 4. 5 + 3 * 2 ** 2
# Evaluation: 5 + 3 * (2 ** 2) = 5 + 3 * 4 = 5 + 12 = 17

# 5. 8 / 4 / 2
# Evaluation: (8 / 4) / 2 = 2 / 2 = 1.0
```

### Exercise 6 Solution
```python
def check_number(number):
    if number == 0:
        return "Zero"
    # Using bitwise AND to check if even
    elif (number & 1) == 0:
        return "Even"
    else:
        return "Odd"

# Test cases
print(check_number(0))    # Zero
print(check_number(4))    # Even
print(check_number(7))    # Odd
print(check_number(-2))   # Even
```

### Bonus Challenge Solution
```python
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
print(calculator(10, 5, '+'))   # 15
print(calculator(10, 0, '/'))   # Error: Division by zero
print(calculator(2, 3, '**'))   # 8
```

## Assessment Criteria
- All exercises completed: Excellent
- 5/6 exercises completed: Good
- 4/6 exercises completed: Needs review
- Less than 4/6: Review Day 2 material before proceeding
