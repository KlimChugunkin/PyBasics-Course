"""
Задание 5.
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков.
Добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках. Сделать аргументы именованными.

"""
from random import choice, sample


def get_jokes(how_many: int, repeats=True):
    """
    генерирует заданное количество шуток из списков слов
    :param how_many: количество шуток
    :param repeats: разрешает повторно использовать слова
    :return: список из заданного количества шуток в виде строк
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    if repeats:
        for _iter in range(how_many):
            jokes_list.append(' '.join([choice(nouns), choice(adverbs), choice(adjectives)]))
    else:
        for noun, adv, adj in zip(sample(nouns, how_many), sample(adverbs, how_many), sample(adjectives, how_many)):
            jokes_list.append(' '.join([noun, adv, adj]))
    return jokes_list


ask_jokes = [[3,  True],
             {'repeats': False, 'how_many': 5}]

print(get_jokes(*ask_jokes[0]))
print(get_jokes(**ask_jokes[1]))
