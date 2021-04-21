"""

Необходимо обработать список из условия задачи — обособить каждое целое число кавычками  и дополнить нулём до двух
целочисленных разрядов. Сформировать из обработанного списка строку.

"""


def framing_quotes(work_list, index):  # Добавляет кавычки впередеи и позади елемента index в work list
    work_list.insert(index, '"')
    work_list.insert(index + 2, '"')


def str_is_signed_digit(string):  # Провекрка, является ли строка числом если первые символы '+' или '-'
    if string[0] == '+' or string[0] == '-':
        if string[1:].isdigit():
            return True
    return False


report_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
while index < len(report_list):
    if report_list[index].isdigit():    # если елемент report_list[index] - число
        report_list[index] = report_list[index].zfill(2)
        framing_quotes(report_list, index)
        index += 4
    elif str_is_signed_digit(report_list[index]):  # если елемент report_list[index] - число с ведущим + или -
        sign = report_list[index][0]
        report_list[index] = report_list[index][1:]     # отделяем числовую часть от знака
        framing_quotes(report_list, index)
        report_list.insert(index + 1, sign)     # вставляем знак перед числовой частью
        report_list[index + 2] = report_list[index + 2].zfill(2)  # дополняем числовую часть ведущим '0'
        index += 5
    else:
        index += 1
print(report_list)
"""
Сборка строки из списка. Так как не все элементы списка разделяются пробелом, применить метод join не получается.
Приходится использовать контагенацию строк.
"""

report_string = ''
for i in range(len(report_list)):
    if report_list[i].isdigit() or report_list[i] == '+' or report_list[i] == '-':
        report_string += report_list[i]
    elif report_list[i] == '"' and report_list[i - 1].isdigit():
        report_string += report_list[i]
    else:
        report_string += ' '+report_list[i]

print(report_string)


