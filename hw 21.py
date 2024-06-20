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
            print (f"{self.name} не стал есть  {food.name}")
            self.alive = False

class Predator(animal):
    pass

class Flower(plant):
    pass

class Fruit(plant):
    pass

Cat = Mamal("Кот")
apple = Fruit ("Яблоко", True)
Krapiva = Flower("Крапива", False)
Cat.eat (apple)
print (Cat.alive)
Cat.eat (Krapiva)
print (Cat.alive)
