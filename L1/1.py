from xmlrpc.client import boolean


# print("Hello world!")

# типы данных и переменная
# int, float, boolean, str, list, None

'''value = None
a = 123
b =1.23
print(a)
print(b)
value = 1234
print(value)
print(type(a))
print(type(b))
print(type(value))

s = 'Hello \n"world"' #\n перевод на новую строку
print(s)
s1 = 'Hello "world"' #\n перевод на новую строку


# интерпаляция
print(a, ' - ', b, ' - ', s1)
print('{} - {} - {}'.format(a,b,s1))
print('{1} - {2} - {0}'.format(a,b,s1)) #переставлять местами
print(f'{a} - {b} - {s1}')

f = True
print(f)
print(type(f))'''

# списки/массивы

'''list =['1', '2', '3', 'hello', 1, 2, 3, 4.456, True]
print(list)'''

# ввод и вывод данных

'''print("введите а")
a = int(input()) #int (float) меняет тип данныс с сточного на числовое
print("введите b")
b = int(input())
print(a,b)
print(f'{a} {b}')
print(a, '+', b, '=', a + b)'''

# арифмитические операции
'''
a = 123
b = -321
c = a+b
y = a*b
print(c)
print(y)

r = 12
m = 8
n = r / m #деление с остатком
t = r // m #целочисленное деление
k = r % m #остаток от деления
o = r ** m #возведение в степень
print(n)
print(t)
print(k)
print(o)

a = 1.3123
b = 3
y = round(a*b, 2) #округление
print(y)

a = 5
a+=3
print(a)'''

# логические операции

a = 1 < 4
print(a)
a = 1 < 4 > 2 < 10
print(a)
a = 1 < 4 and 5 > 2
print(a)
a = 1 == 4 
print(a)
a = 1 != 4
print(a)

a = 'qwerty'
b = 'qwerty'
c = a == b
print(c) 

a = [1,2]
b = [1,2]
print(a == b)

f = 1 > 2 or 4 < 6
print(f)

list = [1,2,3,4]
print(list)
print(2 in list)
print(not 2 in list)
is_odd = list[0] % 2 == 0
print(is_odd)
is_odd_1 = not list[0] % 2 == 0
print(is_odd_1)

'''f = False

for item in range(3):
    print(item, end=" ")

else:
    f = True
print(f" цикл выполнен полностью {f}")'''