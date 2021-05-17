"""
Задание 7
Принимать из командной строки значение суммы продаж и записывть их в файл bakery.csv в кодировке utf-8. Нумерация
записей начинается с 1.
Более подробнаую информацию см. в Readme_bakery.txt
"""

import sys

STORAGE_FILE = 'bakery.csv'
ENTRY_LEN = 25
ERROR_MSG = 'Работа с числами длинной более 13 символов не поддерживается'

sale = sys.argv[1].replace(',', '.')
if len(sale) > 13:
    raise ValueError(ERROR_MSG)
with open(STORAGE_FILE, 'a+', encoding='utf-8') as f:
    if f.tell() == 0:
        entry_num = 1
    else:
        f.seek(f.tell() - ENTRY_LEN)
        entry_num = 1 + int(f.readline().split(';')[0])
    entry = f'{str(entry_num).rjust(10, " ")};{sale.rjust(ENTRY_LEN - 12, " ")}\n'
    f.write(entry)
print('Запись успешно добавлена.')
