def show_menu():
    print('Выберите дейстиве: \n1 - Калькулятор \n2 - Конвертер')
    select = input()
    return select


def get_example():
    x = input('Введите выражение: ')
    return x


def get_convert():
    m = int(input('Введите массу в кг: '))
    return m


def show_res(res):
    print(f'Результат вычисления: {res}')


def show_res_m(res):
    print(f'Результат конвертации: {res} грамм')
