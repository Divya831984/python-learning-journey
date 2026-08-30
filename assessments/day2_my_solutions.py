a = 15
b = 4
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor division: {a} // {b} = {a // b}")
print(f"Modulous: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")



age = 25
score = 85
name = "Alice"
print(f"Age is more than 18 : {age > 18}")
print(f"Score is between 80 and 90 : { score >= 80 and score <=90 }")
print(f"Name comes before 'Bob' alphabetically : { name < 'Bob'}")
print(f"Age is equal to 25 AND score is greater than 80 : {age == 25 and score >80 }")
print(f"Age is less than 30 OR score is greater than 90 : { age < 30 or score > 90 }")


print(f"True and False or True: {True and False or True}")
print(f"not True or not False: {not True or not False}")
print(f"True and (False or True): {True and (False or True)}")
print(f"(not True) and (not False): {(not True) and (not False)}")
print(f"False or (True and False) or True: {False or (True and False) or True}")

a = 12  # Binary: 1100
b = 10  # Binary: 1010

print(f"Calculate a & b (bitwise AND) : {a & b}")
print(f"Calculate a | b (bitwise OR) : {a | b}")
print(f"Calculate a ^ b (bitwise XOR) : {a ^ b}")
print(f"Calculate a << 1 (left shift by 1) : {a << 1}")
print(f"Calculate a >> 2 (right shift by 2): {a >> 2}")


print(f"2 + 3 * 4 : {(2 + (3 * 4))}")
print(f"(2 + 3) * 4 : {((2 + 3) * 4)}")
print(f"10 - 2 ** 2 * 3 : {(10 - ((2 ** 2) * 3))}")
print(f"5 + 3 * 2 ** 2 : {(5 + (3 * (2 ** 2)))}")
print(f"8 / 4 / 2 : {((8 / 4) / 2 )}")

def even_odd_number(num):
	if num == 0:
		return "Zero"
	elif(num & 1) == 0:
		return "Even"
	else:
		return "Odd"

print(even_odd_number(6))
print(even_odd_number(7))


