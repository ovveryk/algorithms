class Cat:
    def __init__(self, age):
        self.age = age
        self.value_speed = _set_average_speed()

    def print_age(self):
        print(self.age)

    def _set_average_speed(self):
        if self.age <= 7:
            return 12
        if self.age > 7 and self.age <= 10:
            return 9
        if self.age > 10:
            return 6

#    value_speed = _set_average_speed()
#     Знайти як присвоїти значення приватного метода в змінну класу.
# https://docs.python.org/uk/3.13/tutorial/classes.html#class-and-instance-variables

a = Cat(11)
a.print_age()
print(a.value_speed)


