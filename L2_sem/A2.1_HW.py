from os import system
system('cls')

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num_orig = input('Input a number: ')
suma = 0
for i in num_orig:
    num_orig = num_orig.replace('-', '')
    num_orig = num_orig.replace('.', '')
for i in num_orig:
    suma += int(i)
print(f'{num_orig} -> {suma}')