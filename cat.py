class Cat:
    def __init__(self, age):
        self.age = age
        self. value_speed = self._set_average_speed()
        self.saturation_level = 0
        self.run_km = 0


    def _set_average_speed(self):
        if self.age <= 7:
            return 12
        if 7 < self.age <= 10:
            return 9
        if self.age > 10:
            return 6

    def _increase_saturation_level(self, value):
        self.saturation_level = self.saturation_level + value

        if self.saturation_level > 100:
            self.saturation_level = 100

    def _reduce_saturation_level(self, value):
        self.saturation_level = self.saturation_level - value

        if self.saturation_level < 0:
            self.saturation_level = 0

    def get_saturation_level(self):
        result = f"Saturation level: {self.saturation_level}" if self.saturation_level > 0 else "Ваша кішка мертва :("
        return result

    def get_average_speed(self):
        return f"Average speed: {self.value_speed}"

    def print_age(self):
        print(self.age)

    def run(self, value):
        if value <= 25:
            self._reduce_saturation_level(2)
        if 25 < value <= 50:
            self._reduce_saturation_level(5)
        if 50 < value <= 100:
            self._reduce_saturation_level(15)
        if 100 < value <= 200:
            self._reduce_saturation_level(25)
        if value > 200:
            self._reduce_saturation_level(50)

        return f"Ваша кішка пробігла {value} кілометрів"


    def food(self, value):
        meal = {"feed": 10, "apple": 5, "milk": 2}
        print(f"{value}:", meal[value])
        self._increase_saturation_level(meal[value])

a = Cat(7)
a.food("feed")



print(a.get_saturation_level())
print(a.run(100))
print(a.get_saturation_level())
print(a.get_average_speed())




