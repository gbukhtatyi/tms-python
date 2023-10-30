class Point:
    def __init__(
            self,
            x: int,
            y: int
    ):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def subtraction(self, circle: "Circle"):
        result = abs(self.radius - circle.radius)
        return result if result > 0 else Point(0, 0)


c1 = Circle(10)
c2 = Circle(20)
print('Subtraction for C1 - 10, C2 - 20')
print(c1.subtraction(c2))

c1 = Circle(10)
c2 = Circle(10)
print('Subtraction for C1 - 10, C2 - 10')
print(c1.subtraction(c2))
