# Create a program that accepts two arguments: a string(S), and an integer(N).
# The program should output a list of words from S that have a length greater than N.
# • Words are separated from each other by space characters.
# • Strings do not contain any special characters. (Punctuation or invisible)
# • The program must contain at least one list comprehension expression and one
# lambda.
# • If the number of argument is different from 2, or if the type of any argument is wrong,
# the program prints an AssertionError.

import sys

def filter_string(string: str, n: int) -> None:
	"""
	Filter a string

	Parameters:
		string (str): string to filter
		n (int): length of the word to filter
	Returns:
		None
		result:
			print a list of words from S that have a length greater than N
	"""
	try:
		assert type(string) == str, "argument is not a string"
		assert type(n) == int, "argument is not an integer"
		assert n >= 0, "argument is not positive"
		print([i for i in string.split() if (lambda mot: len(mot) > n)(i)])
	except AssertionError as e:
		print("AssertionError:", e)
		sys.exit(1)

if __name__ == '__main__':
	try:
		if len(sys.argv) != 3:
			raise AssertionError("the arguments are bad")
		filter_string(sys.argv[1], int(sys.argv[2]))
	except AssertionError as e:
		print("AssertionError:", e)
		sys.exit(1)
	sys.exit(0)