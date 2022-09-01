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
'''
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
'''
#управляющие конструкции
# if, else, elif

'''a = int(input('a = ')) 
b = int(input('b = '))

if a > b:
    print('bigger = ', a)
else:
    print('bigger = ', b)'''

'''username = input("Введите имя: ")
if username == 'Марина':
    print("Привет ", username, "!")
elif username == 'Маша':
    print("Это же ", username, "!")
elif username == 'Тома':
    print("Опять ты  ", username, "!")
else:
    print("Добрый день  ", username, "!")'''

'''oriqinal = 546
inverted = 0
while oriqinal !=0:
    inverted = inverted * 10 + (oriqinal % 10)
    oriqinal //=10
else:
    print('Пожалуй хватит)')
print(inverted)'''

'''list =[1,2,3,4,5]
for i in list:
    print(i**2, end=' ')
print()
a = range(10)
for i in a:
    print(i, end=" ")
print()
b = range(1, 10, 2)
for i in b:
    print(i, end=" ")

print()
for i in 'qwerty':
    print(i, end=" ")'''

'''f = False
for item in range(3):
    print(item, end=" ")
else:
    f = True
print(f" цикл выполнен полностью {f}")'''

# работа с текстом
'''
text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...
'''

# списки - продолжение

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i, end=" ") # [20, 4, 6, 8, 10]
print()
print(numbers) # [10, 2, 3, 4, 5]