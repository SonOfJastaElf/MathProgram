#!/usr/bin/python3

def calculate(x, y, op):
	if(op == 1):
		result = x + y
	elif(op == 2):
		result = x - y
	elif(op == 3):
		result = x * y
	elif(op == 4):
		if(y == 0):
			print("Error!  Cannot divide by zero!")
		else:
			result = x / y
	else:
		print("That's not one of the choices.")
	print(result)

print("Let's do a simple math problem.")
x = int(input("Let's have a number:"))
y = int(input("Now let's have another number:"))
print("Choose an operation.  1 for addition, 2 for subtraction, 3 for multiplication or 4 for division")
operation = int(input("What's it gonna be?"))

calculate(x, y, operation)
