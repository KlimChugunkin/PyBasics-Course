"""
Задание 4, 5, 6
Создать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы—
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведённых
типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self, name, max_storage):
        self.name = name
        self.max_storage = max_storage
        self.__dict__ = dict()

    def storage(self, item):
        pass

    def issue(self, item, department):
        pass

    def write_off(self, item):
        pass


class Department:
    def __init__(self, name: str):
        self.name = name


class Equipment:
    def __init__(self, model: str, serial_num: str, in_service: bool):
        self.model = model
        self.serial_num = serial_num
        self.in_service = in_service


class Printer(Equipment):
    def __init__(self, model: str, serial_num: str, in_service: bool, paper_type: str, color: bool):
        super().__init__(model, serial_num, in_service)
        self.paper_type = paper_type
        self.color = color


class Scanner(Equipment):
    def __init__(self, model: str, serial_num: str, in_service: bool, paper_size: str):
        super().__init__(model, serial_num, in_service)
        self.paper_size = paper_size


class Xerox(Equipment, Scanner, Printer):
    pass
