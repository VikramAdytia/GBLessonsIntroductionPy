"""Задайте список из n чисел последовательности
(1 + (1/n))^n и выведите на экран их сумму.

    *Пример:*

    - Для n = 3:  {1: 2, 2: 2.25 , 3: 36.9}"""


def func(n):

    li = []

    for i in range(1, n+1):
        b = (1 + (1 / i)) ** i
        li.append(b)

    print(li)
    print(f"{n}: {sum(li)}")


func(3)
