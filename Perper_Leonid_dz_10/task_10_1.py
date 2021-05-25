"""
Задание 1

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""

class Matrix:
    def __init__(self, *rows):
        self.check_matrix(rows)
        self.__rows = [el for el in rows]

    @staticmethod
    def check_matrix(*rows):
        try:
            column_num = len(rows[0])
        except TypeError:
            raise MatrixError('Object can not be interpreted as matrix row')
        for row in rows:
            if not isinstance(row, list) and (len(row) == column_num)):
                raise MatrixError('Rows must have equal length')


class MatrixError(Exception):
    pass


matr_1 = Matrix([1, 2, 3], [4, 5, 6])