# Day 3: Control Flow - if/else Statements

## Learning Objectives
- Master if statements for conditional execution
- Understand if-else statements for binary choices
- Learn if-elif-else chains for multiple conditions
- Practice nested conditional statements
- Use comparison operators in real scenarios
- Apply logical operators for complex conditions
- Understand ternary operators for concise code
- Complete 30-minute assessment

## What is Control Flow?

Control flow determines the order in which code statements are executed. It allows your programs to make decisions and execute different code based on conditions.

## if Statements

### Basic if Statement
```python
age = 18

if age >= 18:
    print("You are eligible to vote")
```

### How it Works:
- Python evaluates the condition
- If the condition is `True`, the indented code block executes
- If the condition is `False`, the code block is skipped
- **Indentation is crucial** - Python uses indentation to define code blocks

### Example: Temperature Check
```python
temperature = 30

if temperature > 25:
    print("It's a hot day!")
    print("Stay hydrated")
```

## if-else Statements

### Basic if-else Structure
```python
age = 15

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

### How it Works:
- If condition is `True`, execute the if block
- If condition is `False`, execute the else block
- Exactly one of the two blocks will execute

### Example: Number Check
```python
number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

## if-elif-else Chains

### Multiple Conditions
```python
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

print(f"Your grade is: {grade}")
```

### How it Works:
- Python checks conditions in order
- First `True` condition executes its block
- Remaining conditions are skipped
- If none are `True`, the else block executes

### Example: Temperature Description
```python
temperature = 15

if temperature > 30:
    description = "Very hot"
elif temperature > 20:
    description = "Warm"
elif temperature > 10:
    description = "Cool"
else:
    description = "Cold"

print(f"The weather is {description}")
```

## Nested Conditional Statements

### Nested if Statements
```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need to get a license")
else:
    print("You are too young to drive")
```

### Practical Example: Login System
```python
username = "admin"
password = "secret123"
is_active = True

if username == "admin":
    if password == "secret123":
        if is_active:
            print("Login successful")
        else:
            print("Account is inactive")
    else:
        print("Wrong password")
else:
    print("User not found")
```

## Comparison Operators in Conditions

### Using Comparison Operators
```python
# Greater than
if age > 18:
    print("Adult")

# Less than
if age < 65:
    print("Working age")

# Equal to
if status == "active":
    print("Account is active")

# Not equal to
if role != "guest":
    print("Has special permissions")

# Greater than or equal
if score >= 60:
    print("Passing grade")

# Less than or equal
if attempts <= 3:
    print("Keep trying")
```

## Logical Operators in Conditions

### Combining Conditions with and
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive alone")
```

### Combining Conditions with or
```python
day = "Saturday"
is_holiday = True

if day == "Saturday" or day == "Sunday" or is_holiday:
    print("Weekend or holiday")
```

### Combining Conditions with not
```python
is_raining = False

if not is_raining:
    print("Good weather for a walk")
```

### Complex Conditions
```python
age = 30
has_license = True
has_car = False
is_insured = True

if age >= 18 and has_license and (has_car or is_insured):
    print("Can legally drive")
```

## Ternary Operator

### Concise Conditional Expression
```python
# Traditional if-else
age = 20
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary operator (one line)
age = 20
status = "adult" if age >= 18 else "minor"
```

### How it Works:
```python
value_if_true if condition else value_if_false
```

### Practical Examples
```python
# Number check
number = 7
result = "even" if number % 2 == 0 else "odd"

# Temperature
temp = 25
weather = "hot" if temp > 30 else "moderate"

# Score evaluation
score = 85
grade = "pass" if score >= 60 else "fail"
```

## Practical Examples

### Example 1: Grade Calculator
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
print(f"Score: {student_score}, Grade: {calculate_grade(student_score)}")
```

### Example 2: ATM Machine
```python
balance = 1000
pin = "1234"
entered_pin = "1234"
amount = 500

if entered_pin == pin:
    if amount <= balance:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance}")
    else:
        print("Insufficient funds")
else:
    print("Invalid PIN")
```

### Example 3: User Authentication
```python
def authenticate_user(username, password, role):
    # Check if username exists (simplified)
    valid_users = ["admin", "user1", "user2"]
    
    if username in valid_users:
        if password == "secret123":
            if role == "admin":
                return "Admin access granted"
            else:
                return "User access granted"
        else:
            return "Wrong password"
    else:
        return "User not found"

print(authenticate_user("admin", "secret123", "admin"))
```

### Example 4: Shopping Discount
```python
def calculate_discount(amount, is_member):
    if is_member:
        if amount > 100:
            discount = 0.20  # 20% discount
        elif amount > 50:
            discount = 0.10  # 10% discount
        else:
            discount = 0.05  # 5% discount
    else:
        if amount > 200:
            discount = 0.10  # 10% discount
        else:
            discount = 0.0   # No discount
    
    final_amount = amount * (1 - discount)
    return final_amount

print(f"Member $150: ${calculate_discount(150, True)}")
print(f"Non-member $150: ${calculate_discount(150, False)}")
```

## Common Mistakes to Avoid

### 1. Forgetting Colons
```python
if age > 18  # ❌ Missing colon
    print("Adult")

if age > 18:  # ✅ Correct
    print("Adult")
```

### 2. Incorrect Indentation
```python
if age > 18:
print("Adult")  # ❌ Not indented

if age > 18:
    print("Adult")  # ✅ Properly indented
```

### 3. Using Assignment Instead of Comparison
```python
if age = 18:  # ❌ Assignment
    print("Adult")

if age == 18:  # ✅ Comparison
    print("Adult")
```

### 4. Confusing and/or Operators
```python
if age > 18 and < 65:  # ❌ Incorrect syntax
    print("Working age")

if age > 18 and age < 65:  # ✅ Correct
    print("Working age")
```

### 5. Missing else in Expected Cases
```python
if score >= 60:
    result = "pass"
# ❌ What happens if score < 60?

if score >= 60:
    result = "pass"
else:
    result = "fail"  # ✅ Handles all cases
```

## Best Practices

### 1. Use Meaningful Variable Names
```python
if user_age >= legal_voting_age:  # ✅ Clear
    print("Can vote")

if a >= 18:  # ❌ Unclear
    print("Can vote")
```

### 2. Keep Conditions Simple
```python
if age >= 18 and age < 65 and has_license and is_insured:  # Complex
    print("Can drive")

# Better: Break into logical parts
is_eligible_age = age >= 18 and age < 65
has_requirements = has_license and is_insured
if is_eligible_age and has_requirements:
    print("Can drive")
```

### 3. Use elif for Mutually Exclusive Conditions
```python
if score >= 90:
    grade = 'A'
if score >= 80:  # ❌ Will always be checked
    grade = 'B'

if score >= 90:
    grade = 'A'
elif score >= 80:  # ✅ Only checked if first condition is False
    grade = 'B'
```

### 4. Handle Edge Cases
```python
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"  # ✅ Handle edge case
```

## Key Takeaways
- Control flow allows programs to make decisions
- if statements execute code only when conditions are True
- if-else provides binary choices
- if-elif-else handles multiple conditions
- Indentation is crucial in Python
- Comparison operators (==, !=, <, >, <=, >=) are used in conditions
- Logical operators (and, or, not) combine conditions
- Nested conditions handle complex logic
- Ternary operators provide concise conditional expressions
- Always handle edge cases and error conditions

## Interview Preparation Notes
- **Common interview questions**: Nested conditions, logical operator precedence, ternary operators
- **Practice**: Writing complex conditional logic, optimizing nested conditions
- **Advanced**: Short-circuit evaluation, truthy/falsy values, conditional expressions
- **System design**: Decision trees, business logic implementation, validation strategies
