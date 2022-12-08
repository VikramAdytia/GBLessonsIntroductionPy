"""Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
 За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
 Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом

"""""
import random

# while candy > 83:
#     candy -= 28
#     print(candy)


def turn(candy, player):
    print(candy)
    if candy != 0:
        if player:
            print("Сколько конфет нужно взять ?"
                  "За один ход можно забрать не более чем 28 конфет.")
            candy_take = int(input())
            if candy_take > 28:
                exit("За один ход можно забрать не более чем 28 конфет."
                     'cheater')
            candy -= candy_take
            player = not player
            turn(candy, player)
        else:
            if candy > 83:
                candy -= 28
                player = not player
                turn(candy, player)
            elif candy >55:
                candy -= random.randint(1, 25)
                player = not player
                turn(candy, player)
            elif candy >28:
                candy -= candy - 29
                player = not player
                turn(candy, player)
            else: # candy <= 28
                candy -= candy
                turn(candy, player)
    else: # candy = 0
        if player:
            print("А не слипнется?")
        else: # bot is winner
            print("не слипнется")



turn(121, True)