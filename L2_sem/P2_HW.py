from os import system
system('cls')
from copy import copy
from datetime import datetime, date, time
import datetime


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

'''num_orig = input('Input a number: ')
suma = 0
for i in num_orig:
    num_orig = num_orig.replace('-', '')
    num_orig = num_orig.replace('.', '')
for i in num_orig:
    suma += int(i)
print(f'{num_orig} -> {suma}')'''


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

'''num = int(input('Input a number: '))
multiplication = 1
list = []
for i in range(num):
    i+=1
    multiplication*=i
    list.append(multiplication)
print(f'N = {num}, then {list}')'''

# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа

'''def polindrom(num):
    num_first_copy = copy(num)
    num_second = 0
    num_final = 0
    while num_first_copy != 0:
        num_second = num_second * 10 + (num_first_copy % 10)
        num_first_copy //= 10
    if num == num_second:
        return print(f'Polindrom -> {num}')
    else:
        num_final = num + num_second
        return polindrom(num_final)

polindrom(num = int(input('Input a new number: ')))'''

# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

num = int(input('Input a number > 0 and < 1000: ')) #Диапазон от 0 до 1000
nowTime_sec = datetime.datetime.now ().microsecond
if 0<num<1000:
    while num < nowTime_sec:
        nowTime_sec //= 10
    print(f'result = {nowTime_sec}')
else:
    print('Error. Input right number: ')
