from random import randint
'''N = 10
arr = []
for i in range(N):
    arr.append(randint(1, 99))
print(arr)

arr.sort()
print(arr)

min = arr[0]
max = arr[-1]
print(f'min = {min}, max = {max}')'''

# ============================================

'''a = float(input('Веведите первое число: '))
b = float(input('Веведите второе число: '))
if a == b ** 2:
    print(f'Число {b} является квадратом числа {a}')
else:
    print(f'Число {b} не является квадратом числа {a}')'''

'''a = randint(1,99)
b = randint(1,99)
c = randint(1,99)
d = randint(1,99)
e = randint(1,99)
print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}')
if a > b and a > c and a > d and a > e:
    print(f'max a -> {a}')
elif b > a and b > c and b > d and b > e:
    print(f'max b -> {b}')
elif c > a and c > b and c > d and c > e:
    print(f'max c -> {c}')
elif d > a and d > b and d > c and d > e:
    print(f'max d -> {d}')
else:
    print(f'max e -> {e}')'''

''''list = []
for i in range(5):
    list.append(randint(1,99))
print(list)
list.sort()
print(list[-1])
print(max(list))

max = list[0]
for i in list:
    print(i, end=" ")
    if i >= max:
        max = i
print()
print(max)'''

'''number_N = int(input('Веведите число: '))
for i in range(-number_N, number_N+1):
    print(i, end =" ")'''

''''number_N = float(input('Веведите число: '))
number_N = int(number_N*10%10)
print(number_N)'''

'''number_N = float(input('Веведите число: '))
if number_N % 30 != 0:
    if number_N % 5 == 0 and number_N % 10 == 0 or number_N % 15 == 0:
        print('Yes')
    else:
        print('No')
else:
    print('Not right number')'''



