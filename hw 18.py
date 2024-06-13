class House:
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"Теперь в доме {floors} этажей.")
house = House()
house.setNewNumberOfFloors(3)
input()