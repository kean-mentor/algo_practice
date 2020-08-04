"""Given a non-empty string s, you may delete at most one character. Judge
whether you can make it a palindrome. The string will only contain lowercase
characters a-z."""


def solution(s):
    for idx in range(len(s)):
        temp = s[:idx] + s[idx + 1:]
        if temp == temp[::-1]:
            return True
    return False


if __name__ == '__main__':
    print(solution("aa"))  # True
    print(solution("aaa"))  # True
    print(solution("aba"))  # True
    print(solution("abba"))  # True
    print(solution("abcda"))  # False
    print(solution("rakdar"))  # True
