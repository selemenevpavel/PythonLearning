# Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести
# одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

# first = int(input('Vvedite 1 chislo '))
# second = int(input('Vvedite 2 chislo '))
# third = int(input('Vvedite 3 chislo '))
# if first == second == third:
#     print('3')
# elif first == second or first == third:
#     print('2')
# else:
#     print('0')


# Даны два целых числа A и В, A>B. Выведите все нечётные числа от A до B
# включительно, в порядке убывания. В этой задаче можно обойтись без инструкции
# if.

# a = int(input('Vvedite 1 chislo '))
# b = int(input('Vvedite 2 chislo '))
# a = a - (a-1) % 2
# for i in range(a, b-1, -2):
#     print(i)


# Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов.

# n = int(input('Vvedite 1 chislo '))
# for i in range(n):
#     n=(-3)**(i)
#     print (n)


# Напишите программу, которая проверяет пятизначное число на палиндром.

# n = input('Vvedite chislo ')
# if n[0] == n[4] and n[1] == n[3]:
#     print(f'chislo n={n} palindrom')
# else:
#     print('ne palindrom')

# Prostoe reshenie
# n = input('Vvedite chislo ')
# if n==n[::-1]:
#     print(f'chislo n={n} palindrom')
# else:
#     print(f'chislo n={n} NE palindrom')


# Удалить вторую цифру трёхзначного числа.

# n = input('Vvedite chislo ')
# print(n[0]+n[-1])

# n = int(input('Vvedite chislo '))
# print(n // 100 * 10+n % 10)


# Напишите программу, в которой пользователь будет задавать две строки, а
# программа - определять количество вхождений одной строки в другой.

# str_1 = 'mama myla ramu param pam map'
# str_2 = 'ma'
# print(str_1.count(str_2))

# str_1 = 'mama myla ramu'
# str_2 = 'ma'
# count = 0
# i=0
# while i < len(str_1):
#     res = True
#     for j in range(len(str_2)):
#         if str_1[i] != str_2[j]:
#             res = False
#         i+=1
#     if res == True:
#         count += 1
# print(count)

# По данному целому числу N распечатайте все квадраты натуральных чисел, не
# превосходящие N, в порядке возрастания.

n = int(input('Vvedite chislo '))
i = 0
while i**2 < n:
    print(i*i)
    i +=1
