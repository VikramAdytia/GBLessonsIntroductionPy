"""Напишите программу, которая будет преобразовывать
десятичное число в двоичное.

Пример:

    - 45 -> 101101
    - 3 -> 11
    - 2 -> 10"""


def dec_to_bin(dec_input):

    remember = dec_input
    converter_inside = ""
    
    while dec_input != 0:

        converter_inside += (str(dec_input % 2))
        dec_input //= 2
    
    print(remember, "->", converter_inside)



dec_to_bin(45)
