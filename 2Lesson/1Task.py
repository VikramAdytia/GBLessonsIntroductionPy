"""Напишите программу, которая принимает на вход
вещественное число и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11
"""
"""

def sum_of_elements_in_number(focus_integer):
    sum_of_elements = 0
    if focus_integer < 1:
        while focus_integer < 1:
            sum_of_elements += focus_integer * 10
            focus_integer *= 10
    while focus_integer != 0:
        sum_of_elements += focus_integer % 10
        focus_integer //= 10

    sum_of_elements = int(sum_of_elements)
    print(sum_of_elements)

#sum_of_elements_in_number(0.56)

"""

def clean_string(string):
    cleane_string = string.replace(".", "")
    cleaned_string = cleane_string.replace("-","")
    if not cleaned_string.isdigit():
        print("принимает на вход вещественное число")
        exit()
    return cleaned_string

print(sum(map(int,str(clean_string("-0.212345")))))
