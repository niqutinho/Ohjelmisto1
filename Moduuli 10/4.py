import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change

        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{self.name} - Current Status")
        print("-" * 60)
        print(f"{'License':<10} {'Max Speed':<10} {'Current Speed':<15} {'Distance':<10}")
        print("-" * 60)
        for car in self.cars:
            print(
                f"{car.license_plate:<10} {car.maximum_speed:<10} {car.current_speed:<15} {car.travelled_distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False