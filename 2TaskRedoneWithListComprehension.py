"""Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""


# def fact(n):
#
#     f = 1
#     l = []
#
#     # for i in range(1, n+1):
#     #     f *= i
#     #     l.append(f)
#     l=[];  l=[l[-1] for x in range(1,n+1) if not l.append(x*l[-1] if l else 1)]
#
#     print(l)
#
# 
# fact(4)

l=[];  l=[l[-1] for x in range(1,4+1) if not l.append(x*l[-1] if l else 1)]
print(l)