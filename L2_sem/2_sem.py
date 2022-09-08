from copy import copy
from random import randint, random

'''nun_first = int(input('Input a new number: '))
nun_first_copy = copy(nun_first)
num_second = 0
while nun_first_copy != 0:
    num_second = num_second * 10 + (nun_first_copy % 10)
    nun_first_copy //= 10
print(nun_first)
print(num_second)
if nun_first == num_second:
    print('Polindrom')
else:
    print('Not Polindrom')'''


'''for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'x={x}, y={y}, z={z}')
print(not (x or y or z) == (not x and not y and not z))'''


# 1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:    
# - Для N = 5: 1, -3, 9, -27, 81

'''num = int(input('N = '))
for i in range(num):
    print(f'{(-3)**i}', end = ' ')'''


# 2.Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: [4, 7, 10, 13, 16, 19]

'''num = int(input('N = '))
list = []
for el in range(1, num+1):
    list.append(3*el+1)
print(list)'''

#  3.Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

'''text_1 = input('First text: ')
text_2 = input('Second text: ')
count = 0
for i in range(len(text_1)):
    print(text_1[i:i+len(text_2)])
    if text_1[i:i+len(text_2)] == text_2:
        count+=1
print(count)'''

text_1 = input('First text: ')
text_2 = input('Second text: ')
count = 0
while text_1.find(text_2) != -1:
    x = text_1.find(text_2)
    text_1 = text_1[x+1:]
    count+=1
print(count)