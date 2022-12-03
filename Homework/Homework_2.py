# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

# n = input('Введите число: ')
# def sum(n):
#     if float(n) < 0:
#         n = - float(n)
#         number = 0
#     for i in str(n):
#         if i != '.':
#             number += int(i)
#             print(number)
#     return number
# print(f'Сумма чисел равна {sum(n)}')


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

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

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input('Введите количество чисел в списке '))

# res = 0
# for i in range(n):
#     e = (1+1/n)**n
#     res += e
#     i += 1
# print(res)
