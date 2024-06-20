class Vehicle():
    def __init__(self, owner):
        self.owner = owner
        self.__model = 'Basic'
        self.__engine_power = 200
        self.__color = 'Black'
        self.__COLOR_VARIANTS = ['black', 'red', 'blue']
    def get_model (self):
        print (f'Model is: {self.__model}\n')
    def get_horsepower (self):
        print (f'Horse power: {self.__engine_power}\n')
    def get_color (self):
        print (f'Color is: {self.__color}\n')  
    def get_info (self):
        print (f'Model is {self.__model}\n')
        print (f'Horse power: {self.__engine_power}\n')
        print (f'Color is: {self.__color}\n')
        print (f'Owner is: {self.owner}\n')  
    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print('Нельзя сменить на новый цвет\n')

class Sedan(Vehicle):
    def __init__(self, owner):
        super().__init__(owner) # Без данной команды наследования не происходит
        self.__PASSENGER_LIMIT = 5
        self.owner = owner

G8 = Sedan('Nick')
G8.get_color()
G8.set_color('blue')
G8.set_color('purple')
G8.get_color()
G8.get_horsepower()
G8.get_model()
G8.get_info()
G8.owner = ('Nikc')
G8.get_info()