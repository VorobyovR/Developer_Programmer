from os import system
system('cls')
import utils as check
import random
from random import randint

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# 1. Input

print('Input numbers: ')
list_first = list(input() for i in range(10))
list_second = list(set(list_first))
print(f'{list_first} -> {list_second}')

# 2. Random

'''list_first = list(randint(1, 10) for i in range(20))
list_second = list(set(list_first))
print(f'{list_first} -> {list_second}')'''