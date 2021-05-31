"""
Задание 7
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку методов
сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса (комплексные
числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
"""


class Complex:
    def __init__(self, real, image=0):
        self.__dict__['real'] = real
        self.__dict__['image'] = image

    def __str__(self):
        return f'{self.__dict__["real"]}+{self.__dict__["image"]}i'

    def __add__(self, other):
        _real = self.__dict__['real'] + other.__dict__['real']
        _image = self.__dict__['image'] + other.__dict__['image']
        return Complex(_real, _image)

    def __mul__(self, other):
        _a1 = self.__dict__['real']
        _b1 = self.__dict__['image']
        _a2 = other.__dict__['real']
        _b2 = other.__dict__['image']
        return Complex((_a1 * _a2 + _b1 * _b2), (_a1 * _b2 + _a2 * _b1))


num = Complex(5, 2)
num1 = Complex(1, 3)
print(num + num1)
print(num * num1)
