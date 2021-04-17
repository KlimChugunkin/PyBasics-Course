"""
Задание 5

Создать вручную список, содержащий цены на товары.
a) Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
b) Вывести цены, отсортированные по возрастанию, новый список не создавать
c) Создать новый список, содержащий те же цены, но отсортированные по убыванию
d) Вывести цены пяти самых дорогих товаров.

"""


def get_str_price(price):   # возвращает строку формата '<r> руб <kk> коп' полученную из float price
    ruble = str(int(price // 1))
    kop = str(int(price % 1 * 100))
    return f'{ruble} руб {kop.zfill(2)} коп'


goods = [34.5, 65.89, 45, 12.07, 41.8, 55.92, 23, 48.56, 96.34, 11.72, 15, 89.6]

# Задание а)
prices_list = []
for price in goods:
    prices_list.append(get_str_price(price))
print(', '.join(prices_list))

# Задание b)

print(f'id списка до сортировки: {id(prices_list)}')
prices_list.sort()
print('Отсортированный список:',  ', '.join(prices_list))
print(f'id списка после сортировки: {id(prices_list)}')

# Задание с)
prices_list_reverse = sorted(prices_list, reverse=True)
print('Cписок отсортированный в обратном порядке', ', '.join(prices_list_reverse))

# Задание d)
print('5 самых дорогих товаров:', ', '.join(prices_list[-5:]))
