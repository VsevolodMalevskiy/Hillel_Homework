# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределённый метод move, перед появлением надписи «move» выводит
# надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
# метода move, после появления надписи «move» должна появиться надпись
# «max speed is <max_speed>». Вместо <max_speed> должно выводится значение
# обязательного атрибута max_speed.
# Создать по 2 объекта для каждого из классов truck и car,
# проверить все их методы и атрибуты.

import time

class Auto:
    def __init__(self, brand, age: int, mark, color="white", weight=2000):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight


    def move(self):
        print("Move")


    def stop(self):
        print("Stop")


    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, brand, age: int, mark, max_load, color="white", weight=2000):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load


    def move(self):
        print("attention")
        super().move()


    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age: int, mark, max_speed, color="white", weight=2000):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


car_1 = Car("Opel", 7, "Astra", 216, "black", 1250)
car_2 = Car("Mitsubishi", 1, "Outlander", 188, "brown", 1505)
car_3 = Truck("Volvo", 3, "FH13B", 16000, "red", 14000)
car_4 = Truck("DAF", 6, "95XF380", 11000, "grey", 12000)

print(f"\nАвтомобиль - {car_1.brand} {car_1.mark}, цвет - {car_1.color}, возраст - {car_1.age} лет, "
      f"максимальная скорость - {car_1.max_speed} км/час, собственный вес - {car_1.weight} кг")
car_1.move()
car_1.stop()
car_1.birthday()
print(f"настоящий возраст - {car_1.age}, лет\n")

print(f"\nАвтомобиль - {car_2.brand} {car_2.mark}, цвет - {car_2.color}, возраст - {car_2.age} лет, "
      f"максимальная скорость - {car_2.max_speed} км/час, собственный вес - {car_2.weight} кг")
car_2.move()
car_2.stop()
car_2.birthday()
print(f"настоящий возраст - {car_2.age}, лет")

print(f"\nАвтомобиль - {car_3.brand} {car_3.mark}, цвет - {car_3.color}, возраст - {car_3.age} лет, "
      f"максимальная грузоподъемность - {car_3.max_load} кг, собственный вес - {car_3.weight} кг")
car_3.move()
car_3.stop()
car_3.load()
car_3.birthday()
print(f"настоящий возраст - {car_3.age}, лет\n")

print(f"\nАвтомобиль - {car_4.brand} {car_4.mark}, цвет - {car_4.color}, возраст - {car_4.age} лет, "
      f"максимальная грузоподъемность - {car_4.max_load} кг, собственный вес - {car_4.weight} кг")
car_4.move()
car_4.stop()
car_4.load()
car_4.birthday()
print(f"настоящий возраст - {car_4.age}, лет\n")