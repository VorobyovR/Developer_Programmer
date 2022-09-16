from os import system
system('cls')
import random as rand
from random import randint

import fun as check

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def diff_max_min(size: int):
    list = []
    for i in range(size):
        list.append(round(rand.random() * 10 ** rand.randint(0,3), 2))
    min = list[0] % 1
    max = list[0] % 1
    for i in range(1, len(list)):
        if list[i] % 1 > 0 and list[i] % 1 < min:
            min = list[i] % 1
        if list[i]%1 > max:
            max = list[i] % 1
    result = round(max - min, 2)
    return print(f'{list} => {result}')

numbers = diff_max_min(int(input('Input size for list: ')))