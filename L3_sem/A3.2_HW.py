from os import system
system('cls')
import random as rand
from random import randint

import fun as check

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def create_list(size: int):
    list = []
    for i in range(size):
        list.append(randint(-10,10))
    return list
def multiplication_couples(list):
    list_2 = []
    for i in range((len(list)+1)//2):
        c = list[i] * list[-1-i]
        list_2.append(c)
    return list_2

print("Input a number:")
n = check.CheckNumber()
list_res = create_list(n)
multiplication_res = multiplication_couples(list_res)
print(f'{list_res} => {multiplication_res}')