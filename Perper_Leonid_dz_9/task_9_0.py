"""
Задание 0 (из вебинара)
1 Вынести метод проверки аргументов из класса BirthForm в класс базовая форма
2 Написать свое исключение на нехватку данных для класса
3 Прописать метод get_passport_data для класса MarriageForm:
    Нужно вынуть passport_info из каждого из паспартов и добавить атрибуты к объекту данного класса, такие как
    self.name_1, self.name_2 так далее.

Работаем в МФЦ.
Поддержка различных форм докуметов:
* свидетельство о рождении
* свидетельство о смене работы
* свидетельство о браке
Помним, что все должно быть масштабируемо!
"""
import time


class NotEnoughDataError(Exception):
    pass


class PFR:
    def send_data(self):
        print('Form was sent')

    def update_data(self):
        print('updated')


class BaseForm:
    minimum_info = set()

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        res = [f"{key} : {value}" for key, value in self.__dict__.items()]
        return ', '.join(res)

    def check_data(self):
        if self.minimum_info.difference(set(self.__dict__.keys())):
            raise NotEnoughDataError(f'We need more data! {self.minimum_info.difference(set(self.__dict__.keys()))}')


class Passport(BaseForm):
    minimum_info = frozenset({'name', 'surname', 'age'})


class BirthForm(BaseForm, PFR):
    """
    маленькое повторение: написать свое исключение на нехватку данных
    (выполнено: см class NotEnoughDataError. вызывается методом BaseForm.check_data() )
    """
    minimum_info = frozenset({'name', 'surname', 'birth_date', 'mothers_name', 'fathers_name'})


class MarriageForm(BaseForm):
    """
    Вынести в класс базовая форма метод проверки аргументов
    (выполнено: см. класс BaseForm)
    """
    passport_info = frozenset({"name", "surname", "age"})

    def get_passport_data(self, passport1, passport2):
        """
        Нужно вынуть passport_info из каждого из паспартов и добавить атрибуты к
        объекту данного класса, такие как
        self.name_1, self.name_2 так далее
        (Выполнено)
        """
        passport1.check_data()
        passport2.check_data()
        for key in self.passport_info:
            self.__dict__[f'{key}_1'] = passport1.__dict__[key]
            self.__dict__[f'{key}_2'] = passport2.__dict__[key]

    def update_passport_data(self, passport1, passport2):
        if isinstance(passport1, Passport) and isinstance(passport2, Passport):
            passport1.__dict__['marriage'] = True
            passport2.__dict__['marriage'] = True
        else:
            print('Wrong passports!')


birth_form_test = BirthForm(name='Иван', surname='Петров', fathers_name='Борис', mothers_name='Наташа',
                            birth_date='01.02.2003')
birth_form_test.check_data()


test_user = Passport(name="Basil", surname='Ivanov',
                     birth_date='19/05/1980', mothers_name='Natalia', age=25,
                     fathers_name='Kirill')

test_user1 = Passport(name="Katya", surname='Petrova', age=33,
                      birth_date='19/05/1978', mothers_name='Natalia')

marrige_form1 = MarriageForm()
marrige_form1.get_passport_data(test_user, test_user1)
marrige_form1.update_passport_data(test_user, test_user1)
print(test_user)
print(marrige_form1)
