"""Given a string, find the first non-repeating character in it and return its
index. If it doesn't exist, return -1.
Note: all the input strings are already lowercase."""


def solution(x):
    for idx, c in enumerate(x):
        if x.count(c) == 1:
            return idx
    return -1

    # Solution if I can't use string.count() function.
    # for idx, c in enumerate(x):
    #     cnt = 0
    #     for k in x:
    #         if k == c:
    #             cnt += 1
    #     if cnt == 1:
    #         return idx
    # return -1

    # Solution with collections.Counter
    # import collections

    # counts = collections.Counter(x)
    # print(counts)
    # for idx, c in enumerate(x):
    #     if counts[c] == 1:
    #         return idx
    # return -1


if __name__ == '__main__':
    print(solution('barbados'))  # 2
    print(solution('tomato'))  # 2
    print(solution('newspaper'))  # 0
    print(solution('abba'))  # -1
