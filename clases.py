class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_seconds(self, n):
        print(f"add seconds: {n}")

    def subtract_seconds(self, n):
        print("subtract seconds")

    def display(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")


my_watch = Time(2, 12, 34)
my_watch.display()
