"""Напишите программу, которая найдёт произведение пар чисел
 списка. Парой считаем первый и последний элемент,
 второй и предпоследний и т.д.

Пример:

    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]"""

import random

random_list = []
sum_o_sides_rl = []

for i in range(5):
    n = random.randint(1, 25)
    random_list.append(n)

print(random_list)

for j in range((len(random_list))//2 + (len(random_list)) % 2):
    k = -(j+1)
    sum_o_sides_rl.append(random_list[j] * random_list[k])

print(sum_o_sides_rl)
