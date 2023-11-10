class KgToPoundsV1:
    def __init__(self, kg: float):
        self.__kg = kg

    def get_kg(self) -> float:
        return self.__kg

    def set_kg(self, kg: float):
        self.__kg = kg

    def to_pounds(self) -> float:
        return 2.2 * self.__kg


class KgToPoundsV2:
    def __init__(self, kg: float):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg: float):
        self.__kg = kg

    def to_pounds(self) -> float:
        return 2.2 * self.__kg


test1 = KgToPoundsV1(1)
print('Test get_kg():', test1.get_kg())
test1.set_kg((5))
print('Test set_kg(5):', test1.get_kg())
print('Test to_pounds:', test1.to_pounds())

test2 = KgToPoundsV2(1)
print('Test get_kg():', test2.kg)
test2.kg = 5
print('Test set_kg(5):', test2.kg)
print('Test to_pounds:', test2.to_pounds())
