"""
Задание 4
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при хранении
данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Сохранить
объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём значение None. Если наоборот —
выходим из скрипта с кодом «1». Проверить сохранённые данные.

"""
from sys import exit

OUTPUT_FILE_NAME = 'users_hobby.txt'

with open('users.csv', 'r', encoding='utf-8') as users_csv, open('hobby.csv', 'r', encoding='utf-8') as hobby_csv, \
     open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as dest:
    for line in users_csv:
        user = line.strip('\n')
        hobby = hobby_csv.readline().rstrip('\n')
        if not hobby:
            hobby = None
        output_str = f'{user}: {hobby}\n'
        dest.write(output_str)
    if hobby_csv.readline():
        exit(1)
# проверка правильности записи
with open(OUTPUT_FILE_NAME, 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip('\n'))
