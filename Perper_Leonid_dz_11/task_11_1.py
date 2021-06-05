"""
Задание 1
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

from re import match


class Date:
    def __init__(self, data: str):
        self.get_values(data)

    @classmethod
    def get_values(cls, data: str):
        if match(r'^\d{2}-\d{2}-\d{4}$', data):
            data_parsed = [int(elm) for elm in data.split('-')]
        else:
            raise ValueError('Date doesn\'t match pattern "dd-mm-yyyy"')
        Date.validate_values(data_parsed[0], data_parsed[1], data_parsed[2])
        cls.day, cls.month, cls.year = data_parsed

    @staticmethod
    def validate_values(day: int, month: int, year: int):
        if not 0 < day <= 31:
            raise ValueError('Day value out of range')
        elif not 0 < month <= 12:
            raise ValueError('Month value out of range')
        elif year > 2300:
            raise ValueError('Year value out of range')


date_test_list = ['31-05-2002', '3105-2002', '32-05-2002', '31-13-2002', '31-05-5687']
for element in date_test_list:
    try:
        date_test = Date(element)
        print(date_test.day, date_test.month, date_test.year, sep='/')
    except ValueError as err:
        print(err)
