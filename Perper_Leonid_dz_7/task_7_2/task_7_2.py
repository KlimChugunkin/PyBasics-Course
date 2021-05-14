"""
Задание 2
Написать скрипт, создающий стартер (заготовку) для проекта со структурой из файла config.yaml
подумайте о ситуации, когда некоторые папки уже есть на диске.
"""

import os
import yaml
from yaml.loader import SafeLoader

CONFIG_FILE = 'config.yaml'
DEST = 'D:\\PyBasics-Course\\Perper_Leonid_dz_7\\task_7_3'

with open('config.yaml', 'r', encoding='utf-8') as yml:
    config_data = tuple(yaml.load(yml, Loader=SafeLoader))
for line in config_data:
    os.makedirs('\\'.join([DEST, line[0]]), exist_ok=True)
    if line[2]:
        files_path = ['\\'.join([DEST, line[0], file_name]) for file_name in line[2]]
        for file in files_path:
            with open(file, 'w') as f:
                pass
