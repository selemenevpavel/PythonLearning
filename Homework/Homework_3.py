# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

# from random import randint

# n = int(input('Задайте количество элементов в списке '))
# list = []
# for i in range(n):
#     list.append(randint(0, 10))
# print('Исходный список', list)

# res = 0
# for i in range(n):
#     if i % 2 != 0:
#         res += list[i]
# print('Сумма элементов с нечетными позициями =', res)


# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint

# n = int(input('Задайте количество элементов в списке '))
# list = []
# for i in range(n):
#     list.append(randint(0, 10))
# print('Исходный список', list)

# res = []
# for i in range(n):
#     if i < len(list)/2:
#         res.append(list[i] * list[-i-1])

# print('Полученный список', res)


# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# from random import random

# n = int(input('Задайте количество элементов в списке '))
# list = []
# for i in range(n):
#     list.append(round(random()*10,3))
#     print('%.2f' % list[i], end=', ')
#     list[i] = list[i] - int(list[i])

# diff = max(list) - min(list)
# print()
# print('Разность между max и min равна %.2f' % diff)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# bin = ''
# dec = int(input('Введите десятичное число: '))
# while dec != 0:
#     bin = str(dec % 2) + bin
#     dec //= 2
# print('Равное ему в двоичное:', bin)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)


n = int(input('Задайте длину ряда: '))

sp = [0,]
for e in range(1, n+1):
    sp.append(fib(e))

sp2 = []
for i in range(1, n+1):
    sp2.append(-fib(i))

sp3=sp2.__add__(sp)    

print(sorted(sp3))
