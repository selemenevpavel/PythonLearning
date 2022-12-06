# Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списке.

# sp = [int(i) for i in input().split()]
# for el in sp:
#     if sp.count(el) == 1:
#         print(el)


# Дан список чисел. Выведите все элементы списка, которые больше предыдущего
# элемента.

# sp = [int(i) for i in input().split()]
# for i in range(len(sp)-1):
#     if sp[i] < sp[i+1]:
#         print(sp[i+1], end=' ')


# Реализуйте алгоритм задания случайных чисел без использования встроенного
# генератора псевдослучайных чисел.
# Подсказка: можно использовать модуль datetime

# import time


# def myrandom(x):
#     t = str(time.time())[-x:]
#     print(t)


# myrandom(18)

# Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.

# sp = []
# a = int(input('искомое число '))
# for a in range(5):
#     n = input()
#     sp.append(n)
# print(sp)

# count = 0
# for el in sp:
#     if str(a) in el:
#         count +=1
# if count > 0:
#     print('YES')
# else:
#     print('NO')


# Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.

# sp = ['qwe', 'asd', 'zxc', 'qwe', 'ertqwe']
# find = 'qwe'
# count = 0

# for i in range(len(sp)):
#     if sp[i] == find:
#         count +=1
# if count == 2:
#     print(i)
# else:
#     print('NO')


# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# sp = [1, 5, 2, 2, 2, 4, 5, 6]
# print(len(set(sp)))


# Даны два списка чисел. Найдите все числа, которые входят как в первый,
# так и во второй список и выведите их в порядке возрастания.

# sp1 = [1, 3, 2]
# sp2 = [4, 3, 2]

# print(*set(sp1) & set(sp2)) # * - убирает {} обрамления списка

# Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:

MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..'}

s = 'Help me SOS'.upper().split()
for j in s:
    for i in j:
        if i in MORSE:
            print(MORSE[i], end=' ')
        else:
            print(i, end=' ')
    print(' ')