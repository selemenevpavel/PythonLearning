# Задайте строку из набора чисел. Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя используйте пробел.

# n = input('Введите несколько чисел ').split()
# print(n)
# n = [int(i) for i in n]
# print(n)
# print(f'Максимум: {max(n)}')
# print(f'Минимум: {min(n)}')


# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1 - с помощью математических формул нахождения корней квадратного
# уравнения
# 2 - с помощью дополнительных библиотек Python

# f = '5x ^ 2 + 3x + -7 = 0'

# f = f[:-3]  # срез, обозначающий срезать 0 сначала и 3 с конца
# print(f)
# f = f.split('+')
# print(f)
# koef = []
# for i in f:
#     koef.append(int(i.split('x')[0]))
# print(koef)
# a, b, c = koef
# D = b*b-4*a*c
# print(D)
# if D > 0:
#     x1 = round((-b-D**0.5)/(2*a), 2)
#     x2 = round((-b+D**0.5)/(2*a), 2)
#     print(x1, x2)
# elif D == 0:
#     x1 = round((-b)/(2*a), 2)
#     print(x1)
# else:
#     print('Корней нет')


# Решение с помощью библиотеки math
# import math

# f = '5x ^ 2 + 3x + -7 = 0'

# f = f[:-3]  # срез, обозначающий срезать 0 сначала и 3 с конца
# print(f)
# f = f.split('+')
# print(f)
# koef = []
# for i in f:
#     koef.append(int(i.split('x')[0]))
# print(koef)
# a, b, c = koef
# D = b*b-4*a*c
# print(D)
# if D > 0:
#     x1 = round((-b-math.sqrt(D))/(2*a), 2)
#     x2 = round((-b+math.sqrt(D))/(2*a), 2)
#     print(x1, x2)
# elif D == 0:
#     x1 = round((-b)/(2*a), 2)
#     print(x1)
# else:
#     print('Корней нет')


# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее
# кратное) этих двух чисел.

# a = int(input('Введите число '))
# b = int(input('Введите число '))
# if a > b:
#     for i in range(1, b+1):
#         if a*i % b == 0:
#             print(a*i)
#             break
# elif a < b:
#     for i in range(1, a+1):
#         if b*i % a == 0:
#             print(b*i)
#             break
# else:
#     print(a)


# В единственной строке записан текст. Для каждого слова из данного текста
# подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца
# строки.

# # slovar = {'login': 'ivan', 'password': '123'}
# # login = 'ivan'
# # password = '12а3'
# # if login == slovar['login'] and password == slovar['password']:
# # print('Доступ разрешен')
# # else:
# # print('Неверная пара логин/пароль')
# #
# # slovar['email'] = 'iv@mail.ru'
# # print(slovar)
# # for key, value in slovar.items():
# # print(key, value)

# # stroka = 'aabbbccccc' # {'a': 2, 'b': 3, 'c': 5}
# # slovar = {}
# # for i in stroka:
# # slovar[i] = slovar.get(i, 0) + 1
# # # if i in slovar:
# # # slovar[i] += 1
# # # else:
# # # slovar[i] = 1
# # print(slovar)

# stroka = 'one two one tho three'.split()
# slovar = {}
# for i in stroka:
#     slovar[i] = slovar.get(i, 0) + 1
#     print(slovar[i]-1, end=' ')


# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к
# парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# Входные данные             # Выходные данные
# 3                          # Bye
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye

# slovar = {}
# for i in range(3):
#     key, value = input().split()
#     slovar[key] = value
# print(slovar)

# slovo = input('Введите слово: ')
# for key, value in slovar.items():
#     if slovo == key:
#         print(value)
#     elif slovo == value:
#         print(key)
#     else:
#         print('Не найдено совпадений')



# Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите
# слово, которое в этом тексте встречается чаще всего. Если таких слов несколько,
# выведите то, которое меньше в лексикографическом порядке.
# apple orange banana banana orange



slovar ={}
stroka = 'apple orange banana banana orange'.split()
print(stroka)
for i in stroka:
    slovar[i] = slovar.get(i, 0)+1
print(slovar)
maxi = max(slovar.values())
mini = 'z'
for key, value in slovar.items():
    if value == maxi:
        if key < mini:
            mini = key
print(mini)
