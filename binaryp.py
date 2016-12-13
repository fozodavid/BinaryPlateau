import math

MAXIMUM = 2**32
MINIMUM = 1


def solution(n):
    if not isinstance(n, int):
        raise ValueError
    if n > MAXIMUM or n < MINIMUM:
        raise ValueError

    string = bin(n)[2:]
    plateaus = string.split('0')
    return max(map(len, plateaus))

if __name__ == '__main__':
    inputlist = list(map(int, (input().split())))
    for n in inputlist:
        print(solution(n))
