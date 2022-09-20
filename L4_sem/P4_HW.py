from os import system

system('cls')
import utils as check
import math

# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

'''def prime_factors_number(n):
   i = 2
   list_prime_fact = []
   while 2 * 2 <= n:
       while n % i == 0:
           list_prime_fact.append(i)
           n = n // i
       i = i + 1
   if n > 1:
       list_prime_fact.append(n)
   return list_prime_fact

print('Input a number: ')
n = check.CheckNumber()
print(f'{n} -> {prime_factors_number(n)}')'''

# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

'''def unique_numbers(numbers):
    lst_res = []
    for number in numbers:
        if number not in lst_res:
            lst_res.append(number)
        else:
            continue
    return lst_res

lst = [1,1,1,1,2,2,2,3,3,3,4]
print(f'{lst} -> {unique_numbers(lst)}')'''

# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4
#
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

'''file_app_information = open('file_app_information.txt', 'w+')
file_app_information.write('Ангела Меркель 5' '\nАндрей Валетов 5' '\nФредди Меркури 3' '\nАнастасия Пономарева 4')
file_app_information.close()

file_app_information_read = open('file_app_information.txt')
lst = [line.strip() for line in file_app_information_read]
lst_str = str(lst)
print(lst)

lst_values = []
count = 0
for i in lst_str:
    try:
        lst_values.append(int(i))
    except ValueError:
        pass

num = 5
idx = [i[0] for i in enumerate(lst_values) if i[1] == num]

first = lst.pop(0)
first = first.upper()
lst.insert(0, first)
second = lst.pop(1)
second = second.upper()
lst.insert(1, second)

lst_str_fin = str(lst)
print(lst)

file_app_information = open('file_app_information.txt', 'w+')
file_app_information.write(lst_str_fin)
file_app_information.close()'''

# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

'''def get_encoding(text: str, step: int):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in text:
        position = alphabet.find(i)
        new_position = position + step
        if i in alphabet:
            result += alphabet[new_position]
        else:
            result += i
    return result

def get_decoding(text: str, step: int):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in text:
        position = alphabet.find(i)
        new_position = position - step
        if i in alphabet:
            result += alphabet[new_position]
        else:
            result += i
    return result

text = input('Input text for encoding: ').upper()
shake_character = int(input('Encoding step: '))
print(f'Encoding -> {get_encoding(text, shake_character)}')

file_encoding = open('file_encoding.txt', 'w+')
file_encoding.write(get_encoding(text, shake_character))
file_encoding.close()

file_dencoding = open('file_encoding.txt')
file_dencoding = file_dencoding.read()

print(f'Decoding -> {get_decoding(file_dencoding, shake_character)}')'''


# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def dencoding(text):
    encoding = ""
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + text[i]
        i = i + 1
    return encoding

file_RLE_original = open('file_RLE_original.txt', 'w+')
file_RLE_original.write('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
file_RLE_original.close()

file_RLE_original = open('file_RLE_original.txt')
file_RLE_original = file_RLE_original.read()

ile_RLE_changed = open('file_RLE_changed.txt', 'w+')
ile_RLE_changed.write(dencoding(file_RLE_original))
ile_RLE_changed.close()


