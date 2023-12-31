class Circle:
    PI = 3.14  # Глобальный атрибут

    def __init__(self, radius: int | float):
        # Создаем новый атрибут для экземпляра класса `Circle`
        self.__radius = radius

    def get_radius(self) -> int | float:
        """
        Геттер `Getter`
        Возвращает значение защищенного атрибута"""
        return self.__radius

    def set_radius(self, radius: int | float):
        """`Setter`"""
        # Что тип radius это либо int, либо float и, если это так и он больше 0
        if isinstance(radius, (int, float)) and radius > 0:
            self.__radius = radius

        # Что тип radius это либо int, либо float и, если это так и он МЕНЬШЕ ИЛИ РАВЕН 0
        elif isinstance(radius, (int, float)) and radius <= 0:
            print("Радиус должен быть больше 0")

        # Что тип radius это НЕ int и НЕ float
        else:
            print(
                f"Для радиуса ожидается тип int или float, был передал {type(radius)}"
            )

    # Вычисляемый атрибут (уже не метод)
    @property
    def area(self) -> int | float:
        return self.PI * self.__radius ** 2

    # Вычисляемый атрибут (уже не метод)
    @property
    def circumference(self) -> int | float:
        return self.PI * 2 * self.__radius


c = Circle(10)

print(c.circumference)  # Теперь обращение без `()` Это уже атрибут!
print(c.area)  # Теперь обращение без `()` Это уже атрибут!

c.set_radius(11)

print(c.circumference)
print(c.area)

print(c.get_radius())
