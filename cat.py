class Cat:
    def __init__(self, age):
        self.age = age
        self. value_speed = self._set_average_speed()
        self.saturation_level = 0


    def _set_average_speed(self):
        if self.age <= 7:
            return 12
        if 7 < self.age <= 10:
            return 9
        if self.age > 10:
            return 6

    def _increase_saturation_level(self):
       pass

    def _reduce_saturation_level(self):
        pass

    def get_saturation_level(self):
        result = f"Saturation level: {self.saturation_level}" if self.saturation_level > 0 else "Ваша кішка мертва :("
        return result

    def get_average_speed(self):
        pass

    def print_age(self):
        print(self.age)

    def run(self):
        pass

    def food(self):
        pass


a = Cat(1)
a.print_age()
a._increase_saturation_level()
print(a.value_speed)
print(a.saturation_level)
print(a.get_saturation_level())




