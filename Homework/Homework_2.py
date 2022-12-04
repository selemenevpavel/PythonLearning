# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

# n = input('Введите число: ')
# def sum(n):
#     if float(n) < 0:
#         n = -float(n)
#     number = 0
#     for i in str(n):
#         if i != '.':
#             number += int(i)
#             return number
# print(f'Сумма чисел равна {sum(n)}')


# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input('Введите число: '))
# if n < 0:
#     print('Некорректное значение')
# if n == 0:
#     print(1)
# factorial = 1
# for i in range(n):
#     i += 1
#     factorial *= i
#     print(factorial, end=", ")


# # Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input('Введите количество чисел в списке '))

# res = 0
# for i in range(n):
#     e = (1+1/n)**n
#     res += e
#     i += 1
# print(f'Сумма чисел равна {res}')


# # Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# # Найдите произведение элементов на указанных позициях. Позиции хранятся
# # в файле file.txt в одной строке одно число.

# n = int(input('Задайте число N '))

# list = [i for i in range(-n, n+1)]

# print('Список от -N до N', list)

# path = 'file_homework2.txt'
# data = open(path, 'r')
# for line in data:
#     a = int(line[0])
#     b = int(line[1])
#     print('Номера позиций в файле ', line[0], line[1])
#     mult = list[a] * list[b]
# print('Произведение чисел на указанных позициях', mult)


# # Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).

from random import randint

n = int(input('Задайте количество элементов в списке '))
list = []
for i in range(n):
    list.append(randint(0, 10))
print('Исходный список', list)

def shuffle(list):
    for i in range(n):
        index = randint(0, n-1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list

print('Перемешанный список', shuffle(list))
