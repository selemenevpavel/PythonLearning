from view import *
from model import *

def main():
    while True:
        select = show_menu()
        if select == 1:
            people = get_people()
            show_people(people)
        elif select == 2:
            man = add_menu()
            add_people(man)
            show_result('Запись добавлена')
        elif select == 3:
            number = delete_menu()
            delite_people(number)
            show_result('Запись удалена')
        elif select == 4:
            show_result('До встречи')
            break
