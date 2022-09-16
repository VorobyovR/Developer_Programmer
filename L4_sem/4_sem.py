from os import system
system('cls')
import math


# 1 Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

'''number = input('Input a number: ')
list = []
for i in number:
    list.append(i)
list = sorted(list)
max = list[-1]
min = list[0]
print(f'{list}: max = {max}, min = {min}')'''
# ---------------------------------------------------------------------------

'''list1 = [int(s) for s in input('Input a number: ').split()]
print(list1)
mx = max(list1)
mn = min(list1)
print(mn, mx)'''

# 2 Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения;
# 2) с помощью дополнительных библиотек Python.

'''a = int(input('Укажите коэффициент а: '))
b = int(input('Укажите коэффициент b: '))
c = int(input('Укажите коэффициент c: '))
d = b**2 - 4*a*c
print(d)
if d < 0:
    r = 'Действительных корней нет'
elif d == 0:
    r = f'Уравнение имеет один корень: {-b/(2*a)}'
else:
    r = f'Корни уровнения: x1 = {(-b+d**0.5)/(2*a)}, x2 = {(-b-d**0.5)/(2*a)}'
print(r)'''

'''a = int(input('Укажите коэффициент а: '))
b = int(input('Укажите коэффициент b: '))
c = int(input('Укажите коэффициент c: '))
d = b**2 - 4*a*c
if a == 0:
    r = 'Решения нет'
elif d < 0:
    r = 'Действительных корней нет'
else:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    r = f'Корни уравнения: x1 = {x1}, x2 = {x2}'
print(r)'''

# 3 Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# variant 1

'''a = int(input('Input a number: '))
b = int(input('Input a number: '))
if b > a:
    a, b = b, a
for i in range(1, b):
    if (a * (i))%a == 0 and (a * (i))%b == 0:
        print(i)
        break
print(f'{a} {i} = {a * (i)}')

# variant 2

a = int(input('Input a number: '))
b = int(input('Input a number: '))

print(math.lcm(b, a))

# variant 3

i = min(a, b)
print(i)
while True:
    if i%a == 0 and i%b == 0:
        break
    i+=1
print(i)'''


# 4. Доп задача

'''n = 80
sieve = set(range(2, n+1))
# print(sieve)
prime_list = []
while sieve:
    prime = min(sieve)
    prime_list.append(prime)
    # print(prime)
    sieve -= set(range(prime, n+1, prime))
    # print(sieve)
print(prime_list)

print(round(math.pi, 4))'''

# --------------------------------------------------------------------------

'''file1 = '5x^5 + 3 x ^ 2 + 3 * x - 22 * x^7 - 77'
file2 = '3x^2 - 2x + 5'


def get_ones(line):
    tmp = []
    last = 0
    positive = True
    for i, item in enumerate(line):
        if item in {'+', '-'}:
            if positive:
                tmp.append(line[last:i])
            else:
                tmp.append('-' + line[last:i])
            last = i + 1
            positive = item == '+'

    if positive:
        tmp.append(line[last:])
    else:
        tmp.append('-' + line[last:])
    return tmp


def get_coef(one):
    for i, item in enumerate(one):
        if item == 'x':
            return int(one[:i]), one[i:]
    return int(one), None


lst1 = get_ones(file1.replace(' ', '').replace('*', ''))
lst2 = get_ones(file2.replace(' ', '').replace('*', ''))

dct1 = {item[1]: item[0] for item in map(get_coef, lst1)}
dct2 = {item[1]: item[0] for item in map(get_coef, lst2)}


print(dct1)
print(dct2)'''

# ----------------------------------------------------------------------