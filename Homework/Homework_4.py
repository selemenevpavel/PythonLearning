# Вычислить число c заданной точностью d

# from math import pi
# d = int(input('Введите количество знаков после запятой: '))
# print('точность d=', 1/(10**d))
# print(f'число Пи с точностью {d} знаков', round(pi, d))


# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

# n = int(input('Введите натуральное число N: '))
# sp = []
# a = 2
# while a <= n:
#     if n % a == 0:
#         sp.append(a)
#         n = n / a
#     else:
#         a += 1
# print(sp)


# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# from random import randint
# n = int(input('Задайте количество элементов в списке: '))
# sp = []
# for i in range(n):
#     sp.append(randint(0, n//2))
#     # диапазон от 0 до n//2 выбран для того, чтобы числа в списке повторялись
# print(f'Случайный список из {n}-элементов', sp)

# a = set(sp)
# sp1 = []
# for i in a:
#     if (sp.count(i) < 2):
#         sp1.append(i)
# print('Список неповторяющихся элементов ', sp1)


# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k.

# from random import randint

# k = int(input('Введите степеь многочлена: '))

# koef = []
# for i in range(k+1):
#     koef.append(randint(0, 101))
# print(f'Коэффициенты многочлена {koef}')


# def write_file(st):
#     with open('PythonLearning\Homework\Homework-4.1.txt', 'w') as data:
#         data.write(st)


# def create_str(koef):
#     lst= koef[::1]
#     write = ''
#     if len(lst) < 1:
#         write = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 write += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     write += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 write += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     write += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 write += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 write += ' = 0'
#     return write

# write_file(create_str(koef))


# Даны два файла, в каждом из которых находится запись многочлена. Задача -
# сформировать файл, содержащий сумму многочленов.

f1 = '7x^2 + 5x + 2'
f2 = '3x^2 + 7x + 5'

with open('PythonLearning\Homework\HW4.2.1.txt', 'w', encoding='utf-8') as file:
    file.write(f1)
with open('PythonLearning\Homework\HW4.2.2.txt', 'w', encoding='utf-8') as file:
    file.write(f2)

with open('PythonLearning\Homework\HW4.2.1.txt','r') as file:
    func1 = file.readline()
    list1 = func1.split('+')
koef1 = []
for i in list1:
    koef1.append(int(i.split('x')[0]))
print('список коэффициентов первого многочлена ', koef1)

with open('PythonLearning\Homework\HW4.2.2.txt','r') as file:
    func2 = file.readline()
    list2 = func2.split('+')
koef2 = []
for i in list2:
    koef2.append(int(i.split('x')[0]))
print('список коэффициентов второго многочлена ', koef2)

sum = []
for i in range(3):
    sum.append(koef1[i] + koef2[i])
print('Сумма коэффициентов многочленов', sum)

def write_file(st):
    with open('PythonLearning\Homework\HW4-res.txt', 'w') as data:
        data.write(st)


def create_str(sum):
    lst= sum[::1]
    write = ''
    if len(lst) < 1:
        write = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                write += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    write += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                write += f'{lst[i]}x'
                if lst[i+1] != 0:
                    write += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                write += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                write += ' = 0'
    return write

write_file(create_str(sum))
