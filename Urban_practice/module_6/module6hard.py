import math

class Figure:
    def __init__(self, sides, color, filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        return all(0 <= value <= 255 for value in (r, g, b))

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = (r, g, b)
            return self.__color

    def __is_valid_sides(self, new_sides):
        return all(side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(new_sides):
            self.__sides = new_sides

class Circle(Figure):
    sides_count = 1
    def __init__(self, r, g ,b, radius, filled=False):
        color = (r,g,b)
        super().__init__(self.sides_count, color, filled)
        self.__radius = radius

    def get_square(self):
        square = math.pi * (self.__radius ** 2)
        return square

class Triangle(Figure):
    sides_count = 3
    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)

    def get_square(self, a, b, c):
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12
    def __init__(self, r, g, b, sides, filled=False):
        self.sides = sides
        color = (r, g, b)
        super().__init__([sides] * self.sides_count, color, filled)

    def get_volume(self):
        return  self.sides * self.sides * self.sides




circle1 = Circle(200, 200, 100, 10) # (Цвет, стороны)
cube1 = Cube(222, 35, 130, 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())






