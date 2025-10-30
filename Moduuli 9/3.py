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


car = Car("ABC-123", 142)

car.current_speed = 60
car.drive(1.5)
