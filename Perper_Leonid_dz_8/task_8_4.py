"""
Задание 4
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError. Замаскировать работу декоратора.

"""
from functools import wraps


def val_checker(arg_check_func):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if not all([arg_check_func(arg) for arg in args]):
                raise ValueError('Wrong_input')
            return func(*args)
        return wrapper
    return _val_checker


@val_checker(lambda x: 0 < x < 1000)
def calc_sum(*args):
    result = 0
    for num in args:
        result += num
    return result


print(calc_sum(5, 8, 1, 10, 3), calc_sum.__name__, sep=', ')
