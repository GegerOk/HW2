class Building:
    def __init__(self, number_of_floors, building_type):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

building1 = Building(3, 'Офисное здание')
building2 = Building(3, 'Офисное здание')
print(building1 == building2)
building1.numberOfFloors = 2
print(building1 == building2)