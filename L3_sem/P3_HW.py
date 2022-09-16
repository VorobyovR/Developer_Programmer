from os import system

system('cls')
import random as rand
from random import randint

import fun as check

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Variant 1

'''def create_list(size: int):
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
print(f'{list_res} -> result: {sum_res}')'''

# Variant 2
'''list = [randint(-50, 50) for i in range(1, 10) if i % 2 != 0]
print(sum(list))'''

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

'''def create_list(size: int):
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
print(f'{list_res} => {multiplication_res}')'''

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

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

'''def binar_calc(num):
    bin_number = ''
    while num > 0:
        bin_number = str(num % 2) + bin_number
        num //= 2
    return bin_number

print("Input a number:")
number = check.CheckNumber()
print(f'{number} -> {binar_calc(number)}')'''

# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

'''def fibonacci_negafibonacci(n: int):
    l_one = []
    l_two = []
    for i in range(0,n):
        if i == 0:
            l_one.append(0)
        elif 1 <= i <= 2:
            l_one.append(1)
            if i == 1:
                l_two.append(1)
            if i == 2:
                l_two.append(-1)
        else:
            l_one.append(l_one[i-2]+l_one[i-1])
            l_two.append(((-1)**(i+1))*l_one[-1])
    
    l_two = l_two[::-1]
    final = l_two + l_one
    return final

print("Input a number:")
n = check.CheckNumber()
print(fibonacci_negafibonacci(n))'''
