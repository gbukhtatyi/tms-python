class Matrix:
    def __init__(self, numbers: list[list[int]]):
        self.numbers = numbers

    def __str__(self):
        'Переопределить метод __str__'
        result = '';
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers[0])):
                result += str(self.numbers[i][j]) + ' '
            result = result.strip() + '\n'
        return result

    def __add__(self, other):
        'Сложение'
        return self.__class__([
            [cell + other.get_number(i, k) for k, cell in enumerate(row)] for i, row in enumerate(self.numbers)
        ])

    def __sub__(self, other):
        'Вычитание'
        return self.__class__([
            [cell - other.get_number(i, k) for k, cell in enumerate(row)] for i, row in enumerate(self.numbers)
        ])

    def __mul__(self, number):
        'Умножение'
        return self.__class__([[cell * number for cell in row] for row in self.numbers])

    def transpose(self):
        'Транспонирование'
        return self.__class__([
            [self.get_number(k, i) for k, cell in enumerate(row)] for i, row in enumerate(self.numbers)
        ])

    def __eq__(self, other):
        for i, row in enumerate(self.numbers):
            if len(row) != len(other.get_row(i)):
                return False
            for k, cell in enumerate(row):
                if cell != other.get_number(i, k):
                    return False

        return True

    def get_row(self, m: int):
        return self.numbers[m] if self.numbers[m] else []

    def get_number(self, m: int, n: int):
        return self.numbers[m][n] if self.numbers[m] and self.numbers[m][n] else 0

    def create_matrix(self, m: int, n: int, value: int) -> "Matrix":
        matrix = [];
        for i in range(m):
            row = []
            for j in range(n):
                row.append(value)
            matrix.append(row)
        return self(matrix)

    @classmethod
    def create_zero_matrix(self, m: int, n: int) -> "Matrix":
        'Создает единичную матрицу размером m, n'
        return self.create_matrix(self, m, n, 0)

    @classmethod
    def create_one_matrix(self, m: int, n: int) -> "Matrix":
        'Создает нулевую матрицу размером m, n'
        return self.create_matrix(self, m, n, 1)

    @classmethod
    def craete_diagonal_matrix(self, numbers: list[int]) -> "Matrix":
        'Создает диагональную матрицу из переданного списка'
        matrix = [];
        for i in range(len(numbers)):
            row = []
            for j in range(len(numbers)):
                if i == j:
                    row.append(numbers[i])
                else:
                    row.append(0)
            matrix.append(row)
        return self(matrix)

    def get_size(self) -> tuple:
        'Возвращает размерность матрицы'
        return len(self.numbers), len(self.numbers[0])

    def get_amount(self) -> tuple:
        'Возвращает кол-во элементов в матрице'
        m, n = self.get_size()
        return m * n

    def get_sum(self) -> int:
        'Возвращает сумму всех элементов матрицы'
        return sum([sum(row) for row in self.numbers])

    def except_negative(self) -> "Matrix":
        'Возвращает новую матрицу, где вместо отрицательных чисел стоят нули'
        result = []
        for i in range(len(self.numbers)):
            row = []
            for j in range(len(self.numbers[0])):
                if self.numbers[i][j] < 0:
                    row.append(0)
                else:
                    row.append(self.numbers[i][j])
            result.append(row)

        return self.__class__(result)


matrix = Matrix([[-1, 3, 2], [0, 1, 3], [-2, 2, 4]])
second_matrix = Matrix([[0, 0, 0], [1, 1, 1], [2, 2, 2]])

print('Исходная матрица')
print(matrix)

print('Сложение матриц (только одинаковых размерностей)')
print(matrix + second_matrix)

print('Вычитание матриц')
print(matrix - second_matrix)

print('Умножение матрицы на число 2')
print(matrix * 2)

print('Транспонирование матрицы')
print(matrix.transpose())

print('Создает единичную матрицу размером m, n')
zero_matrix = Matrix.create_zero_matrix(3, 4)
print(zero_matrix)

print('Создает единичную матрицу размером m, n')
one_matrix = Matrix.create_one_matrix(3, 4)
print(one_matrix)

print('Создает диагональную матрицу из переданного списка')
diagonal_matrix = Matrix.craete_diagonal_matrix([3, 4, 5, 6])
print(diagonal_matrix)

print('Возвращает размерность матрицы')
print(matrix.get_size())

print('Возвращает кол-во элементов в матрице')
print(matrix.get_amount())

print('Возвращает сумму всех элементов матрицы')
print(matrix.get_sum())

print('Возвращает новую матрицу, где вместо отрицательных чисел стоят нули')
print(matrix.except_negative())

print('Возможность сравнения на равенство двух матриц')
print(matrix == second_matrix)
