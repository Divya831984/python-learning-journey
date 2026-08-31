# Day 3 Assessment - My Solutions
# Write your code below for each exercise

# Exercise 1: Basic if Statement (5 minutes)
# Write a program that:
# - Takes a number as input
# - Checks if the number is positive
# - If positive, print "The number is positive"
# Test with both positive and negative numbers

# Write your code here:

n = 5 
if n>0:
	print(f"Number {n} is positive")
else:
	print(f"Number {n} is negative")

n = -3
if n>0:
	print(f"Number {n} is positive")
else:
	print(f"Number {n} is negative")


n = 8
if(n % 2 == 0):
	print(f"Number {n} is even")
else:
	print(f"Number {n} is odd")
	

score = 85
if(score > 90):
	print("Grade A")
elif(score > 80 and score <90):
	print("Grade B")
elif(score > 70 and score <80):
	print("Grade C")
elif(score > 60 and score <70):
	print("Grade D")
elif(score < 60):
	print("Grade F")

score = 60
if(score > 90):
	print("Grade A")
elif(score > 80 and score <90):
	print("Grade B")
elif(score > 70 and score <80):
	print("Grade C")
elif(score > 60 and score <70):
	print("Grade D")
elif(score < 60):
	print("Grade F")


age = 18
has_license = True

if(age >= 18 and has_license):
	print("You are eligible to drive")
else:
	print("You are not eligible to drive")

is_active = True
username = "admin"
password = "secret123"

if(username eq "admin" and password eq "secret123" and is_active):
	print("Login successful")
else:
	print("Login unsuccessful")