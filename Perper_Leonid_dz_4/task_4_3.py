"""
Задание 3 (вместо задания 2)
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. Функция должна возвращать
результат числового типа, например float. Если в качестве аргумента передали код валюты, которого нет в ответе,
вернуть None.

"""

import requests
from decimal import *
from datetime import datetime


URL_CURRENCY_CBR = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(curr_code: str):
    """
    Returns currency exchange rate in attitude to rubles as float by currency code.
    :param curr_code: currency code, ex.'USD' or 'GBP' <str>
    :return: currency rate <Decimal>, date parsed from API <datetime.date>. Returns 'None' if currency code is not valid
    """
    response_str = requests.get(URL_CURRENCY_CBR).text
    start_index = response_str.find(curr_code.upper())
    if start_index == -1:
        return None
    else:
        response_str_split = response_str[start_index:].partition('<Value>')[2]
        currency_rate_decimal = Decimal(response_str_split.partition('</Value>')[0].replace(',', '.'))
        # currency_rate_float = float(response_str_split.partition('</Value>')[0].replace(',', '.'))
        response_str_split = response_str.partition('Date="')[2]
        date_from_url = datetime.date(datetime.strptime(response_str_split.partition('"')[0],'%d.%m.%Y'))
        # return currency_rate_float, currency_rate_decimal
        return currency_rate_decimal, date_from_url


# print(currency_rates('usd')[0]*100000000000 + 0.0012, Decimal(currency_rates('usd')[1]*10000000000 + Decimal(0.0012)))
print(*currency_rates('usd'))

