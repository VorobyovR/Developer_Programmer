from os import system
system('cls')
import random as rand
from random import randint

import fun as check

# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci_negafibonacci(n: int):
    l_one = []
    l_two = []
    for i in range(0,n):
        if i == 0:
            l_one.append(0)
        elif 1 <= i <= 2:
            l_one.append(1)
            if i == 1:
                l_two.append(1)
            if i == 2:
                l_two.append(-1)
        else:
            l_one.append(l_one[i-2]+l_one[i-1])
            l_two.append(((-1)**(i+1))*l_one[-1])
    
    l_two = l_two[::-1]
    final = l_two + l_one
    return final

print("Input a number:")
n = check.CheckNumber()
print(fibonacci_negafibonacci(n))