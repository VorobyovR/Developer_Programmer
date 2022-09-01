from xmlrpc.client import boolean


# print("Hello world!")

# типы данных и переменная
# int, float, boolean, str, list, None

value = None
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
print(type(f))


f = False

for item in range(3):
    print(item, end=" ")

else:
    f = True
print(f" цикл выполнен полностью {f}")