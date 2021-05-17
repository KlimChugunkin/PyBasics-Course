"""
Задание 3
Написать декоратор для логирования типов позиционных аргументов функции. Если аргументов несколько - выводить данные о
каждом через запятую. Вывести тип значения функции. Решить задачу для именованных аргументов. Замаскировать работу
декоратора. Вывести имя функции.
"""


def type_logger(func):
    def wrapper(*args, **kwargs):
        func(*args)
        args_list = []
        for arg in args:
            args_list.append(f'{arg}: {type(arg)}')
        print(*args_list, sep=', ')
        return
    return wrapper


@type_logger
def print_line(*args):
    print(*args, sep='\n')


print_line('have', 'a', 'good', 'day', 5)
