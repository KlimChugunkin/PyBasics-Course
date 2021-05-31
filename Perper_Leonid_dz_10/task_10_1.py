"""
Задание 1

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, *args):
        self.check_matrix(*args)
        self.__rows = [el for el in args]

    def __str__(self):
        matrix_str = []
        for row in self.__rows:
            str_row = ' '.join([str(elem) for elem in row])
            matrix_str.append(str_row)
        return '\n'.join(matrix_str)

    def __add__(self, other):
        if self.get_size() != other.get_size():
            raise MatrixError('Both summands must have the same size')
        _list = [[elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
                 for row1, row2 in zip(self.__rows, other.__rows)]
        return Matrix(*_list)

    def get_size(self):
        return len(self.__rows[0]), len(self.__rows)

    @staticmethod
    def check_matrix(*args):
        try:
            column_num = len(args[0])
        except TypeError:
            raise MatrixError('Object can not be interpreted as matrix row')
        for row in args:
            if not isinstance(row, list) or len(row) != column_num:
                raise MatrixError('Rows must have equal length')


class MatrixError(Exception):
    def __init__(self, text):
        self.txt = text


matrix_1 = Matrix([1, 1, 1, 1],
                  [2, 2, 2, 2],
                  [3, 3, 3, 3])

matrix_2 = Matrix([4, 4, 4, 4],
                  [5, 5, 5, 5],
                  [6, 6, 6, 6])
matrix_3 = matrix_1 + matrix_2
print(matrix_1, matrix_2, matrix_3, type(matrix_3), sep='\n\n')
