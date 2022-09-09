from os import system
system('cls')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Input a number: '))
multiplication = 1
list = []
for i in range(num):
    i+=1
    multiplication*=i
    list.append(multiplication)
print(f'N = {num}, then {list}')









