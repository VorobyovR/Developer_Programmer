from os import system
system('cls')

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num_orig = input()
num_copy = num_orig.replace('.', '')
suma = 0
for i in num_copy:
    suma += int(i)
print(f'{num_orig} -> {suma}')