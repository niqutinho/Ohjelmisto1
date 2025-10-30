class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            return

        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Hissi on nyt kerroksessa {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Hissi on nyt kerroksessa {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(elevator_count):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, target_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            return

        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("PALOHÄLYTYS! Kaikki hissit siirtyvät alas!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)