import csv


def get_people():
    
    with open('Seminars\Seminar_8\people.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
        return sp


def add_people(man):
    
    with open('Seminars\Seminar_8\people.csv', 'a', encoding="utf8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(man)


def delite_people(number):
    
    with open('Seminars\Seminar_8\people.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        sp = list(reader)
    if number < len(sp):
        del sp[number]
        with open('Seminars\Seminar_8\people.csv', 'w', encoding="utf8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for row in sp:
                writer.writerow(row)
