# Day 2: Operators and Expressions

## Learning Objectives
- Master arithmetic operators and their behavior
- Understand comparison operators and boolean logic
- Learn logical operators and short-circuit evaluation
- Explore bitwise operators for low-level operations
- Understand operator precedence and associativity
- Practice operator overloading concepts (for senior-level preparation)
- Complete 30-minute assessment

## Arithmetic Operators

### Basic Arithmetic
```python
# Addition
result = 10 + 5        # 15

# Subtraction
result = 10 - 5        # 5

# Multiplication
result = 10 * 5        # 50

# Division (always returns float)
result = 10 / 5        # 2.0
result = 10 / 3        # 3.333...

# Floor Division (integer division)
result = 10 // 3       # 3 (truncates decimal)
result = -10 // 3      # -4 (rounds down)

# Modulus (remainder)
result = 10 % 3        # 1
result = 10 % 5        # 0

# Exponentiation
result = 2 ** 3        # 8
result = 10 ** 2       # 100
```

### Operator Behavior with Different Types
```python
# Integer operations
a = 10
b = 3
print(a + b)           # 13 (int)
print(a / b)           # 3.333... (float)

# Float operations
a = 10.5
b = 3.2
print(a + b)           # 13.7 (float)

# Mixed operations
a = 10
b = 3.5
print(a + b)           # 13.5 (float - promotes to float)
```

## Comparison Operators

### Basic Comparisons
```python
# Equal
x = 5
y = 5
print(x == y)          # True

# Not equal
x = 5
y = 3
print(x != y)          # True

# Greater than
x = 5
y = 3
print(x > y)           # True

# Less than
x = 5
y = 3
print(x < y)           # False

# Greater than or equal
x = 5
y = 5
print(x >= y)          # True

# Less than or equal
x = 5
y = 3
print(x <= y)          # False
```

### Comparison with Different Types
```python
# Numbers
print(5 > 3)           # True
print(5.5 > 5)         # True

# Strings (lexicographical comparison)
print("apple" < "banana")  # True
print("Apple" < "apple")   # True (uppercase comes first)

# Lists (element-wise comparison)
print([1, 2] < [1, 3])    # True
print([1, 2] < [2, 1])    # True
```

## Logical Operators

### Basic Logical Operations
```python
# AND operator (both must be True)
print(True and True)       # True
print(True and False)      # False
print(False and False)     # False

# OR operator (at least one must be True)
print(True or True)        # True
print(True or False)       # True
print(False or False)      # False

# NOT operator (reverses boolean)
print(not True)            # False
print(not False)           # True
```

### Short-Circuit Evaluation
```python
# AND short-circuits (stops at first False)
print(False and print("This won't print"))  # False

# OR short-circuits (stops at first True)
print(True or print("This won't print"))   # True

# Practical example
x = 5
# This won't cause division by zero due to short-circuit
if x != 0 and 10 / x > 2:
    print("Condition met")
```

### Complex Logical Expressions
```python
age = 25
has_license = True
has_car = False

# Can drive if age >= 18 AND has license
can_drive = age >= 18 and has_license
print(can_drive)           # True

# Can travel alone if age >= 18 AND has_license AND has_car
can_travel_alone = age >= 18 and has_license and has_car
print(can_travel_alone)    # False

# Can be passenger if age >= 18 OR (age < 18 AND has_parent_consent)
can_be_passenger = age >= 18 or (age < 18 and True)
print(can_be_passenger)    # True
```

## Bitwise Operators

### Basic Bitwise Operations
```python
# Bitwise AND (&)
a = 5   # Binary: 101
b = 3   # Binary: 011
print(a & b)              # 1 (Binary: 001)

# Bitwise OR (|)
a = 5   # Binary: 101
b = 3   # Binary: 011
print(a | b)              # 7 (Binary: 111)

# Bitwise XOR (^)
a = 5   # Binary: 101
b = 3   # Binary: 011
print(a ^ b)              # 6 (Binary: 110)

# Bitwise NOT (~)
a = 5   # Binary: 101
print(~a)                 # -6 (two's complement)

# Left Shift (<<)
a = 5   # Binary: 101
print(a << 1)             # 10 (Binary: 1010)
print(a << 2)             # 20 (Binary: 10100)

# Right Shift (>>)
a = 20  # Binary: 10100
print(a >> 1)             # 10 (Binary: 1010)
print(a >> 2)             # 5 (Binary: 101)
```

### Practical Bitwise Applications
```python
# Check if a number is even (using bitwise AND)
number = 10
is_even = (number & 1) == 0
print(is_even)            # True

# Swap two numbers without temporary variable
a = 5
b = 3
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)               # 3, 5

# Check if a number is power of 2
number = 16
is_power_of_2 = (number & (number - 1)) == 0 and number != 0
print(is_power_of_2)      # True
```

## Assignment Operators

### Basic Assignment
```python
# Simple assignment
x = 10

# Compound assignment operators
x += 5    # x = x + 5
x -= 3    # x = x - 3
x *= 2    # x = x * 2
x /= 4    # x = x / 4
x //= 2   # x = x // 2
x %= 3    # x = x % 3
x **= 2   # x = x ** 2
```

## Operator Precedence

### Precedence Hierarchy (Highest to Lowest)
```python
# 1. Parentheses
result = (2 + 3) * 4    # 20

# 2. Exponentiation
result = 2 ** 3 * 4     # 32 (not 4096)

# 3. Unary operators (+, -, ~)
result = -2 ** 2         # -4 (not 4)

# 4. Multiplication, Division, Floor Division, Modulus
result = 10 + 2 * 3      # 16 (not 36)

# 5. Addition, Subtraction
result = 10 - 2 + 3      # 11 (left to right)

# 6. Bitwise Shift
result = 1 << 2 + 1      # 8 (not 4)

# 7. Bitwise AND
result = 5 & 3 | 2       # 2

# 8. Bitwise XOR
result = 5 ^ 3 & 2       # 7

# 9. Bitwise OR
result = 5 | 3 & 2       # 5

# 10. Comparison operators
result = 5 > 3 and 2 < 4 # True

# 11. Logical NOT
result = not True or False # False

# 12. Logical AND
result = True and False or True # True

# 13. Logical OR
result = False or True and False # False

# 14. Assignment
x = 5 + 3 * 2            # 11
```

### Complex Expression Examples
```python
# Complex expression with multiple operators
result = 2 + 3 * 4 ** 2 / 8 - 1
# Step by step:
# 4 ** 2 = 16
# 3 * 16 = 48
# 48 / 8 = 6
# 2 + 6 = 8
# 8 - 1 = 7
print(result)            # 7

# Using parentheses for clarity
result = (2 + 3) * (4 ** 2) / (8 - 1)
# Step by step:
# 2 + 3 = 5
# 4 ** 2 = 16
# 8 - 1 = 7
# 5 * 16 = 80
# 80 / 7 = 11.428...
print(result)            # 11.428...
```

## Identity and Membership Operators

### Identity Operators (is, is not)
```python
# Check if two variables refer to the same object
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)            # True (same object)
print(a is c)            # False (different objects, same content)
print(a == c)            # True (same content)

# None comparison
x = None
print(x is None)         # True
print(x is not None)     # False
```

### Membership Operators (in, not in)
```python
# String membership
text = "Hello World"
print("Hello" in text)   # True
print("hello" in text)   # False (case sensitive)
print("Python" not in text) # True

# List membership
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)      # True
print(6 in numbers)      # False
print(6 not in numbers)  # True

# Dictionary membership (checks keys)
person = {"name": "John", "age": 30}
print("name" in person)  # True
print("John" in person)  # False (checks keys, not values)
```

## Senior-Level Concepts: Operator Overloading

### Understanding Operator Overloading
```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Overload + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Overload - operator
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    # Overload * operator (scalar multiplication)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # String representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
v1 = Vector(3, 4)
v2 = Vector(1, 2)

result = v1 + v2
print(result)            # Vector(4, 6)

result = v1 - v2
print(result)            # Vector(2, 2)

result = v1 * 2
print(result)            # Vector(6, 8)
```

## Practical Examples

### Example 1: Calculator Function
```python
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Division by zero"
    elif operation == '%':
        return a % b
    elif operation == '**':
        return a ** b
    else:
        return "Invalid operation"

print(calculator(10, 5, '+'))   # 15
print(calculator(10, 5, '/'))   # 2.0
print(calculator(10, 0, '/'))   # Division by zero
```

### Example 2: Grade Calculator
```python
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

student_score = 85
grade = calculate_grade(student_score)
print(f"Score: {student_score}, Grade: {grade}")
```

### Example 3: Number Properties Checker
```python
def check_number_properties(number):
    properties = {
        'positive': number > 0,
        'negative': number < 0,
        'zero': number == 0,
        'even': number % 2 == 0,
        'odd': number % 2 != 0,
        'prime': is_prime(number)
    }
    return properties

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(check_number_properties(7))
print(check_number_properties(12))
```

## Common Mistakes to Avoid

1. **Confusing = with ==**
```python
if x = 5:    # Error: assignment in condition
if x == 5:   # Correct: comparison
```

2. **Operator precedence issues**
```python
result = 2 + 3 * 4     # 14 (not 20)
result = (2 + 3) * 4   # 20 (use parentheses)
```

3. **Division by zero**
```python
result = 10 / 0        # Error: ZeroDivisionError
if denominator != 0:
    result = 10 / denominator
```

4. **Floating point precision**
```python
result = 0.1 + 0.2     # 0.30000000000000004 (not exactly 0.3)
```

## Key Takeaways
- Arithmetic operators follow standard mathematical rules
- Comparison operators return boolean values
- Logical operators use short-circuit evaluation
- Bitwise operators work on binary representations
- Operator precedence determines evaluation order
- Use parentheses for clarity in complex expressions
- Identity operators check object identity, not equality
- Membership operators test for sequence membership
- Operator overloading allows custom behavior for classes

## Interview Preparation Notes
- **Common interview questions**: Operator precedence, short-circuit evaluation, bitwise operations
- **Practice**: LeetCode problems involving bit manipulation
- **Advanced**: Operator overloading, custom classes with operators
- **System design**: Understanding operator behavior in distributed systems
