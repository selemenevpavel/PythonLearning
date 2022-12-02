# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# num = int(input("Введите порядковый номер дня недели: "))

# if 1 > num or num > 7:
#     print('Некорректное значение')
# elif num > 5:
#     print('Выходной!')
# else:
#     print('Иди на работу')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# if not (x or y or z) == (not x and not y and not z):

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == (not x and not y and not z):
                print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно при x = {x}, y={y}, z={z}')