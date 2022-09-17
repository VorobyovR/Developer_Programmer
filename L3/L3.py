from os import system
system('cls')

# 1. LAMBDA

def calc1(x):
    return x**2
# g = f
# print(type(f))
# print(type(g))
# print(f(4))
# print(g(4))

'''def calc2(x):
    return x+100

def math(op, x):
    print((op(x)))
math(calc1, 4)
math(calc2, 100)

def calc3(x, y):
    return x-y

def calc4(x, y):
    return x*y

def math2(op, a, b):
    print(op(a, b))
math2(calc3, 100, 50)
math2(calc4, 50, 10)'''

'''def math2(op, a, b):
    print(op(a, b))

summ = lambda x, y: x+y-1
math2(summ, 4, 5)
math2(lambda x, y: x+y-1, 4, 5)'''

# 2. LIST COMPREHENSION

# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

'''list = [i for i in range(1, 21)]
print(list)
list2 = [i for i in range(1, 21) if i%2 == 0]
print(list2)
list3 = [(i, i) for i in range(1, 21) if i%2 == 0]
print(list3)'''

'''def f(x):
    return x**3

list4 = [f(i) for i in range(1, 21) if i%2 == 0]
print((list4))
list5 = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
print((list5))'''

'''my_file = open('L3.txt', 'w+')
my_file.write('1 2 3 5 8 15 23 38')
my_file.close()

f = open('L3.txt', 'r')
data = f.read() + ' '
f.close()

numbers = []
while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[space_pos+1:]
out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
# print(out)

def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
# print(data)

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)'''

# 3. MAP

'''ls = list(map(int, input().split()))
print(ls)'''

# 4. FILTER

'''data1 = [i for i in range(10)]
print(data1)
res = list(filter(lambda x: not x%2, data1)) # берем только четные значения из списка data1
print(res)'''

# 5. ZIP

'''users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [1, 5, 8, 36, 2]
salary = [111, 222, 333]
data3 = list(zip(users, ids))
print(data3)
data4 = list(zip(users, ids, salary))
print(data4)'''

# 6. ENUMERATE

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data5 = list(enumerate(users))
print(data5)


