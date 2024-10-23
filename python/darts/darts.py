from math import sqrt

def score(x, y):
    pos = sqrt((abs(x) ** 2 + abs(y) **2))

    if pos > 10:
        return 0

    if pos > 5:
        return 1

    if pos > 1:
        return 5

    if pos >= 0 :
        return 10
