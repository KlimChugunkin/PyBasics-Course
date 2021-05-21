"""
Задание 5
Реализовать класс Stationery (канцелярская принадлежность):
- определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
- создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
- в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
  сообщение;

Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationary:
    title = 'Принадлежность'

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки маркером')


test_0 = Stationary('Кисть')
test_1 = Pen('Карандаш')
test_2 = Pencil('Карандаш')
test_3 = Handle('Маркер')
test_0.draw()
test_1.draw()
test_2.draw()
test_3.draw()
