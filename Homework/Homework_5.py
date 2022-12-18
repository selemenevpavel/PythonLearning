# # Напишите программу, удаляющую из текста все слова, содержащие "абв".
# # [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]

# sp = ['ПРИВЕТ', 'ЗАБВЕНИЕ', 'ПОКА']

# sp = list(filter(lambda x: 'абв'.upper() not in x, sp))

# print(', '.join(sp))


# # Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# # после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# # более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# # ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у
# # своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота "интеллектом"

# from random import randint

# conf = int(input('Введите количество конфет для игры: '))

# x = randint(1, 2)

# if x == 1:
#     print('Начинает первый игрок')
# else:
#     print('Начинает второй игрок')

# hod = x - 1
# max_step = 28
# while conf > 0:
#     if hod == 0:
#         step = int(input('Взять конфет 1 игроку: '))
#         if step > conf or step > max_step:
#             print(f'Нельзя брать больше {max_step} конфет за ход')
#             step = int(input(f'Взять конфет 1 игроку: '))
#         conf -= step
#     if conf > 0:
#         print(f'Осталось конфет: {conf}')
#         hod = 1
#     else:
#         print('Конфет не осталось')

#     if hod == 1:
#         step = int(input('Взять конфет 2 игроку: '))
#         if step > conf or step > max_step:
#             print(f'Нельзя брать больше {max_step} конфет за ход')
#             step = int(input(f'Взять 2 конфет игроку: '))
#         conf -= step
#     if conf > 0:
#         print(f'Осталось конфет: {conf}')
#         hod = 0
#     else:
#         print('Конфет не осталось')

# if hod == 1:
#     print('Победил второй игрок')
# if hod == 0:
#     print('Победил первый игрок')


# Игра против бота с ИНТЕЛЛЕКТОМ

# from random import randint

# conf = int(input('Введите количество конфет для игры: '))

# x = randint(1, 2)

# if x == 1:
#     print('Начинает игрок')
# else:
#     print('Начинает бот')

# hod = x - 1
# max_step = 28
# while conf > 0:
#     if hod == 0:
#         step = int(input('Взять конфет игроку: '))
#         if step > conf or step > max_step:
#             print(f'Нельзя брать больше {max_step} конфет за ход')
#             step = int(input(f'Взять конфет игроку: '))
#         conf -= step
#     if conf > 0:
#         print(f'Осталось конфет: {conf}')
#         hod = 1
#     else:
#         print('Конфет не осталось')

#     if hod == 1:
#         if conf <= max_step:
#             step = conf
#             print(f'Бот взял конфет: {step}')
#         if max_step + 2 <= conf < max_step * 2:
#             step = 1
#             print(f'Бот взял конфет: {step}')
#         if conf >= max_step * 2:
#             step = randint(1, max_step)
#             print(f'Бот взял конфет: {step}')
#         conf -= step
#     if conf > 0:
#         print(f'Осталось конфет: {conf}')
#         hod = 0
#     else:
#         print('Конфет не осталось')

# if hod == 0:
#     print('Победил игрок')
# if hod == 1:
#     print('Победил бот')


# # Создайте программу для игры в "Крестики-нолики".

# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]

# victories = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]


# def print_maps():
#     print(maps[0], end=" ")
#     print(maps[1], end=" ")
#     print(maps[2])

#     print(maps[3], end=" ")
#     print(maps[4], end=" ")
#     print(maps[5])

#     print(maps[6], end=" ")
#     print(maps[7], end=" ")
#     print(maps[8])


# def step_maps(step, symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol


# def get_result():
#     win = ""

#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"

#     return win


# game_over = False
# player1 = True

# while game_over == False:
#     print_maps()

#     if player1 == True:
#         symbol = "X"
#         step = int(input("Ход 1 игрока: "))
#     else:
#         symbol = "O"
#         step = int(input("Ход 1 игрока: "))

#     step_maps(step, symbol)
#     win = get_result()
#     if win != "":
#         game_over = True
#     else:
#         game_over = False

#     player1 = not (player1)

# print_maps()
# print("Победил", win)

# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Пример:
# # Введите текст для кодировки:
# # WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# # Текст после кодировки: 12W1B12W3B24W1B14W
# # Текст после дешифровки:
# # WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# # Входные и выходные данные хранятся в отдельных текстовых файлах.


# with open('Homework\HW5.1.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Текст для кодирования: '))
# with open('Homework\HW5.1.txt', 'r') as file:
#     text = file.readline()


# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string


# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string


# with open('Homework\HW5.1.txt', 'r') as file:
#     decoded_string = file.read()

# with open('Homework\HW5.2.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Закодированная строка: ' + rle_encode(decoded_string))
# print('Декодированная строка: ' + decoded_string)
