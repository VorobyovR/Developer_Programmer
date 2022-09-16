from os import system
system('cls')
import random as rand
from random import randint

import fun as check

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def binar_calc(num):
    bin_number = ''
    while num > 0:
        bin_number = str(num % 2) + bin_number
        num //= 2
    return bin_number

print("Input a number:")
number = check.CheckNumber()
print(f'{number} -> {binar_calc(number)}')