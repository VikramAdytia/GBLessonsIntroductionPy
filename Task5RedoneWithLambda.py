"""Задайте число. Составьте список чисел Фибоначчи,
в том числе для отрицательных индексов.

Пример:

    - для k = 8 список будет выглядеть так:
     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]"""


# def neg_fib(n):
#
#     fib1 = fib2 = 1
#     fib_list = [fib1, fib2]
#
#     for i in range(2, n):
#
#         fib1, fib2 = fib2, fib1 + fib2
#         fib_list.append(fib2)
#
#     neg_fib_list = []
#     k = len(fib_list)-1
#
#     while k != 0:
#         if k % 2:
#             neg_fib_list.append(fib_list[k]*-1)
#             k -= 1
#         else:
#             neg_fib_list.append(fib_list[k])
#             k -= 1
#
#     neg_fib_list.append(0)
#     neg_fib_list.extend(fib_list)
#
#     print(neg_fib_list)
#
#
# neg_fib(int(input()))

from functools import reduce




def neg_fib(n):

    # fib1 = fib2 = 1
    # fib_list = [fib1, fib2]
    #
    # for i in range(2, n):
    #
    #     fib1, fib2 = fib2, fib1 + fib2
    #     fib_list.append(fib2)
    #

    fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

    fib_list = fib(n)
    neg_fib_list = []
    k = len(fib_list) - 1

    while k != 0:
        if k % 2:
            neg_fib_list.append(fib_list[k]*-1)
            k -= 1
        else:
            neg_fib_list.append(fib_list[k])
            k -= 1

    # neg_fib_list.append(0)
    neg_fib_list.extend(fib_list)

    print(neg_fib_list)


neg_fib(int(input()))

