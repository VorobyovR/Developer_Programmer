from os import system
system('cls')

# 1. работа с файлом txt

# with open('file.txt', 'a') as data:
#     data.write('line 11\n')
#     data.write('line 21\n')

# colors =['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLine 123\n')
# data.write('Line 133\n')
# data.close

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# 2. Модули 

# import fun as h
# print(h.f(1))

# 3. Функции

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...
# print(new_string(4))
# ==================================================

# def concatenatio(*params):
    ## res: str = "" # показана работа с строками
    # res: int = 0 # показана работа с числами - сложение всех элементов
    # for item in params:
    #     res += item
    # return res
## print(concatenatio('a', 's', 'd', 'w')) # asdw
## print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...
# ===================================================

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2) # расчет фибоначи
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# 4. Кортежи. Кортеж – это неизменяемый “список”

# a, b = 3, 4
# print(a)
# print(b)

# a =(3,4,41,-3)
# print(a)
# print(a[0])
# print(a[-2])
# ====================================

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# ======================================

# a =(3,4,41,-3)
# for item in a:
#     print(item)
# ======================================

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment
# ===========================================

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# 5. Словари. Неупорядоченные коллекции произвольных объектов с доступом по ключу

'''dictionary = {}
# слеш нужен, чтобы не писать все в одну строку
dictionary = \
{
'up': '↑',
'left': '←',
'down': '↓',
'right': '→'
}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←  типы ключей могут отличаться

for k in dictionary.keys(): # выводим ключи
    print(k)
for el in dictionary.values(): # выводим значения
    print(el)
dictionary['up'] = 'up' # меняем значения в словаре
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: up
# down: ↓
# right: →'''

# 6. Множества. Неупорядоченная совокупность элементов

# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(a)
# print(type(a)) # set
# print(type(b)) # set
# ================================================

'''colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red') # удаление элемента
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok, удаление элемента
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()'''
# ===================================================

'''a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}

q = a \
.union(b) \
.difference(a.intersection(b))
# {1, 21, 3, 13}

s = frozenset(q) # замораживание множества, больше ничего с ним делать нельзя
print(s)'''
# =====================================================

# Глубокая работа со списками

'''list1 = [1,2,3,4,5]
list2 = list1
list1[0] = 123
list1[1] = 333
for i in list1:
    print(i)
print()
for i in list2:
    print(i)'''
# ======================================================

list1 = [1,2,3,4,5]
print(len(list1))
print(list1.pop())
print(len(list1))
print(list1.pop(2))
print(len(list1))
print(list1)
list1.insert(2, 11)
print(list1)
list1.append(35)
print(list1)

