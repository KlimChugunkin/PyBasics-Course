"""
Задание 4, 5, 6
Создать класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы—
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведённых
типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

from source import Scanner, Printer, Xerox, Warehouse, Department

warhse = Warehouse(50)
sales_dept = Department(3)

item2 = Printer(model='Canon Z0', serial_num=586454, paper_size='A3', color=False)
item1 = Printer(model='HP 2580', serial_num=2588405, paper_size='A4', color=True)
item3 = Scanner(model='Samsung 156', serial_num=246465, paper_size='A2', dpi=300)
item4 = Xerox(model='Xerox 450', serial_num=26558405, paper_size='A3', dpi=600, color=True)
print(item1, item2, item3, item4, sep='\n')
items_list = [item1, item2, item3, item4]
for item in items_list:
    warhse.storage(item)
print(warhse.show_storage())
warhse.write_off('printer', 'HP 2580')
print(warhse.show_storage())
warhse.storage(item1)
print(warhse.show_storage())
warhse.issue('printer', 'Canon Z0', sales_dept)
print(warhse.show_storage())
