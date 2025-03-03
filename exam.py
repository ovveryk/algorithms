class Car:
    def __init__(self, model, year, engine, km):
        self.model = model
        self.year = year
        self.engine = engine
        self.km = km

    def calculate_age (self):
        age = 2025 - self.year
        return age

    def show_model(self):
        print(f"{self.model}")

    def show_average_mileage(self):
        average_mileage = self.km // (2025 - self.year)
        print(average_mileage)
        return average_mileage


my_car = Car("Audi", 1988, 2.0, 200000)
my_car.show_average_mileage()

print(my_car.model)

year = Car("BMW", 2000, 1.6, 12000)
print(year.calculate_age())
my_car.show_model()




