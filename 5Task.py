"""Реализуйте алгоритм перемешивания списка.
Реализуйте алгоритм нахождения(генерации) рандомного(случайного) числа.
(Не используя библиотеки связанные с рандомом)
"""

import time

# https://en.wikipedia.org/wiki/Linear_congruential_generator


def x():
    a = 1664525
    m = 2 ^ 32
    c = 1013904223
    g = time.time()
    return (a*g + c) % m


print(x())
