class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def str(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (self.height + self.width) * 2

    @property
    def is_square(self):
        return self.width == self.height


rect = Rectangle(4, 4)
print("Test rect.str()", rect.str())
print("Test rect.get_area()", rect.get_area())
print("Test rect.get_perimeter()", rect.get_perimeter())
print("Test rect.is_square()", rect.is_square)
