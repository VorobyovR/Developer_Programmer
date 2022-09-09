from ast import Index
from copy import copy
from random import randint, random
from datetime import datetime, date, time

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
for i in range(0, num-1):
    print(f'{(-3)**i}', end = ', ')
else:
    print(f'{(-3)**(num-1)}', end = '')'''


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

'''text_1 = input('First text: ')
text_2 = input('Second text: ')
count = 0
while text_1.find(text_2) != -1:
    x = text_1.find(text_2)
    text_1 = text_1[x+1:]
    count+=1
print(count)'''

# 4.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами

'''n = randint(10,20)
list = [randint(1, 30) for i in range(n)]
print(list)
max = max(list)
index_max = list.index(max)
min = min(list)
index_min = list.index(min)
if index_max > index_min:
    list = list[index_min+1:index_max]
elif index_max < index_min:
    list = list[index_max+1:index_min]
sum = 0
for i in list:
    sum+=i
print(f'{list} -> sum = {sum}')'''


# 5. Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10% ( 10% от наибольшего)

'''n = randint(10,20)
list = [randint(1, 30) for i in range(n)]
print(list)
max = max(list)
max1 = round(max/10 - 0.005, 2)
# print(max1)
count = 0
for i in list:
    if max - i <= max1:
        count+=1
        print(i, end=" " )
print()
print(count)'''


'''A = [randint(1, 30) for i in range(10)]
max = A[0]
for i in A[1:]:
    if i > max:
        max = i
count = 0
for i in A:
    if max*0.9 < i and i !=max:
        count += 1
print(count)'''

# Выход из цикла

# number = 23
# running = True
# while running:
#     guess = int(input('Введите целое число : '))
#     if guess == number:
#            print('Поздравляю, вы угадали.')
#            running = False # это останавливает цикл while
#     elif guess < number:
#           print('Нет, загаданное число немного больше этого.')
#     else:
#           print('Нет, загаданное число немного меньше этого.')
# else:
#      print('Цикл while закончен.')
# # Здесь можете выполнить всё что вам ещё нужно
# print('Завершение.')

while True:
    s = input('Введите что-нибудь : ')
    if s == 'c':
        break
    print('Длина строки:', len(s))
print('Завершение')