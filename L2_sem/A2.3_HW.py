from os import system
system('cls')

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input('Input a number: '))
multiplication = 1
result = 0
sum = 0
list = []
for i in range(num):
    i+=1
    multiplication*=i
    list.append(multiplication)
for i in list:
    result = (1+1/i)**i
    sum = sum + result
print(f'For num = {6}: {round(sum)}')
