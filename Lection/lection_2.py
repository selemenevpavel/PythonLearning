# with open('file.txt', 'a') as data:
#     data.write('Line 1\n')
#     data.write('Line 2\n')


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)  #разделителей не будет
# data.close()


# path='file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close

# import hello      # Импорт метода (функции) из файла hello
# print(hello.f(2.3))

# import hello as h
# print(h.f(2.3))   #Запись сверху равносильна записи снизу

# def concatenatio(*parasm):
#     res = 0
#     for item in parasm:
#         res += item
#     return res

# print(concatenatio(1, 2, 3, 4))


# # Рекурсия

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)


# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

# Кортежи - неизменяемый список

# (a) = (3, 4, 1, 56, 34)   #координаты кортежа а
# print(a)
# print(a[3])   #при указании в квадратных скобках положительного числа, работаем как с массивом и начинаем с 0-го элемента
# print(a[-2])  # при указании отрицательного числа работаем как со списком и элементы идут с конца
# a[0]=12       #такая запись не работает


# Словари

# dictionary = {}  # пустой словарь
# dictionary = \
#     {
#         'up': 'вверх',
#         'down': 'вниз',
#         'lift': 'влево',
#         'right': 'вправо'
#         #ключ: значение
#     }
# print(dictionary)           #{'up': 'вверх', 'down': 'вниз', 'lift': 'влево', 'right': 'вправо'}
# print(dictionary['right'])  #вправо

# for k in dictionary.keys(): #просмотр всех ключей
#     print(k)
# for k in dictionary.values():  #просмотр всех значений
#     print(k)

# Множества

# colors = {'red', 'green', 'blue'}

# colors.add('gray')
# colors.remove('red')    #Выведет ошибку в случае отсутствия элемента
# colors.discard('red')     #удалит элемент и продолжит работу без ошибки даже если элемента нет
# colors.clear()            #очистит множество удалив все элементы
# print (colors)

# a = {1, 2, 3, 4, 5}
# b = {2, 4, 6, 8, 9}
# c = a.copy()                #{1, 2, 3, 4, 5}
# u = a.union(b)              #{1, 2, 3, 4, 5, 6, 8, 9}
# i = a.intersection(b)       #{2, 4}
# dl = a.difference(b)        #{1, 3, 5}
# dr = b.difference(a)        #{8, 9, 6}

# q = a\
#     .union(b)\
#     .difference(a.intersection(b))      #{1, 3, 5, 6, 8, 9}

# print(q)



