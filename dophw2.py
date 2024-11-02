import math


class Figure:
    sides_count = 0

    def __init__(self, *sides):
        self.__sides = list(sides)
        self.__color = []
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and \
            0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            print('Цвет изменён')
        else:
            print("Некорректные значения цвета, цвет остается прежним.")

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Некорректные значения сторон или неверное их количество.")


class Circle(Figure):
    sides_count = 1

    def __init__(self, circumference):
        super().__init__(circumference)
        self.__radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def get_square(self):
        s = sum(self._Figure__sides) / 2
        return math.sqrt(s * (s - self._Figure__sides[0]) * (s - self._Figure__sides[1]) * (s - self._Figure__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, side_length):
        super().__init__(*([side_length] * self.sides_count))

    def get_square(self):
        return self._Figure__sides[0] ** 3


circle = Circle(21)
triangle = Triangle(3, 4, 5)
cube = Cube(3)
circle.set_color(255, 0, 0)
print(circle.get_color())
circle.set_color(300, -20, 100)
print(f"Площадь круга: {circle.get_square()}")
print(f"Площадь треугольника: {triangle.get_square()}")
print(f"Объем куба: {cube.get_square()}")
print(f"Периметр круга: {len(circle)}")
print(f"Периметр треугольника: {len(triangle)}")
print(f"Периметр куба: {len(cube)}")

cube.set_sides(5, 3, 12, 4, 5)
print(cube.get_sides())
circle.set_sides(2)
print(circle.get_sides())
