# Make a program that takes a string as an argument and encodes
# it into Morse Code.
# • The program supports space and alphanumeric characters
# • An alphanumeric character is represented by dots . and dashes -
# • Complete morse characters are separated by a single space
# • A space character is represented by a slash /
# You must use a dictionary to store your morse code
# If the number of arguments is different from 1, or if the type of
# any argument is wrong, the program prints an AssertionError.

import sys

NESTED_MORSE = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
            "3": "...--", "4": "....-", "5": ".....", "6": "-....",
            "7": "--...", "8": "---..", "9": "----.", " ": "/"
        }


def morse_code(string: str) -> str:
    """
    Encode a string into Morse Code

    Parameters:
        string (str): string to encode
    Returns:
        str : The string encoded into Morse Code
    """

    string = string.upper()
    assert all(i in NESTED_MORSE for i in string), "the arguments are bad"
    return " ".join([NESTED_MORSE[i] for i in string])


def main():
    """
    Main function to parse arguments and encode the string.
    """

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        result = morse_code(sys.argv[1])
        print(result)

    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)


if __name__ == '__main__':
    main()
