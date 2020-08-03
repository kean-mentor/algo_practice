"""Given an integer, return the integer with reversed digits.
Note: The integer could be either positive or negative."""


import sys


def solution(x):
    string_version = str(x)

    if string_version[0] == "-":
        return int("-" + string_version[:0:-1])
    else:
        return int(string_version[::-1])


if __name__ == '__main__':
    try:
        user_input = int(sys.argv[1])
        print(solution(user_input))
    except ValueError:
        print("Your input is not an integer.")
