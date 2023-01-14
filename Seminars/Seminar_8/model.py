import csv
from view import add_menu


def get_people_csv():
    with open('Seminars\Seminar_8\people.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
        return sp


def add_people_csv(man):
    with open('Seminars\Seminar_8\people.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(man)


def delete_people_csv(number):
    with open('Seminars\Seminar_8\people.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
    if number < len(sp):
        del sp[number]
        with open('Seminars\Seminar_8\people.csv', 'w', encoding="utf8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in sp:
                writer.writerow(row)
        with open('Seminars\Seminar_8\people.txt', 'w', encoding="utf8", newline='') as txtfile:
            writer = writer(txtfile, delimiter=';')
            for row in sp:
                writer.writerow(row)


def get_people_txt():
    with open('Seminars\Seminar_8\people.txt', encoding="utf8") as txtfile:
        reader = reader(txtfile, delimiter=';')
        sp = list(reader)
        return sp
    
    
def add_people_txt(man):
    with open('Seminars\Seminar_8\people.txt', 'a', encoding="utf8", newline='') as txtfile:
        writer = writer(txtfile, delimiter=';')
        writer.writerow(man)
        
        
