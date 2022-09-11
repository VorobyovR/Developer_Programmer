from os import system
system('cls')

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.


num = int(input('Input a number: '))
result = 0
sum = 0
d = {}

for i in range(1, num+1):
    result = round((1+1/i)**i, 2)
    sum = sum + result
    d[i] = result
print(f'For num = {num}: {round(sum)}')
print(d)
