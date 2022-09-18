from os import system
system('cls')
import utils as check
import math


# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def get_ones(line):
    list_temp = []
    last = 0
    positive = True
    for i, item in enumerate(line):
        if item in {'+', '-'}:
            if positive:
                list_temp.append(line[last:i])
            else:
                list_temp.append('-' + line[last:i])
            last = i + 1
            positive = item == '+'
    if positive:
        list_temp.append(line[last:])
    else:
        list_temp.append('-' + line[last:])
    return list_temp

def get_coef(one):
    for i, item in enumerate(one):
        if item == 'x':
            return int(one[:i]), one[i:]
        if item == 'y':
            return int(one[:i]), one[i:]
    return int(one), None

def convert_list(dict):
    lst = list(dict.values())
    return lst

def write_file(list):
    file_result = open('4.5_final.txt', 'w+')
    file_result.write(f'final -> {result}')
    file_result.close()
    return file_result

first_num = open('4.5_1.txt', 'r')
first_num = first_num.read()
print(f'original first -> {first_num}')

second_num = open('4.5_2.txt', 'r')
second_num = second_num.read()
print(f'original second -> {second_num}')

first_num = get_ones(first_num.replace(' ', '').replace('*', ''))
second_num = get_ones(second_num.replace(' ', '').replace('*', ''))

first_dic = {item[1]: item[0] for item in map(get_coef, first_num)}
second_dic = {item[1]: item[0] for item in map(get_coef, second_num)}

list_for_first = convert_list(first_dic)
list_for_second = convert_list(second_dic)

list_for_first.extend([0] * (len(list_for_second) - len(list_for_first)))
list_for_second.extend([0] * (len(list_for_first) - len(list_for_second)))
print(f'first -> {list_for_first}')
print(f'second -> {list_for_second}')

result = list(map(sum, zip(list_for_first, list_for_second)))
print(f'final -> {result}')

write_file(result)


