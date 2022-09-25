from os import system
system('cls')

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def dencoding(text):
    encoding = ""
    i = 0
    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + text[i]
        i = i + 1
    return encoding

def encoding(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

file_RLE_original = open('file_RLE_orig.txt', 'w+')
file_RLE_original.write('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')
file_RLE_original.close()

file_RLE_original = open('file_RLE_orig.txt')
file_RLE_original = file_RLE_original.read()

ile_RLE_changed = open('file_RLE_chang.txt', 'w+')
ile_RLE_changed.write(dencoding(file_RLE_original))
ile_RLE_changed.close()

file_RLE_changed = open('file_RLE_chang.txt')
file_RLE_changed = file_RLE_changed.read()

file_RLE_chang_last = open('file_RLE_chang_last.txt', 'w+')
file_RLE_chang_last.write(encoding(file_RLE_changed))
file_RLE_chang_last.close()
