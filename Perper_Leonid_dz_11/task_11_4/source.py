class Warehouse:
    def __init__(self, max_storage):
        self.max_storage = max_storage
        self.__dict__ = dict()

    def storage(self, item):
        """
        Puts item equipment in storage
        :param item: instance of Equipment class
        :return: None
        """
        if not isinstance(item, Equipment):
            raise ValueError('Object must be Equipment')
        elif self.__dict__.get(type(item)):
            self.__dict__[type(item)].append(item)
        else:
            self.__dict__.update({type(item): [item]})
        print(f'Equipment {item.__dict__["model"]} stored successfully')
        return None

    def issue(self, item_type, item_model, department):
        """
        Transfers item type of <item_type> with attr model=<item_model> from self to <department>
        :param item_type: str 'printer','scanner' or 'xerox'
        :param item_model: str model of item
        :param department: instance of class Warehouse
        :return: None
        """
        if isinstance(department, Warehouse):
            department.storage(self.find_item(item_type, item_model))
            self.write_off(item_type, item_model)
            print(f'Equipment {item_model} was issued successfully')
        else:
            raise TypeError('department must be class Warehouse')
        return None

    def write_off(self, item_type, item_model):
        """
        Discards item type <item_type> with attr model=<item_model> from storage
        :param item_type: str 'printer','scanner' or 'xerox'
        :param item_model: str model of item
        :return: None
        """
        _dict = {'printer': Printer, 'scanner': Scanner, 'xerox': Xerox}
        self.__dict__[_dict[item_type]].remove(self.find_item(item_type, item_model))
        print(f'Equipment {item_model} removed successfully')
        return None

    def show_storage(self):
        """
        shows equipment currently stored on warehouse
        :return: string of lines, separated with '\n'.
                Each line has structure <type of equipment>: <equip_1_model>; <equip_2_model>;...
        """
        _ls = list()
        for key, value in self.__dict__.items():
            _str = ':'.join([str(key), ';'.join([item.__dict__['model'] for item in value])])
            _ls.append(_str)
        return '\n'.join(_ls)

    def find_item(self, item_type, item_model):
        """
        Searches for item type <item_type> with attr model=<item_model> in self
        :param item_type: str 'printer','scanner' or 'xerox'
        :param item_model: str model of item
        :return: item of Equipment class, None if no such item in storage
        """
        _dict = {'printer': Printer, 'scanner': Scanner, 'xerox': Xerox}
        for equip in self.__dict__[_dict[item_type]]:
            if equip.__dict__['model'] == item_model:
                return equip
        return None


class Department(Warehouse):
    pass


class Equipment:
    __params = {'model': str, 'serial_num': int, 'paper_size': str}

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return '; '.join([f'{key}: {value}' for key, value in self.__dict__.items()])

    @staticmethod
    def check_params(params_dict, template):
        if not set(params_dict.keys()) == set(template.keys()):
            raise ValueError(f'Expected parameters: {template.keys()}')
        else:
            for key in template.keys():
                if not isinstance(params_dict[key], template[key]):
                    raise ValueError(f'{key} must be {template[key]}')

    @classmethod
    def get_params(cls):
        return cls.__params


class Printer(Equipment):
    __params = Equipment.get_params().copy()
    __params.update({'color': bool})

    def __init__(self, **kwargs):
        Equipment.check_params(kwargs, self.__params)
        super().__init__(**kwargs)


class Scanner(Equipment):
    __params = Equipment.get_params().copy()
    __params.update({'dpi': int})

    def __init__(self, **kwargs):
        Equipment.check_params(kwargs, self.__params)
        super().__init__(**kwargs)


class Xerox(Equipment):
    __params = Equipment.get_params().copy()
    __params.update({'dpi': int, 'color': bool})

    def __init__(self, **kwargs):
        Equipment.check_params(kwargs, self.__params)
        super().__init__(**kwargs)
