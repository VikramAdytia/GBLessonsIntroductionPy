"""Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу между максимальным
 и минимальным значением дробной части элементов.

Пример:

    - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19"""

import random

random_list = []

for i in range(5):
    n = round(random.uniform(1.5, 25.5), 2)
    random_list.append(n)

rounded_random_list = []

for i in range(len(random_list)):
    t = round((random_list[i]), 2)
    rounded_random_list.append(t)

min_rounded_random_list = rounded_random_list[0]
max_rounded_random_list = rounded_random_list[0]

for i in range(len(rounded_random_list)):

    if rounded_random_list[i] > max_rounded_random_list:
        max_rounded_random_list = rounded_random_list[i]
    elif rounded_random_list[i] < min_rounded_random_list:
        min_rounded_random_list = rounded_random_list[i]

print(random_list, "=>", max_rounded_random_list - min_rounded_random_list)
