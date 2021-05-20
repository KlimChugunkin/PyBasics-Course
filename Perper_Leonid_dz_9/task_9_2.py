"""
Задание 2
Реализовать класс Road (дорога).
 - определить атрибуты: length (длина), width (ширина);
 - значения атрибутов должны передаваться при создании экземпляра класса;
 - атрибуты сделать защищёнными;
 - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
 - использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
"""


class Road:
    _length = 0
    _width = 0
    __thick = 5
    __mass_cm = 25

    def __init__(self, length_input, width_input):
        self._length = length_input
        self._width = width_input

    def calc_mass(self):
        return self._width * self._length * self.__thick * self.__mass_cm * 0.001


road = Road(5000, 5)
print(road.calc_mass(), ' tons')
