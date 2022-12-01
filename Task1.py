"""Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.

Пример:

    - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""


import random

random_list = []
sum_o_uev_i_rl = 0

for i in range(5):
    n = random.randint(1, 25)
    random_list.append(n)

print(random_list)

for j in range(len(random_list)):
    if j % 2:
        sum_o_uev_i_rl += random_list[j]

print(sum_o_uev_i_rl)
