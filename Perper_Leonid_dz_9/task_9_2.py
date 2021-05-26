"""
Задание 2
Реализовать класс Road (дорога).
 - определить атрибуты: length (длина), width (ширина);
 - значения атрибутов должны передаваться при создании экземпляра класса;
 - атрибуты сделать защищёнными;
 - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
 - использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной
в 1 см*число см толщины полотна. проверить работу метода.
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__thick = 5
        self.__mass_per_cube = 25

    def calc_mass(self):
        return self._width * self._length * self.__thick * self.__mass_per_cube / 1000


length = 5000
width = 5
road = Road(length, width)
print(f'Масса дорожного покрытия размерами {length} x {width} м - {road.calc_mass()} тонн')
