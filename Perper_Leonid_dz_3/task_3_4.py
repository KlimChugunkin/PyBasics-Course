"""
Задание 4(вместо задания 3)
Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую
словарь, в котором ключи — первые буквы фамилий, а значения — словари, аналогичные данному, но реализовыанные по
первой букве имен и содержащие записи, в которых фамилия начинается с соответствующей буквы.
"""


def thesaurus_adv(*args: str):
    first_names = {}
    for person in args:
        first_name_letter = person.split(' ')[1][0]
        if first_name_letter not in first_names:
            first_names.update({first_name_letter: {person[0]: [person]}})
        else:
            add_second_name(person, first_names[first_name_letter])
    return first_names


def add_second_name(person_str, second_name_dict):
    """
    Дополняет список (value словаря second_name_dict) строчкой person_str,
    либо дополняет словарь  second_name_dict новой парой key: value (первая буква person_str : список строк с
    единственным элементом  person_str)

    :param person_str: строка вида 'Имя Фамилия'
    :param second_name_dict: словарь в котором ключ - первая буква имнеи, значение - список строк вида 'Имя Фамилия'
    :return: None
    """
    if person_str[0] in second_name_dict:
        second_name_dict[person_str[0]].append(person_str)
    else:
        second_name_dict.update({person_str[0]: [person_str]})


test_names = ["Иван Сергеев", "Инна Серова", "Игнат Севриенко", "Анна Савельева",
              "Аверьян Скорый", "Владислав Григорьев", "Валерий Гозлов", "Сергей Горяинов",
              "Савелий Гозман", "Валентина Гинес", 'Иван Иванов']
print(thesaurus_adv(*test_names))
print(sorted(thesaurus_adv(*test_names)))  # Список из отсортированных по возрастанию ключей
