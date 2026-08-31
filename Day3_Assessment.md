# Day 3 Assessment - Control Flow (30 Minutes)

## Instructions
- Complete all exercises in order
- Time limit: 30 minutes
- Write your solutions in Python
- No external resources allowed during assessment

## Exercise 1: Basic if Statement (5 minutes)
Write a program that:
- Takes a number as input
- Checks if the number is positive
- If positive, print "The number is positive"
- Test with both positive and negative numbers

## Exercise 2: if-else Statement (5 minutes)
Write a program that:
- Takes a number as input
- Checks if the number is even or odd
- Prints "Even" if even, "Odd" if odd
- Use the modulo operator (%) for the check

## Exercise 3: if-elif-else Chain (5 minutes)
Write a program that:
- Takes a score (0-100) as input
- Assigns grades: A (90+), B (80+), C (70+), D (60+), F (<60)
- Prints the grade
- Test with different scores

## Exercise 4: Nested Conditions (5 minutes)
Write a program that:
- Takes age and has_license as input
- Checks if person can drive:
  - Must be 18 or older
  - Must have a license
- Prints appropriate message for each case

## Exercise 5: Logical Operators (5 minutes)
Write a program that:
- Takes username, password, and is_active as input
- Checks login conditions:
  - Username must be "admin"
  - Password must be "secret123"
  - Account must be active (is_active = True)
- Prints "Login successful" or appropriate error message

## Exercise 6: Ternary Operator (5 minutes)
Write a program that:
- Takes a temperature as input
- Uses ternary operator to assign "hot" if temp > 30, "moderate" otherwise
- Prints the result
- Also create a similar check for even/odd using ternary

## Bonus Challenge (Time Permitting)
Create a simple ATM program that:
- Takes PIN, balance, and withdrawal amount as input
- Checks if PIN is correct ("1234")
- Checks if withdrawal amount is available
- Updates balance if successful
- Handles insufficient funds and wrong PIN cases
- Prints final balance or error message

## Self-Check
After completing the assessment, ask yourself:
- Can I write basic if statements correctly?
- Do I understand if-else and if-elif-else chains?
- Can I use logical operators in conditions?
- Did I handle all possible cases in my conditions?
- Did I complete all exercises within 30 minutes?

## Solutions (Check after completing)

### Exercise 1 Solution
```python
number = 5

if number > 0:
    print("The number is positive")

# Test with negative
number = -3
if number > 0:
    print("The number is positive")
else:
    print("The number is not positive")
```

### Exercise 2 Solution
```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### Exercise 3 Solution
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

print(f"Score: {score}, Grade: {grade}")
```

### Exercise 4 Solution
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

### Exercise 5 Solution
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

### Exercise 6 Solution
```python
temperature = 35
weather = "hot" if temperature > 30 else "moderate"
print(f"Temperature: {temperature}, Weather: {weather}")

number = 8
parity = "even" if number % 2 == 0 else "odd"
print(f"Number: {number}, Parity: {parity}")
```

### Bonus Challenge Solution
```python
def atm_machine(pin, balance, amount):
    correct_pin = "1234"
    
    if pin == correct_pin:
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: ${balance}")
        else:
            print("Insufficient funds")
    else:
        print("Wrong PIN")

# Test cases
atm_machine("1234", 1000, 500)   # Success
atm_machine("1234", 1000, 1500)  # Insufficient funds
atm_machine("9999", 1000, 500)   # Wrong PIN
```

## Assessment Criteria
- All exercises completed: Excellent
- 5/6 exercises completed: Good
- 4/6 exercises completed: Needs review
- Less than 4/6: Review Day 3 material before proceeding
