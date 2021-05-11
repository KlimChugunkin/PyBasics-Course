"""
Задание 7
Редактировать записи файла bakery.csv, принимая из командной строки номер записи и новое значение. Нумерация записей
начинается с 1.
Более подробнаую информацию см. в Readme_bakery.txt
"""

import csv
import sys

STORAGE_FILE = 'bakery.csv'
args = [1, '178,7']
with open(STORAGE_FILE, 'r+', encoding='utf-8', newline='') as f:
    f.seek(0)
    reader = csv.reader(f)
    writer = csv.writer(f)
    #while reader.line_num != args[0]:
    #print(reader.line_num)
    #reader.__next__()
    writer.writerow([args[1]])

