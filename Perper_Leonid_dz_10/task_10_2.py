"""
Задание 2
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
Одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
- для пальто (V/6.5 + 0.5),
- для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.

Выполнить общий подсчёт расхода ткани.

Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""

from abc import ABC, abstractmethod


class ClothesAbstract(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calc_cloth(self):
        pass


class Suit(ClothesAbstract):
    def __init__(self, name: str, height: int):
        super().__init__(name)
        self.height = height

    def calc_cloth(self):
        return self.height * 2 + 0.3


class Coat(ClothesAbstract):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def calc_cloth(self):
        return self.size / 6.5 + 0.5


class Clothes:
    def __init__(self):
        self.items = []
        self._cloth_vol = 0

    def add_item(self, item):
        if isinstance(item, ClothesAbstract):
            self.items.append(item)
        else:
            raise TypeError(f'{item} is not a clothes')

    @property
    def cloth_vol(self):
        self._cloth_vol = 0
        for item in self.items:
            self._cloth_vol += item.calc_cloth()
        return self._cloth_vol


test_1 = Coat('Тройка', 13)
print(test_1.calc_cloth())
clothes = Clothes()
clothes.add_item(test_1)
print(clothes.cloth_vol)
test_2 = Suit('Тройка', 3)
clothes.add_item(test_2)
print(clothes.cloth_vol)
