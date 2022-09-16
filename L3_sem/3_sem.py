from gettext import find
from os import system
from posixpath import split
system('cls')
import random as rand
from random import randint

# list = [1,2,3]
# list1 = tuple(list)
# print(list1)


# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

'''l1 = []
s = 0
n = int(input('Input size for lis: '))
for i in range(n):
    l1.append(randint(-50,50))
print(l1)
for i in range(len(l1)):
    if i%2 != 0:
        s+=l1[i]
print(s)'''

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

'''l1 = []
l2 = []
n = int(input('Input size for lis: '))
for i in range(n):
    l1.append(randint(-10,10))
print(l1)
for i in range((len(l1)+1)//2):
    print(f'{l1[i]} * {l1[-1-i]}')
    c = l1[i] * l1[-1-i]
    print(c)
    l2.append(c)
print(l2)'''

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''l1 = []
# l2 = []
n = int(input('Input size for lis: '))
for i in range(n):
    l1.append(round(rand.random() * 10 ** rand.randint(0,3), 2))
min = l1[0]%1
max = l1[0]%1
for i in range(1, len(l1)):
    if l1[i]%1 > 0 and l1[i]%1 < min:
        min = l1[i]%1
    if l1[i]%1 > max:
        max = l1[i]%1
result = round(max - min, 2)
print(f'{l1} => {result}')'''
# ---------------------------------------------------------------------

'''def num(a:int, b:int):
    c = a+b
    return c

a = int(input())
b = int(input())
print(num(a, b))'''
# -----------------------------------------------------------------------

'''num = input("Input number: ")
print(''.join(list(filter(lambda char: char.isdigit(), num))))'''

# ---------------------------------------------------------------

# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['апап4', 'fdgg3', 'fgdf', '6', 'fg24'] - ищем 24 - найдено на 4 индексе

'''def leave_only_number(st): # функция, которая оставляет тоько числа в строке:
    result = ''
    for i in st:
        if ord(i) > ord('/') and ord(i) < ord(':'):
            result+=i
    return result

num = input('Input a number: ')
list = ['апап4', 'fdgg3', 'fgdf', '6', 'fg24']
ind = 0
for i in list:
    t_el = leave_only_number(i)
    if num =in t_el:
        print(f'{list} - ищем {num} - найдено на {ind} индексе')
    ind+=1'''

# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

'''st = 'йцу'
n_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]

ind = 0
sh = 0
# m_ind = 0

for i in n_list:

    if i == st and sh < 2:
        sh += 1
        m_ind = ind
    ind += 1

if sh != 0:
    print(f'{n_list} - ищем: {st}, ответ {m_ind} индексе')
else:
    print(f'{n_list} - ищем: {st}, ответ: -1')'''
    
# 3.Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Input a number: "))
d = {}
for i in range(1, n+1):
    d[i] = 3 * i + 1
    i+=1
print(d)



