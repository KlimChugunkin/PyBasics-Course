"""
Задание 7
Редактировать записи файла bakery.csv, принимая из командной строки номер записи и новое значение. Нумерация записей
начинается с 1.
Более подробнаую информацию см. в Readme_bakery.txt
"""

import sys

STORAGE_FILE = 'bakery.csv'
ENTRY_LEN = 25
ERROR_MSG = 'Работа с числами длинной более 13 символов не поддерживается'

args = sys.argv[1:]
if len(args[1]) > 13:
    raise ValueError(ERROR_MSG)
with open(STORAGE_FILE, 'r+', encoding='utf-8') as f:
    carret_pos = (int(args[0]) - 1) * (ENTRY_LEN + 1)
    if carret_pos > (f.seek(0, 2) - ENTRY_LEN - 1):
        print(f'Записи с номером {args[0]} не суцествует')
        sys.exit(1)
    f.seek(carret_pos)
    entry = f'{args[0].rjust(10, " ")};{args[1].rjust(ENTRY_LEN - 12, " ")}\n'
    f.write(entry)
    print(f'Запись {args[0]} успешно изменена на {args[1]}')
