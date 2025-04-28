# Тема: Наслідування

# Задача: Транспортні засоби
# Опис: Створіть базовий клас Transport з методом move(). Створіть підклас відповідно до варіанта
# та реалізуйте метод move().
# 3. Boat

def move():
    print("Transport is moving")


class Transport:
    def __init__(self):
        pass


class Boat(Transport):
    pass

boat = Boat()
move()

# Задача: Тварини
# Опис: Створіть базовий клас Animal з методом make_sound(). Створіть підклас для свого варіанта
# тварини та реалізуйте метод.
# 3. Cow

class Animal:
    def make_sound(self):
        print("The animal make a sound.")

class Cow(Animal):
        pass

cow = Cow()
cow.make_sound()


# Задача: Електронні пристрої
# Опис: Створіть базовий клас Device з методом start(). Створіть підклас для свого варіанта
# пристрою та реалізуйте метод start().
# 3. Tablet

class Device:
    def start(self):
        print("Your device is starting")

class Tablet(Device):
    pass

tablet = Tablet()
tablet.start()


# Тема: Поліморфізм

# Задача: Геометричні фігури
# Опис: Створіть базовий клас Shape з методом area(). Реалізуйте підклас відповідно до варіанта та
# обчисліть площу
# 3. Rectangle

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle1 = Rectangle(4,3)
print(rectangle1.area())