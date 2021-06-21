import numpy as np
import random


def getpos(n):
    return (n // 3) * 3


def getsq(arr, x, y):
    return arr[getpos(x):getpos(x) + 3, getpos(y):getpos(y) + 3]


if __name__ == '__main__':
    arr: np.ndarray = np.arange(81).reshape(9, 9)
    """"# print(arr)
    for c in range(10):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        print(arr)
        print(arr[x, y])
        print(getsq(arr, x, y))"""
