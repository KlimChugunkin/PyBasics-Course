"""
Задача 2 (вместо задачи 1)
Написать функцию num_translate_adv(), переводящую числительные от 0 до 10 c английского на русский язык,
Если перевод сделать невозможно, вернуть None. Реализовать корректную работу с числительными, начинающимися с заглавной
буквы — результат тоже должен быть с заглавной.

"""


def num_translate_adv(number: str):
    """
    Перевод числительных от 0 до 10 с английского на русский
    :param number: чилительное на английском (str)
    :return: чилительное на русском (str)
    """
    num_eng_to_rus = {
                      'zero': 'ноль',
                      'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять'
                      }
    if number.istitle():
        return num_eng_to_rus.get(number.lower()).capitalize()
    else:
        return num_eng_to_rus.get(number)


test_list = ['zero', 'Four', 'not a key']
for some_str in test_list:
    print(num_translate_adv(some_str))
