import random


class Car:
    def __init__(self, license_plate, max_speed):
        self.license_plate = license_plate
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change

        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def race():
    cars = []
    for i in range(1, 11):
        license_plate = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(license_plate, max_speed))

    race_ongoing = True
    while race_ongoing:
        for car in cars:

            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)

            car.drive(1)

            if car.travelled_distance >= 10000:
                race_ongoing = False

    sorted_cars = sorted(cars, key=lambda car: car.travelled_distance, reverse=True)
    return sorted_cars