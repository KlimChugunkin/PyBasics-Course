"""
Задание 2
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных, вводимых
пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    divider = input('Введите делитель для числа 1024: ')
    if divider == '0':
        raise MyZeroDivisionError('Делить на ноль нельзя')
except MyZeroDivisionError as err:
    print(err)
else:
    print(f'Результат операции 1024/{divider} = {1024 / float(divider)}')
