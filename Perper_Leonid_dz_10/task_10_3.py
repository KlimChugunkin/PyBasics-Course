"""
Задание 3
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка». В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов:
 - сложение (__add__()),
 - вычитание (__sub__()),
 - умножение (__mul__()),
 - деление (__floordiv____truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток соответственно.
 - Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
    клеток.
 - Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
    больше нуля, иначе выводить соответствующее сообщение.
 - Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
 - Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
    ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Этот метод
позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек
между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все
оставшиеся.
"""


class Cell:
    def __init__(self, num: int):
        self.elem_num = num

    def __str__(self):
        return f'Cell of {self.elem_num} elements'

    def __add__(self, other):
        Cell.check_arg(other)
        return Cell(self.elem_num + other.elem_num)

    def __sub__(self, other):
        Cell.check_arg(other)
        result_cell_num = self.elem_num - other.elem_num
        if result_cell_num <= 0:
            raise ValueError(f'Can not subtract {other} form self')
        return Cell(result_cell_num)

    def __mul__(self, other):
        Cell.check_arg(other)
        return Cell(self.elem_num * other.elem_num)

    def __floordiv__(self, other):
        Cell.check_arg(other)
        return Cell(self.elem_num // other.elem_num)

    def __truediv__(self, other):
        return self // other

    def make_order(self, lines_num: int):
        _lines = [str().ljust(lines_num, '*') for _iter in range(self.elem_num // lines_num)]
        if self.elem_num % lines_num:
            _lines.append(str().ljust(self.elem_num % lines_num, '*'))
        return '\n'.join(_lines)

    @staticmethod
    def check_arg(item):
        if not isinstance(item, Cell):
            raise TypeError('Can not perform operation on not a Cell object')


test_item1 = Cell(8)
test_item2 = Cell(3)
print(test_item1, type(test_item1))
print(test_item1.make_order(5))
# add
test_result = test_item1 + test_item2
print(test_result, type(test_result))
# subtract
test_result = test_item1 - test_item2
print(test_result, type(test_result))
# multiply
test_result = test_item1 * test_item2
print(test_result, type(test_result))
# division
test_result = test_item1 / test_item2
print(test_result, type(test_result))
# integer division
test_result = test_item1 // test_item2
print(test_result, type(test_result))
