from os import system
system('cls')
import random as rand
from random import randint

import fun as check


# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list(size: int):
    list = []
    for i in range(size):
        list.append(randint(-50,50))
    return list
def sum_elem(list):
    sum = 0
    for i in range(len(list)):
        if i%2 != 0:
            sum+=list[i]
    return sum

print("Input a number:")
n = check.CheckNumber()
list_res = create_list(n)
sum_res = sum_elem(list_res)
print(f'{list_res} -> result: {sum_res}')