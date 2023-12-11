# This time you have to make a real autonomous program, with a main, which takes
# a single string argument and displays the sums of its upper-case characters, lower-case
# characters, punctuation characters, digits and spaces.
# • If None or nothing is provided, the user is prompted to provide a string.
# • If more than one argument is provided to the program, print an AssertionError.

import sys

# compt carac

def compt_carac(string: str) -> None:
	"""
	Count the number of characters in a string

	Parmeters:
		string (str): string to count
	Returns:
		None
	result:
		print the number of characters in the string
	"""
	
	upper = 0
	lower = 0
	punct = 0
	digit = 0
	space = 0
	for i in string:
		if i.isupper():
			upper += 1
		elif i.islower():
			lower += 1
		elif i.isdigit():
			digit += 1
		elif i.isspace():
			space += 1
		else:
			punct += 1
	print("The texte contains: " + str(len(string)) + " characters")
	print("\t- " + str(upper) + " upper letters")
	print("\t- " + str(lower) + " lower letters")
	print("\t- " + str(punct) + " punctuation marks")
	print("\t- " + str(space) + " spaces")
	print("\t- " + str(digit) + " digits")

if __name__ == '__main__':
	try:
		if len(sys.argv) > 2:
			raise AssertionError("more than one argument is provided")
		if len(sys.argv) == 1:
			print("What is the text to count?")
			string = sys.stdin.readline()
			if not string:
				print("No text provided")
				sys.exit(0)
		else:
			string = sys.argv[1]
		assert type(string) == str, "argument is not a string"
		compt_carac(string)
	except AssertionError as e:
		print("AssertionError:", e)
		sys.exit(1)
	sys.exit(0)
