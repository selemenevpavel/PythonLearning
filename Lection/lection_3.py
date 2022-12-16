# def f(x):
#     return x**2

# g = f
# print(f(2))
# print(g(8))

# def calc1(x):
#     return x+10


# def calc2(x):
#     return x*10

# def math(op, x):
#     print (op(x))

# math(calc1, 10)
# math(calc2, 10)
# ___________________________________________________________

# def sum(x, y):
#     return x+y

# def sum(x, y): return x+y  # запись равносильна записи выше


# def mylt(x, y):
#     return x*y


# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a,b)


# calc(sum, 4, 5)
# calc(lambda x, y: x+y, 4, 5)  # Равносильные записи


# ----------------------------------------------------------------------

# LIST Comprehension

# list = []

# for i in range(1, 21):
#     if (i % 2 == 0):
#         list.append(i)

# print(list)

# list = [i for i in range(1, 21) if i % 2 == 0] #Список четных от 1 до 21
# print(list)

# list = [(i, i) for i in range(1, 21) if i % 2 == 0] #Список кортежей четных от 1 до 21
# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0] #Список кортежей четных и их кубов от 1 до 21
# print(list)


# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4 5 8 15 23 38'.split()

# res = select(int, data) # Превращение списка дата в список чисел
# res = where(lambda x: not x%2, res)  #Проверка на честность в списке res
# res = select(lambda x: (x, x**2), res)  # Создание кортежа из х и его квадрата
# print(res)

# -----------------------------------------------------------------------------------------

# li = [x for x in range(1, 21)]

# li = list(map(lambda x: x+10, li))

# print(li)

# data = list(map(int, input().split()))
# print(data)


# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4 5 8 15 23 38'.split()

# res = map(int, data) # Превращение списка дата в список чисел
# res = where(lambda x: not x%2, res)  #Проверка на честность в списке res
# res = list(map(lambda x: (x, x**2), res))  # Создание кортежа из х и его квадрата
# print(res)

# -----------------------------------------------------------------------------

# data = [x for x in range(10)]

# res = list(filter(lambda x: x % 2 == 0, data))

# print(res)


# data = '1 2 3 4 5 8 15 23 38'.split()

# res = map(int, data) # Превращение списка дата в список чисел
# res = filter(lambda x: not x%2, res)  #Проверка на честность в списке res
# res = list(map(lambda x: (x, x**2), res))  # Создание кортежа из х и его квадрата
# print(res)


# ------------------------------------------------------------------------------------------

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# data = list(zip(users, ids, salary))  # Объединение наборов
# print(data)



users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111,222,333]

data = list(enumerate(users)) # Нумерация наборов
print(data)