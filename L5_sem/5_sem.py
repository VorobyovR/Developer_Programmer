from os import system
system('cls')
from random import randint
from math import factorial

'''file_app_information = open('student_information.txt', 'w+', encoding='utf-8') # encoding='utf-8' позволяет записывать кирилицу
file_app_information.write('Ангела Меркель 5' '\nАндрей Валетов 5' '\nФредди Меркури 3' '\nАнастасия Пономарева 4')
file_app_information.close()

list_student = []

with open('student_information.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        if '5' in line:
            line = line.upper()
    list_student.append(line.replace('\n',''))
print(list_student)

with open('changed_student_information.txt', "w+", encoding='utf-8') as file_obj:
    for line in list_student:
        file_obj.write(line + '\n')'''

'''def read_file():
    with open('student_information.txt', encoding='utf-8') as file:
        data = file.read().split('\n')
    return  data
student_with_marks = read_file()
for i, element in enumerate(student_with_marks):
    student_with_marks[i] = element.rsplit(' ', maxsplit=1)
print(student_with_marks)
print(type(student_with_marks))'''

# -------------------------------------------------------------------------------
'''num = [randint(1, 10) for i in range(5)]
print(num)
is_odd = lambda num: False if num%2 else True
num = list(filter(is_odd,num))
print(num)'''

'''num1 = [randint(1, 10) for i in range(5)]
print(num1)
num2 = [randint(1, 10) for i in range(5)]
print(num2)
num3 = []
for num1, num2 in zip(num1, num2):
    num3.append(num1+num2)
print(num3)'''

'''numbers = [1,2,3,4,5,6,7,8,9]
factorial = list(map(factorial, numbers))
print(factorial)'''

'''n = 5
lst =[]
lst = [randint(1, 100) for i in range(1, n+1)]
print(lst)'''

# -------------------------------------------------------------------

# n = int(input("Введите число целое: "))

'''''# list_of_coef = random_list(0, 3, n)
# list_of_coef.append(random_list(1, 100, 1).pop())

list_of_coef = [randint(1, 10) for i in range(5)]
# list_of_coef = [randint(1, 10) for i in range(5)]

print(list_of_coef)
str = f"{list_of_coef[n]}*x^{n}"
i = n-1
while i > 0:
    if list_of_coef[i] == 0:
        i -= 1
        continue
    elif i == 1:
        str += f" + {list_of_coef[i]}*x"
    else:
        str += f" + {list_of_coef[i]}*x^{i}"
    i -= 1
else:
    str += f" + {list_of_coef[0]}"
print(str)

with open("Our_polynom.txt", 'w+', encoding='utf-8') as file:
    print(str + " = 0", file=file)'''

# ===========================================================================

# 1 В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

'''lst = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20'
lst = lst.split(',')
lst = [int(i.strip()) for i in lst]
print(lst)
print(lst[9]+2)
res = []
# for i in range(len(lst)-1):
#     if lst[i] + 1 != lst[i+1]:
#         res.append(lst[i]+1)
res = [lst[i]+1 for i in range(len(lst)-1) if lst[i] + 1 != lst[i+1]]
print(res)'''

# 2 Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

'''l = [1, 5, 2, 3, 4, 6, 1, 7]
# l = [l[i] for i in range(len(l)-1) if l[i] < l[i+1]]
# print(l)
# lr = []
# el = l[0]
# lr.append(el)
# for i in range(1, len(l)):
#     if el < l[i]:
#         el = l[i]
#         lr.append(el)
# print(lr)
lr = [l[i] for i in range(1, len(l)) if l[i] > max(l[:i])]
lr.insert(0, l[0])
print(lr)'''

# 3 Напишите программу, удаляющую из текста все слова, содержащие "абв".

# 4 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

'''all_candies = 200
main_player = True
bot = 0

def game_logic(arg_int):
    target = 29
    if arg_int == target:
        return 28
    elif arg_int < target:
        return arg_int
    else:
        return arg_int - target

while all_candies > 28:
    if main_player == True:
        print("Первый игрок берет конфет: ")
        player = int(input())
        if player > 28:
            main_player = None
            print('Конфет можно взять не более = 28')
            break
        if 28 >= player <= 1:
            player = 13
        print(f'Первый игрок взял = {player} конфет')
        all_candies -= player
        main_player = False
        print(f'Конфет осталось = {all_candies}')
    else:
        if all_candies <= 56:
            bot = game_logic(all_candies)
            print(f'Бот взял = {bot} конфет')
            all_candies -= bot
            main_player = True
            print(f'Конфет осталось = {all_candies}')
        else:
            bot = randint(1, 28)
            print(f'Бот взял = {bot} конфет')
            all_candies -= bot
            main_player = True
            print(f'Конфет осталось = {all_candies}')
if main_player == True:
    print(f'Победил игрок. Конфет осталось = {all_candies}')
else:
    print(f'Победил бот. Конфет осталось = {all_candies}')'''

# 5 Создайте программу для игры в "Крестики-нолики".


