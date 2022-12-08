"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

"""
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def priming(x):
    while not is_prime(x):
        x = x//2
    return x


def factor(x):
    factors = []

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            factors.append(i)
            x //= i

    if x != 1:
        if is_prime(x):
            factors.append(x)
        else:
            x = priming(x)
            factors.append(x)

    print(factors)


factor(15684)

