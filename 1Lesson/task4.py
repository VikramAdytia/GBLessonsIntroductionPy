"""Напишите программу, которая по заданному номеру четверти,
 показывает диапазон возможных координат точек в этой четверти (x и y)."""

def quarter_pos_cor (quarter):
    match quarter:
        case 1:
            print("x<0 , y>0")
        case 2:
            print("x>0 , y>0")
        case 3:
            print("x>0 , y<0")
        case 4:
            print("x<0 , y<0")

quarter_pos_cor(int(input()))
