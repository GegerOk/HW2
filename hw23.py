class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1000000
    def horse_powers(self):
        return f"This {self.vehicle_type} has {self.horse} horse powers!"
    
class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.horse = 130
        self.vehicle_type = "Nissan"

    def horse_powers(self):
        return f"This {self.vehicle_type} has {self.horse} horse powers!"

if __name__ == "__main__":
    nissan = Nissan()
    print(nissan.vehicle_type, nissan.price)
    print(nissan.horse_powers())
