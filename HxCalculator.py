"""
Title: HxCalculator
Author: n1ghTm4lz3
Description:
	Hexadecimal Calculator
"""

def main():
	while True:
		formula = input("Formula: ")
		
		if formula == "":
			exit()
		else:
			arithmetic(formula)

def message():
	print("+================================================+")
	print("|             Hexadecimal Calculator             |")
	print("|                                                |")
	print("| Input Sample: 3e8+2af / ?                      |")
	print("| Support operation:                             |")
	print("|   + => Addition                                |")
	print("|   - => Subtraction                             |")
	print("|   * => Multiplication                          |")
	print("|   / => Division                                |")
	print("|   ^ => Exclusive OR                            |")
	print("|   | => OR                                      |")
	print("|   & => AND                                     |")
	print("|   ? => Help Message                            |")
	print("+================================================+")


def arithmetic(formula):
	hex1 = "0x"
	hex2 = "0x"
	operator = ""
	result = ""

	for i in range(len(formula)):
		if formula[i] in "?+-*/^|&":
			operator = formula[i]
		else:
			hex1 += formula[i]
			continue
		hex2 += formula[i + 1:]
		break

	if operator == "?":
		message()
		return
	elif operator == "+":
		result = hex(int(hex1, 16) + int(hex2, 16))
	elif operator == "-":
		result = hex(int(hex1, 16) - int(hex2, 16))
	elif operator == "*":
		result = hex(int(hex1, 16) * int(hex2, 16))
	elif operator == "/":
		result = hex(int(hex1, 16) // int(hex2, 16))
	elif operator == "^":
		result = hex(int(hex1, 16) ^ int(hex2, 16))
	elif operator == "|":
		result = hex(int(hex1, 16) | int(hex2, 16))
	elif operator == "&":
		result = hex(int(hex1, 16) & int(hex2, 16))
	
	print(hex1 + " " + operator + " " + hex2 + " = " + result)
	print()


if __name__ == '__main__':
	message()
	main()
