def solution(x, y, op):
	"""
	This function gets three parameters 2 numbers and an operation
	+  indicates addition
	- indicates subtraction
	* indicates multiplication
	/ indicates division
	% indicates modulus(reminder)
	"""
	if op == "+":
		return x + y
	elif op == "-":
		return x - y
	elif op == "*":
		return x * y
	elif op == "/":
		return x / y
	elif op == "%":
		return x % y
	else:
		return "Invalid operation passed."			