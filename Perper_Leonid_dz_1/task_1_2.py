"""
Задание 2
Вычислить сумму кубов тех нечетных чисел от 0 до 1000, сумма цифр которых
делится на 7
"""
BASE = 10  # основание системы счичления


def is_divides(number, divider=7):  # возвращает True, если число делится на divider(по умолчанию 7)
    if number % divider == 0:
        return True
    return False


def fig_sum(number):  # возвращает сумму цифр числа
    result = 0
    digit = 0  # текущий разряд числа
    while number//(BASE ** digit) != 0:
        result += (number % (BASE ** (digit + 1))) // (BASE ** digit)
        digit += 1
    return result


# Задание а)


odd_cubes = []
for num in range(1, 1000, 2):
    odd_cubes.append(num ** 3)
print("Список кубов чисел от 1 до 1000:", odd_cubes)
cubes_sum = 0
for num in odd_cubes:
    if is_divides(fig_sum(num)):
        cubes_sum += num
print("Сумма чисел, сумма цифр которых делится на 7:", cubes_sum)

# Задание b) К каждому числу исходного списка прибавить 17 и вычислить сумму, аналогично заданию а)

odd_cubes_mod = []
for num in odd_cubes:
    num += 17
    odd_cubes_mod.append(num)
cubes_sum = 0
print('\nМодифицированный список (+17 к каждому элементу):', odd_cubes_mod)
for num in odd_cubes_mod:
    if is_divides(fig_sum(num)):
        cubes_sum += num
print("Сумма чисел, сумма цифр которых делится на 7:", cubes_sum)

# Задание c) - аналогично b), но без создания нового списка
cubes_sum = 0
for i in range(len(odd_cubes)):
    odd_cubes[i] += 17
    if is_divides(fig_sum(odd_cubes[i])):
        cubes_sum += odd_cubes[i]
print('\nМодифицированный список (+17 к каждому элементу):', odd_cubes)
print("Сумма чисел, сумма цифр которых делится на 7:", cubes_sum)