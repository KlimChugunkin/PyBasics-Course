"""
Написать скрипт, который собирает все шаблоны из структуры задания 2 в одну папку templates. Исходные файлы необходимо
оставить. Предусмотреть возможные исключительные ситуации.
"""

import os
import shutil

SRC_DIR = 'my_project'
TEMPL_DIR = 'templates'

templates_path = '\\'.join((SRC_DIR, TEMPL_DIR))
os.makedirs(templates_path, exist_ok=True)
for line in os.walk(SRC_DIR):
    if line[0].split('\\')[-1] == TEMPL_DIR and line[0].split('\\')[-2] != SRC_DIR:
        for fold in line[1]:
            src_path = '\\'.join([line[0], fold])
            dst_path = '\\'.join([templates_path, fold])
            try:
                shutil.copytree(src_path, dst_path)
            except FileExistsError:
                print(f'Что такое в "{templates_path}" уже было, наверное')
