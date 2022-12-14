# # В файле находится N натуральных чисел, записанных через пробел. Среди чисел не
# # хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# sp = list(map(int, input('Введите через пробел несколько цифр: ').split()))
# for i in range(1, len(sp)):
#     if sp[i] - sp[i - 1] > 1:
#         print(sp[i] - 1)


# # Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков
# # и определяет, можно ли из этих отрезков составить треугольник.

# def triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         print('Это треугольник')
#     else:
#         print('Не треугольник')


# triangle(3, 4, 55)


# # Напишите программу, которая подсчитает и выведет сумму квадратов всех
# # двузначных чисел, делящихся на 9
# # При решении задачи используйте комбинацию функций filter, map, sum.
# # Обратите внимание: на 9 должно делиться исходное двузначное число, а не его
# # квадрат.

# 1 решение

# sp = range(10, 100)
# sp = filter(lambda x: x % 9 == 0, sp)
# sp = list(map(lambda x:  x ** 2, sp))
# print('Сумма квадратов всех двузначных чисел, делящихся на 9 = ', sum(sp))

# 2 решение
# sp = [i ** 2 for i in range(10, 100) if i % 9 == 0]
# print('Сумма квадратов всех двузначных чисел, делящихся на 9 = ', sum(sp))


# # Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в
# # нем только двузначные числа. Реализовать программу с использованием функции
# # filter. Результат отобразить на экране в виде последовательности оставшихся чисел
# # в одну строчку через пробел.

# sp = [- 8, 11, 0, -23, 140, 1]
# sp = list(filter(lambda x: 10 <= abs(x) <= 100, sp))
# print(sp)


# # Дан список, вывести отдельно буквы и цифры.

# sp = ['1', 'a', 'b', '2', '3' ,'c']
# spalpha = list(filter(lambda x: x.isalpha(), sp))
# spdigit = list(filter(lambda x: x.isdigit(), sp))
# print('Список букв ', spalpha)
# print('Список цифр ', spdigit)



# # Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится лук. Переписывайте без него.
# # Формат ввода
# # На первой строке вводится натуральное число N — количество пунктов рецепта.
# # Далее следуют N строк — пункты рецепта.
# # Формат вывода
# # Одна строка — пункты рецепта, разделённые запятой и пробелом, без пунктов с упоминанием лука (то есть таких, в которых нет подстроки "лук" в нижнем регистре).

# n = int(input('Введите количество пунктов рецепта: '))

# sp = []
# for i in range(n):
#     str = input(f'Введите строку {i+1}: ')
#     sp.append(str)

# sp = list(filter(lambda x: 'лук' not in x, sp))

# print(', '.join(sp))