from os import system
system('cls')
import random as rand
from random import randint

import utils as check

# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def write_file(k):
    file_result = open('4.4.txt', 'w+')
    file_result.write(f'k = {k} => {randint(1, 100)}x^{k} + {randint(1, 100)}x + {randint(1, 100)} = 0')
    file_result.close()
    return file_result

print("Input a number:")
k = check.CheckNumber()
write_file(k)

