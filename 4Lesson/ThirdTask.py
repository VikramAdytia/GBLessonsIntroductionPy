"""
Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
Пример:
- Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]
"""

import random


def non_repeating_elements(n):

    random_list = []

    for i in range(n):
        random_list.append(random.randint(0, 10))

    print(random_list)

    processed_list = []

    for i in random_list:
        if random_list.count(i) == 1:
            processed_list.append(i)

    print(processed_list)


non_repeating_elements(10)

