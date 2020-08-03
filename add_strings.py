"""Given two non-negative integers num1 and num2 represented as string, return
the sum of num1 and num2. You must not use any built-in BigInteger library or
convert the inputs to integer directly.

Notes:
- Both num1 and num2 contains only digits 0-9.
- Both num1 and num2 does not contain any leading zero.
"""


def solution(num1, num2):

    def convert_str(numstr):
        summary = 0
        length = len(numstr)

        for idx, c in enumerate(numstr):
            summary += (ord(c) - ord('0')) * pow(10, length - 1 - idx)

        return summary

    return convert_str(num1) + convert_str(num2)


if __name__ == '__main__':
    num1 = '3489'
    num2 = '217'

    print(solution(num1, num2))
