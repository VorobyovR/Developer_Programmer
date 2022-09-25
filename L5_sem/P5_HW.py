

# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"


def del_some_words(text: str):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

my_text = 'абвгдейка - это передача"'
print(f'"{my_text} => "{del_some_words(my_text)}')

2.

