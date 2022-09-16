from os import system
system('cls')
import math
import random as rand

list = []
for i in range(10):
    list.append(round(rand.random() * 10 ** rand.randint(0, 3), 2))
print(list)
list2 = []
for i in range(len(list)):
    list2.append((list[i] % 1))
mx = max(list2)
mn = min(list2)
print(mx)
print(mn)
print(round(mx - mn, 2))