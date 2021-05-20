"""
Задание 1
Создать класс TrafficLight (светофор):
 - определить у него один атрибут color (цвет) и метод running (запуск);
 - атрибут реализовать как приватный;
 - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
 - продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
   третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в
   указанном порядке (красный, жёлтый, зелёный);
 - проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep, perf_counter


class TrafficLight:
    __color = ''

    def __init__(self):
        pass

    def running(self):
        colors_dict = {'red': ('\033[0;31;0m', 7), 'yellow': ('\033[0;33;0m', 7), 'green': ('\033[0;32;0m', 7)}
        start = perf_counter()
        while (perf_counter() - start) < 60:
            for key, val in colors_dict.items():
                self.__color = key
                print(f'{val[0]} TrafficLight switched to {key} \033[0;0m')
                sleep(val[1])


tr_light = TrafficLight()
tr_light.running()
