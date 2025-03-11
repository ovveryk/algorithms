class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours + minutes // 60
        self.minutes = minutes % 60
        self.seconds = seconds

    def add_seconds(self, n):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) + n
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60
        print(f"add seconds: {n}")

    def subtract_seconds(self, n):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) - n
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60
        print(f"subtract seconds {n}")

    def display(self):
        print(f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}")


my_watch = Time(0, 90, 0)
my_watch.display()

my_watch.add_seconds(95)
my_watch.display()

my_watch.subtract_seconds(360)
my_watch.display()