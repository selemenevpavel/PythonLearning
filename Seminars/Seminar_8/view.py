def show_menu():
    print('Перечень действий: \n1-показать всех сотрудников \n2-добавить сотрудника \n3-удалить сотрудника\n4-выход')
    select = int(input('Выберите действие: '))
    return select


def add_menu():
    print('Введите ФИО, номер телефона через пробел: ')
    man = input().split()
    return man


def delete_menu(number):
    print('Введите номер записи для удаления: ')
    number = int(input())
    return number


def show_result(msg):
    print(msg)


def show_people(people):
    print('№\tФамилия\tИмя\tТелефон')
    for i, p in enumerate(people):
        print(i, *p, sep='\t')
