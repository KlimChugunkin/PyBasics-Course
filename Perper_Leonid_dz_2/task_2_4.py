"""
Задание 4

Вычленить имена сотрудников из данного списка должностей, привести имена к нормальному виду и сформировать фразы
вида "Привет, <имя сотрудника>!" Желательно выполнить задание без создания нового списка.

"""

stuff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
         'директор аэлита']
for i in range(len(stuff)):
    stuff[i] = stuff[i].split(' ')[-1]  # разбиваем элементы stuff на строки по ' ' и берем последний элемент
    stuff[i] = f'Привет, {stuff[i].capitalize()}!'

print(stuff)
