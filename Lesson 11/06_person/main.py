class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    def str(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}"

    def get_name(self):
        return self.name

    @property
    def set_name(self, new_name):
        self.name = new_name

    @staticmethod
    def is_adult(person: "Person"):
        return person.age > 18

    @classmethod
    def create_from_string(self, s):
        name, age, gender = s.split('-')
        age = int(age)
        return Person(name, age, gender)


person = Person.create_from_string("Иван-19-муж")
print('Тест get_name():', person.get_name())
person.name = 'Павел'
print('Тест set_name():', person.get_name())
print('Тест str():', person.str())
print('Тест is_adult:', Person.is_adult(person))
