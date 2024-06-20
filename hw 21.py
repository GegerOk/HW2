class animal:
    def __init__(self, name):
        self.alive = True
        self.Fed = False
        self.name = name

class plant:
    def __init__(self, name, edible):
        self.edible = edible
        self.name = name

class Mamal(animal):
     def eat(self, food):
        if food.edible == True:
             print (f'{self.name} съел {food.name}')
             self.Fed = True
        else:
            print (f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(animal):
    def eat(self, food):
        if food.edible == True:
             print (f'{self.name} съел {food.name}')
             self.Fed = True
        else:
            print (f"{self.name} не стал есть {food.name}")
            self.alive = False   
    pass

class Flower(plant):
    pass

class Fruit(plant):
    pass

apple = Fruit ("Яблоко", True)
Krapiva = Flower("Крапива", False)

Svin = Mamal("Свин")
Svin.eat (apple)
print (Svin.alive)

Wolf = Predator("Волк")
Wolf.eat (Krapiva)
print (Wolf.alive)
