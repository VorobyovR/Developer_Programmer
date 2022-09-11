from os import system
system('cls')

from typing import List
import random
from random import randint
from random import shuffle

# 5. Реализовать алгоритм перемешивания списка.

# Variant 1

List = [1,2,3,4,5,6,7,8,9]
size = len(List)
print(f'Original list  -> {List}')
List_shake = []
for i in range(size*size):
    rand_elem_list = randint(0,len(List)-1)
    if List[rand_elem_list] not in List_shake:
        List_shake.append(List[rand_elem_list])
print(f'Mixed list v.1 -> {List_shake}')

# Variant 2

Mixed_list = List[:]
random.shuffle(Mixed_list)
print(f'Mixed list v.2 -> {Mixed_list}')

# Variant 3

l1 = []
l2 = []
n = int(input('Input size for lis: '))
for i in range(n):
    l1.append(randint(0,50))
print(l1)
for i in range(n):
    e = randint(0, len(l1)-1)
    print(e, end=" ")
    e2 = l1.pop(e)
    l2.append(e2)
print()
print(l2)





