class Car:
    def __init__ (self, license_plate, max_speed):
        self.license_plate=license_plate
        self.max_speed=max_speed
        self.current_speed=0
        self.travelled_distance=0

car=Car("ABC-123", 142)


print(f"License plate: {car.license_plate}")
print(f"Maximum speed: {car.max_speed} km/h")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")