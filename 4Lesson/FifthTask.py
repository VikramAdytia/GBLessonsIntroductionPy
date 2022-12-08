"""
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*

*Доп задание: значения коэффициентов от -100 до 100
*Доп задание: для разного размера уравнения
"""
import FourthTask


def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num


def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    len_st = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        lst.append(int(st[-1]))
        len_st -= 1
        k = 1
    i = 1
    ii = len_st - 1
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


FourthTask.write_file("file1.txt", FourthTask.create_str(FourthTask.create_mn(int(input("Введите натуральную степень для первого файла k = ")))))
FourthTask.write_file("file2.txt", FourthTask.create_str(FourthTask.create_mn(int(input("Введите натуральную степень для второго файла k = ")))))

with open('file1.txt', 'r') as data_read:
    st1 = data_read.readlines()
with open('file2.txt', 'r') as data_read:
    st2 = data_read.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = calc_mn(st1)
lst2 = calc_mn(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
FourthTask.write_file("file_res.txt", FourthTask.create_str(lst_new))
with open('file_res.txt', 'r') as data_read:
    st3 = data_read.readlines()
print(f"суммa многочленов {st3}")