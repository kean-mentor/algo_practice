"""For a given sentence, return the average word length.
Note: Remember to remove punctuation first."""


import re


def solution(x):
    words = re.findall(r"\w+", x)
    return sum([len(w) for w in words]) / len(words)


if __name__ == '__main__':
    first_input = "Hi all, my name is Tom...I am originally from Australia."
    second_input = "I need to work very hard to learn more about algorithms in Python!"

    print(f'{solution(first_input):.2f}')
    print(f'{solution(second_input):.2f}')
