# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,
# а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.

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


neighbor_car = Auto("BMV", 4, "X5", "red", 2200)

neighbor_car.move()
neighbor_car.stop()
print(neighbor_car.age)
neighbor_car.birthday()
print(neighbor_car.age)
print(neighbor_car.color)
print(neighbor_car.weight)



