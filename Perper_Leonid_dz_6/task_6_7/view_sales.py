"""
Задание 7
Для чтения данных реализовать в командной строке следующую логику:
 - просто запуск скрипта — выводить все записи;
 - запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
 - запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
   числу, включительно.

Более подробнаую информацию см. в Readme_bakery.txt
"""

import sys

STORAGE_FILE = 'bakery.csv'
ENTRY_LEN = 25


def moove_carret(entry_num, file):
    carret_pos = (entry_num - 1) * (ENTRY_LEN + 1)
    if carret_pos > (file.seek(0, 2) - ENTRY_LEN - 1):
        print(f'Записи с номером {entry_num} не суцествует')
        sys.exit(1)
    file.seek(carret_pos)


args = sys.argv[1:3]
with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
    if not args:
        for line in f:
            print(line, end='')
    elif len(args) == 1:
        moove_carret(int(args[0]), f)
        for line in f:
            print(line, end='')
    else:
        moove_carret(int(args[0]), f)
        for line in f:
            print(line, end='')
            if int(line.split(';')[0]) >= int(args[1]):
                break
