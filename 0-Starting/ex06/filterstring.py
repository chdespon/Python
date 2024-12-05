# Create a program that accepts two arguments: a string(S), and an integer(N).
# the arguments are badfrom S that have a
# length greater than N.
# • Words are separated from each other by space characters.
# • Strings do not contain any special characters. (Punctuation or invisible)
# • The program must contain at least one list comprehension expression and one
# lambda.
# • If the number of argument is different from 2,
# or if the type of any argument is wrong,
# the program prints an AssertionError.

import sys
import ft_filter


def filter_string(string: str, n: int) -> None:
    """
    Filter a string

    Parameters:
        string (str): string to filter
        n (int): length of the word to filter
    Returns:
        None
    Result:
        print a list of words from S that have a length greater than N
    """

    # print(ft_filter.ft_filter(42, string.split()))
    print(ft_filter.ft_filter(lambda word: len(word) > n, string.split()))


def main():
    """
    Main function to parse arguments and filter the string
    """

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        try:
            n = int(sys.argv[2])
            if n < 0:
                raise ValueError
        except ValueError:
            raise AssertionError("the arguments are bad")
        filter_string(string, n)

    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)


if __name__ == '__main__':
    main()
