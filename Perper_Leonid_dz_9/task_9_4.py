"""
Задание 4
Реализуйте базовый класс Car:
- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
  turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
- для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
  должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self, name, color):
        self.color,  self.name = color, name

    def go(self):
        print(f'Машина {self.name} начала движение')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повренула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость машины {self.name} - {self.speed} км/ч')
        if self.speed > 60:
            print('Внимание! Превышение скорости!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость машины {self.name} - {self.speed} км/ч')
        if self.speed > 40:
            print('Внимание! Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


class SportCar(Car):
    pass


car_1 = TownCar('Matiz', 'yellow')
car_2 = WorkCar('Lanos', 'white')
car_3 = PoliceCar('Focus', 'special')
car_4 = SportCar('Mustang', 'red')
car_list = [car_1, car_2, car_3, car_4]
for car in car_list:
    print(car.name, car.color, car.speed, car.is_police, sep='; ')
speeds = [35, 45, 70]
for car in car_list:
    car.go()
    for sp in speeds:
        car.speed = sp
        car.show_speed()
    car.turn('направо')
    car.turn('налево')
    car.stop()
