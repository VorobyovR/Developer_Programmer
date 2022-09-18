from os import system
system('cls')
import utils as check
import math

# 1 Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10-1 <= d <= 10-10

def number_pi(num):
    pi = round(math.pi, num)
    return pi

print('Input a number <= 10: ')
d = check.CheckNumber()
if 1 <= d <= 10:
    print(f'{d} -> {number_pi(d)}')
else:
    print('Error, Print a right number')