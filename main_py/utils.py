import random


def sign():
    a = random.randint(0, 2)
    if a == 0:
        return 1
    else:
        return -1


def choose_from_list(in_list):
    num = len(in_list)
    a = random.randint(0, num-1)
    return in_list[a]
