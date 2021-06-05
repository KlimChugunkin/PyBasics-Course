"""
Задание 7
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку методов
сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса (комплексные
числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного результата.
"""


class Complex:
    def __init__(self, real, image=0):
        self.real = real
        self.image = image

    def __str__(self):
        return f'{self.real}+{self.image}i'

    def __add__(self, other):
        _real = self.real + other.real
        _image = self.image + other.image
        return Complex(_real, _image)

    def __mul__(self, other):
        _a1 = self.real
        _b1 = self.image
        _a2 = other.real
        _b2 = other.image
        return Complex((_a1 * _a2 + _b1 * _b2), (_a1 * _b2 + _a2 * _b1))


num = Complex(5, 2)
num1 = Complex(1, 3)
print(num + num1)
print(num * num1)
