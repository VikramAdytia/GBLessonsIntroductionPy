"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:

                - A (3,6); B (2,1) -> 5,09
                - A (7,-5); B (1,-1) -> 7,21"""
import math

def distance_between_two_points_on_plane(x1,y1,x2,y2):
    print(math.sqrt((x2-x1)**2+(y2-y1)**2))

distance_between_two_points_on_plane(3,6,2,1)
