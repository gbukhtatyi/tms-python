def print_attributes(obj):
    for key in obj.__dict__:
        print(key, ' = ', getattr(obj, key))


class Auto:

    def __init__(
            self,
            brand: str,
            mark: str,
            age: int,
            color: str = None,
            weight: float = None
    ):
        self.brand = brand
        self.mark = mark
        self.age = age
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


auto1 = Auto('Brand1', 'Mark1', 1)
auto2 = Auto('Brand2', 'Mark2', 2)

for auto in auto1, auto1:
    print(f'Checking {auto}..')
    print('State of object before birthday:')
    print_attributes(auto)
    auto.birthday()
    print('State of object after birthday:')
    print_attributes(auto)
    print('Action move:')
    auto.move()
    print('Action stop:')
    auto.stop()
