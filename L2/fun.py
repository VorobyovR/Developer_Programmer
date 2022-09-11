from os import system
system('cls')

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# a = 1
# print(f(a))
# ===============================================

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

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2) # расчет фибоначи
list = []
for e in range(1, 10):
    list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34