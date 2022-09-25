from os import system
system('cls')
import random
from random import  randint

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

all_candies = 2021
main_player = True
bot = 0

def game_logic(arg_int):
    target = 29
    if arg_int == target:
        return 28
    elif arg_int < target:
        return arg_int
    else:
        return arg_int - target

while all_candies > 28:
    if main_player == True:
        print("Первый игрок берет конфет: ")
        player = int(input())
        if player > 28:
            main_player = None
            print('Конфет можно взять не более = 28')
            break
        if 28 >= player <= 1:
            player = 13
        print(f'Первый игрок взял = {player} конфет')
        all_candies -= player
        main_player = False
        print(f'Конфет осталось = {all_candies}')
    else:
        if all_candies <= 56:
            bot = game_logic(all_candies)
            print(f'Бот взял = {bot} конфет')
            all_candies -= bot
            main_player = True
            print(f'Конфет осталось = {all_candies}')
        else:
            bot = randint(1, 28)
            print(f'Бот взял = {bot} конфет')
            all_candies -= bot
            main_player = True
            print(f'Конфет осталось = {all_candies}')
if main_player == True:
    print(f'Победил игрок. Конфет осталось = {all_candies}')
else:
    print(f'Победил бот. Конфет осталось = {all_candies}')

