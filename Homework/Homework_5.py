# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]



# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
# более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у
# своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

conf = 100
hod = 1
while conf > 28:
    if hod == 1:
        print('Ход первого игрока')
    else:
        print('Ход второго игрока')


# Создайте программу для игры в "Крестики-нолики".



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример:
# Введите текст для кодировки:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWW
# WWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWW
# WWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.