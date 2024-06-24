class Vehicle():
    __COLOR_VARIANTS = ['black', 'red', 'blue']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

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
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color) # Без данной команды наследования не происходит
        self.__PASSENGER_LIMIT = 5
        self.owner = owner


G8 = Sedan('Nick', 'basic', 200, 'black')
G8.get_color()
G8.set_color('blue')
G8.set_color('purple')
G8.get_color()
G8.get_horsepower()
G8.get_model()
G8.get_info()
G8.owner = 'Nikc'
G8.get_info()
