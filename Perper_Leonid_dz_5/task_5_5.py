"""
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
с сохранением порядка их следования в исходном списке.
"""
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 5, 8, 12, 1, 4, 78, 4, 11, 12, 18, 9, 8, 9, 14, 12, 8, 7, 4, 5]

# решение "в лоб"
start = perf_counter()
result = []
for elem in src:
    if src.count(elem) == 1:
        result.append(elem)
time = perf_counter() - start
print(src)
print(f'Результат: {result}', f'Время выполнения: {time} сек', '', sep='\n')

# решение через конструктор списков
start = perf_counter()
result = [elem for elem in src if src.count(elem) == 1]
time = perf_counter() - start
print(f'Результат: {result}', f'Время выполнения: {time} сек', '', sep='\n')

# решение с помощью множеств
start = perf_counter()
unique_set = set()
_tmp = set()
for elem in src:
    if elem not in _tmp:
        unique_set.add(elem)
    else:
        unique_set.discard(elem)
    _tmp.add(elem)
result = [el for el in src if el in unique_set]
time = perf_counter() - start
print(f'Результат: {result}', f'Время выполнения: {time} сек', '', sep='\n')
