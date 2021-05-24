"""
Задание 3
Реализовать базовый класс Worker (работник):
- определить атрибуты: name, surname, position (должность), income (доход);
- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например,
  {"wage": wage, "bonus": bonus};
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учётом премии (get_total_income).
Проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': 2000, 'bonus': 1500}

    def get_income(self):
        return self.__income['wage'], self.__income['bonus']


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self.get_income()[0] + self.get_income()[1]


posit = Position('Josef', 'Weiss', 'driver')
print(posit.name, posit.surname, posit.position, sep=', ')
print(posit.get_full_name())
print(posit.get_total_income())
