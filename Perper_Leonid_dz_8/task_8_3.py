"""
Задание 3
Написать декоратор для логирования типов позиционных аргументов функции. Если аргументов несколько - выводить данные о
каждом через запятую. Вывести тип значения функции. Решить задачу для именованных аргументов. Замаскировать работу
декоратора. Вывести имя функции.
"""

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        __name__ = func.__name__
        print(f'Name: {func.__name__}')
        print(*[f'{arg}: {type(arg)}' for arg in args], sep=', ')
        if kwargs:
            print(*[f'{key} = {val}: {type(val)}' for key, val in kwargs.items()], sep=', ')
        return func(*args, **kwargs)
    return wrapper


@type_logger
def divide(*args, divider=10, divider_correct=1, div_zero_correct=False):
    if div_zero_correct and divider == 0:
        divider = divider_correct
    result = []
    for arg in args:
        result.append(arg / divider)
    return result


test_list = [5, 8, 10, 6, 12]
print(divide(*test_list, divider=5, div_zero_correct=True))
print(divide.__name__)
