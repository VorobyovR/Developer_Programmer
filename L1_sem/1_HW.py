# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

'''week_day = int(input("Please input the number of the day of week: "))
if week_day in range(1, 5+1):
    print(f'- {week_day} -> No. It is working day')
elif week_day in range(6, 7+1):
    print(f'- {week_day} -> Yes. It is weekend')
else:
    print('Error. Please input right number')'''

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

'''x = bool(0)
y = bool(0)
z = bool(0)
list_first = [x, y, z]

x = bool(not 1)
y = bool(not 1)
z = bool(not 1)
list_second = [x, y, z]

result = list_first == list_second
print(result)
print()

for i in range(len(list_first)):
    list_first[i] = bool(1)
    result = list_first == list_second
    print(result)
    print(list_first)

list_first_check = list_first[:]
list_first_check[1] = bool(0)
result = list_first_check == list_second
print(result)
print(list_first_check)

for i in range(len(list_first)):
    list_first[i] = bool(0)
    result = list_first == list_second
    print(result)
    print(list_first)

list_first[1] = bool(1)
result = list_first == list_second
print(result)
print(list_first)'''

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

from random import randint

'''x = randint(-100, 100+1)
y = randint(-100, 100+1)
if x != 0 and y != 0:
    if x > 0 and y > 0:
        print(f" x = {x}; y = {y} -> 1 section")
    elif x < 0 and y > 0:
        print(f" x = {x}; y = {y} -> 2 section")
    elif x < 0 and y < 0:
        print(f" x = {x}; y = {y} -> 3 section")
    elif x > 0 and y < 0:
        print(f" x = {x}; y = {y} -> 4 section")
else:
    print('Error')'''

# 4.Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

'''section = int(input('Input section number: '))

if section == 1:
    print(f'section = {section} -> (x; y)')
elif section == 2:
    print(f'section = {section} -> (-x; y)')
elif section == 3:
    print(f'section = {section} -> (-x; -y)')
elif section == 4:
    print(f'section = {section} -> (x; -y)')'''

# 5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x_1 = float(input('X for first point: '))
y_1 = float(input('Y for first point: '))
x_2 = float(input('X for second point: '))
y_2 = float(input('Y for second point: '))
A_B_distance = round(((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5, 2)
print(f'A ({x_1},{y_1}); B ({x_2},{y_2}) -> {A_B_distance}')