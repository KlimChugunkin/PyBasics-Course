"""
Задание 5 (вместо задания 4)
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт, в котором
импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Доработать скрипт: теперь он должен
работать и из консоли.

"""
from sys import argv
from utils.utils import currency_rates

"""
currencies = ['usd', 'gbp', 'euro']
for cur in currencies:
    print(f'{currency_rates(cur)[0]}, {currency_rates(cur)[1]}')
"""

cur = argv[1]
print(f'{currency_rates(cur)[0]}, {currency_rates(cur)[1]}')
