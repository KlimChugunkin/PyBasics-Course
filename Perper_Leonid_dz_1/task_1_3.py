"""
Задание 3.
Реализовать склонение слова "процент" для чисел до 20
"""


def decline_percent(num):
    if  num == 1:
        return 'процент'
    elif 1 < num < 5:
        return 'процента'
    elif (5 <= num <= 20) or num == 0:
        return 'процентов'


for i in range(21):
    print(i, decline_percent(i))