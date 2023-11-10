class Soda:
    def __init__(self, additive: str = ""):
        self.additive = additive

    def show_my_drink(self) -> str:
        if len(self.additive) > 0:
            print('Газировка и', self.additive)
        else:
            print('Обычная газировка')


print('Тест без добавки:')
simpleSoda = Soda()
simpleSoda.show_my_drink()

print('Тест с добавкой:')
customSoda = Soda("виски")
customSoda.show_my_drink()
