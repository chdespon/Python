# Create a script that takes a number as argument, checks whether it is odd or even,
# and prints the result.
# If more than one argument is provided or if the argument is not an integer, print an
# AssertionError.

import sys

def is_int(number: any, type: type) -> bool:
	try:
		type(number)
	except ValueError:
		return False
	return True

def whatis(number: int) -> None:
	if number % 2 == 0:
		print("I'm Even")
	else:
		print("I'm Odd")

if __name__ == "__main__":
	try:
		if len(sys.argv) > 2:
			raise AssertionError("more than one argument is provided")
		if len(sys.argv) == 1:
			sys.exit(0)
		assert is_int((sys.argv[1]), int), "argument is not an integer"
		whatis(int(sys.argv[1]))
	except AssertionError as e:
		print("AssertionError:", e)
		sys.exit(1)
	sys.exit(0)