"""
Задание 3
Есть два списка tutors и klasses. Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>).
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None). Доказать, что вы создали именно
генератор. Проверить его работу вплоть до истощения.

"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б',  # '10А', '10Б', '9А'
]
while len(tutors) > len(klasses):
    klasses.append(None)
tuple_generator = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(type(tuple_generator))
for _iter in range(len(tutors) + 1):
    print(next(tuple_generator))
