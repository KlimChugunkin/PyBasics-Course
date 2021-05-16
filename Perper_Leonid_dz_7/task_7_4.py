"""
Задание 4
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых
не превышает этой границы, но больше предыдущей.
"""

import os
import sys

SRC_PATH = '.'

file_size_list = [sys.getsizeof('\\'.join([elem[0], file])) for elem in os.walk(SRC_PATH) for file in elem[2]]
result_dict = {}
dict_keys = [10 ** num for num in range(1, 5)]
prev_val = 0
for key in dict_keys:
    val = []
    for item in file_size_list:
        if prev_val <= item < key:
            val.append(item)
    result_dict.update({key: len(val)})
    prev_val = key
print(*result_dict.items(), sep='\n')
