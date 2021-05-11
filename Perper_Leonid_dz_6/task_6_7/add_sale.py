"""
Задание 7
Принимать из командной строки значение суммы продаж и записывть их в файл bakery.csv в кодировке utf-8. Нумерация
записей начинается с 1.
Более подробнаую информацию см. в Readme_bakery.txt
"""
import csv
import sys

STORAGE_FILE = 'bakery.csv'

sale = sys.argv[1]
with open(STORAGE_FILE, 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([sale])
print('Запись успешно добавлена.')
