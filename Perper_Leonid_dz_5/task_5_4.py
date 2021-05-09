"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего.
"""

from time import perf_counter
from random import randint
from sys import getsizeof

SRC_SIZE = 10000


def greater_num(num_list: list):
    """
    Returns a list of numbers that are greater than previous in list
    :param num_list: list of numbers
    :return: list of numbers that are greater than previous in list
    """
    result = []
    for index in range(1, len(num_list)):
        if num_list[index] > num_list[index - 1]:
            result.append(num_list[index])
    return result


src = [randint(0, 1000) for elem in range(SRC_SIZE)]
print(f'Исходный список: {src[:20]}')
print()

# Реализация через цикл for
start = perf_counter()
result_list = greater_num(src)  # Реализация через цикл for
time = perf_counter() - start
print(f'Размер списка-результата: {getsizeof(result_list)}')
print(f'время обработки:{time} сек')
print(result_list[:10])
print()

# Реализация через конструктор списков №1
start = perf_counter()
result_list_constr_1 = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]
time = perf_counter() - start
print(f'Размер списка-результата: {getsizeof(result_list_constr_1)}')
print(f'время обработки:{time} сек')
print(result_list_constr_1[:10])
print()

# Реализация через конструктор списков №2
start = perf_counter()
src_mod = src.copy()
src_mod.pop(0)
src.pop()
result_list_constr_2 = [elem_src for elem_src, elem_tool in zip(src_mod, src) if elem_src > elem_tool]
time = perf_counter() - start
print(f'Размер списка-результата: {getsizeof(result_list_constr_2)}')
print(f'время обработки:{time} сек')
print(result_list_constr_2[:10])
