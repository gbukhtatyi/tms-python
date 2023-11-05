class TriangleChecker:
    def __init__(self, segments: list[int]):
        self.segments = segments

    def is_triangle(self) -> None:
        if not all(isinstance(segment, int) for segment in self.segments):
            print("Нужно вводить только числа!")
            return False

        if not all(segment > 0 for segment in self.segments):
            print("С отрицательными числами ничего не выйдет!")
            return False

        for a in range(0, len(self.segments) - 2):
            for b in range(a + 1, len(self.segments) - 1):
                for c in range(b + 1, len(self.segments)):
                    side_a = self.segments[a]
                    side_b = self.segments[b]
                    side_c = self.segments[c]
                    if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
                        print("Ура, можно построить треугольник!")
                        return True

        print("Жаль, но из этого треугольник не сделать.")
        return False


print('Test [1, \"test\", 2]:')
checker = TriangleChecker((1, "test", 2))
checker.is_triangle()

print('Test [1, -2, 2]:')
checker = TriangleChecker((1, -2, 2))
checker.is_triangle()
print('Test [1, 2, 2]:')

checker = TriangleChecker((1, 2, 2))
checker.is_triangle()

print('Test [4, 2, 1]:')
checker = TriangleChecker((4, 2, 2))
checker.is_triangle()

print('Test [4, 2, 2, 1]:')
checker = TriangleChecker((4, 2, 2, 1))
checker.is_triangle()
