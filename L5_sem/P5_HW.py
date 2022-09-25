# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

'''def del_some_words(text: str):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

my_text = 'абвгдейка - это передача"'
print(f'"{my_text} => "{del_some_words(my_text)}')'''

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

'''all_candies = 2021
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
    print(f'Победил бот. Конфет осталось = {all_candies}')'''

# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# 4. Создайте программу для игры в ""Крестики-нолики"".

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3  == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')

print(print_state(board))

win_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == '0'):
            return state[x]
        return ''

def game(board):
    current_step = 'X'
    while (get_winner(board, win_combinations) == ''):
        index = int(input(f'Where do you want to draw:  {current_step}?'))
        board[index] = current_step
        print_state(board)
        winner_sign = get_winner(board, win_combinations)
        if winner_sign != '':
            print(f'We have a winner: {winner_sign}')
        current_step = 'X' if current_step == '0' else '0'

game(board)
