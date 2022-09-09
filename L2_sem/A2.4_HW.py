from os import system
from typing import List
system('cls')
from random import randint

# 4. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

N_size = randint(10, 20)
N_element = randint(1, 100)
List = [randint(-N_element, N_element) for i in range(N_size)]
print(f'Original list -> {List}')
position_list = []
for i in range(N_size):
    position_list.append(i)
print(f'Positions list -> {position_list}')
first_pos = randint(0,len(position_list)-1)
second_pos = randint(0,len(position_list)-1)
print(f'First position = {first_pos}')
print(f'Second position = {second_pos}')
result = List[first_pos] * List[second_pos]
print(f'Multiplication = {result}')

