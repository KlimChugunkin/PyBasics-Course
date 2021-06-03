

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
    """
    takes params: 'model', 'serial_num', 'paper_size'
    """
    __params__ = []

    def __init__(self, **kwargs):
        self.check_params(kwargs, self.__params__)
        self.__dict__.update(kwargs)

    @staticmethod
    def check_params(params_dict, template):
        if not set(params_dict.keys()) == set(template):
            raise ValueError(f'Expected parameters: {template}')


class Printer(Equipment):
    __params__ = ['model', 'serial_num', 'paper_size', 'color']


class Scanner(Equipment):
    __params__ = ['model', 'serial_num', 'paper_size', 'dpi']


class Xerox(Equipment):
    __params__ = ['model', 'serial_num', 'paper_size', 'dpi', 'color']




