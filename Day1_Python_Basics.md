# Day 1: Python Basics - Setup, Variables, and Data Types

## Learning Objectives
- Understand what Python is and why it's popular
- Set up Python development environment
- Learn about variables and variable naming
- Master basic data types (integers, floats, strings, booleans)
- Practice type conversion
- Complete 30-minute assessment

## What is Python?
Python is a high-level, interpreted programming language known for:
- **Simple syntax**: Easy to read and write
- **Versatility**: Web development, data science, AI, automation, etc.
- **Large community**: Extensive libraries and frameworks
- **Cross-platform**: Runs on Windows, Mac, Linux

## Setup Instructions

### 1. Install Python
- Download from [python.org](https://python.org)
- Choose Python 3.10+ (recommended 3.11 or 3.12)
- During installation, check "Add Python to PATH"

### 2. Verify Installation
Open command prompt/terminal and run:
```bash
python --version
```

### 3. Choose an Editor/IDE
- **VS Code** (recommended): Free, extensible, great Python support
- **PyCharm**: Powerful IDE for Python development
- **Jupyter Notebook**: Great for data science and learning

## Variables

### What are Variables?
Variables are containers for storing data values.

### Variable Naming Rules
- Must start with a letter or underscore (_)
- Can contain letters, numbers, and underscores
- Case-sensitive (name ≠ Name)
- Cannot use Python keywords (if, else, for, etc.)

### Good Naming Practices
```python
# Good variable names
user_name = "John"
total_score = 95
is_active = True

# Avoid these
x = "John"  # Not descriptive
2nd_place = "Silver"  # Can't start with number
class = "Python 101"  # 'class' is a keyword
```

## Basic Data Types

### 1. Integers (int)
Whole numbers without decimal points
```python
age = 25
count = -5
population = 1000000
```

### 2. Floats (float)
Numbers with decimal points
```python
price = 19.99
temperature = -3.5
pi = 3.14159
```

### 3. Strings (str)
Text data enclosed in quotes
```python
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multi-line string"""
```

### 4. Booleans (bool)
Logical values: True or False
```python
is_student = True
has_license = False
is_valid = True
```

## Type Conversion

Convert between data types using built-in functions:
```python
# String to integer
num_str = "42"
num_int = int(num_str)  # 42

# Integer to string
age = 25
age_str = str(age)  # "25"

# Float to integer
price = 19.99
price_int = int(price)  # 19 (truncates decimal)

# String to float
decimal_str = "3.14"
decimal_float = float(decimal_str)  # 3.14
```

## Checking Data Types
Use the `type()` function:
```python
x = 42
print(type(x))  # <class 'int'>

name = "Alice"
print(type(name))  # <class 'str'>
```

## Practical Examples

### Example 1: Personal Information
```python
name = "John Doe"
age = 30
height = 5.9
is_employed = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Employed: {is_employed}")
```

### Example 2: Simple Calculator
```python
num1 = "10"
num2 = "5"

# Convert strings to integers
num1_int = int(num1)
num2_int = int(num2)

result = num1_int + num2_int
print(f"The sum of {num1} and {num2} is {result}")
```

## Common Mistakes to Avoid

1. **Using undefined variables**
```python
print(username)  # Error: name 'username' is not defined
```

2. **Confusing assignment (=) with comparison (==)**
```python
x = 5  # Assignment
if x == 5:  # Comparison
    print("x is 5")
```

3. **Invalid type conversion**
```python
text = "hello"
num = int(text)  # Error: invalid literal for int()
```

## Key Takeaways
- Python is versatile and beginner-friendly
- Variables store data with meaningful names
- Four basic data types: int, float, str, bool
- Type conversion allows flexibility in data handling
- Always use descriptive variable names

## Next Steps
Complete the 30-minute assessment to reinforce today's concepts.
