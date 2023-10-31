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


class Truck(Auto):
    def __init__(
            self,
            max_load: int,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        print('load')


class Car(Auto):
    def __init__(
            self,
            max_speed: int,
            *args,
            **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.max_speed = max_speed

    def move(self):
        super().move()
        print('max speed is', self.max_speed)


car1 = Car(100, 'Brand1', 'Mark1', 1)
car2 = Car(160, 'Brand2', 'Mark2', 2)
truck1 = Truck(1, 'Brand3', 'Mark3', 3)
truck2 = Truck(2, 'Brand4', 'Mark4', 4)

for auto in car1, car2, truck1, truck2:
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
