import random


def sign():
    a = random.randint(0, 2)
    if a == 0:
        return 1
    else:
        return -1
