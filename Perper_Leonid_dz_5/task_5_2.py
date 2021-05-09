"""
Задание 2(вместо задания 1)
Написать генератор нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

"""

ODD_NUM_RANGE = 10

odd_num_gen = (num for num in range(1, ODD_NUM_RANGE + 1, 2))
print(next(odd_num_gen))
print(next(odd_num_gen))
print(next(odd_num_gen))
print(next(odd_num_gen))
print(next(odd_num_gen))
