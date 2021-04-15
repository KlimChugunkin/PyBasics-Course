"""
Задание 0.
Проверка наличия хотя бы одной цифры в строке

"""

user_input = input("Введите номер: ")
incorrect_input = True
while incorrect_input:
    for char in user_input:
        if char.isdigit():
            incorrect_input = False
            break
    else:
        print("Введенный номер не содержит цифр")
        user_input = input("Попробуйте ещё раз: ")

