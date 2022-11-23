
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def format_checker ():
        try:
            day_of_the_week = int(input())
            return day_of_the_week
        except ValueError:
            print("принимает на вход цифру \n"
                  "https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%84%D1%80%D1%8B")


def is_weekends():
    print('''программа, которая принимает на вход цифру,
         обозначающую день недели, и проверяет,
         является ли этот день выходным''')
    try:
        day_of_the_week = format_checker()
        if 8 > day_of_the_week > 5:
            return print(f"- {day_of_the_week} -> да")
        else:
            return print(f"- {day_of_the_week} -> нет")
    except TypeError:
        print("обозначающую день недели")

is_weekends()
