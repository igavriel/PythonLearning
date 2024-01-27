import names
import random


class Person:
    """
    Person class with random option
    """

    def __init__(self, name=None, age=None, gender=None):
        if not gender:
            self.gender = names.random.choice(['male', 'female'])
        else:
            self.gender = gender.lower()

        if not name:
            self.name = names.get_full_name(self.gender)
        else:
            self.name = name

        if not age:
            self.age = random.randint(1, 100)
        else:
            self.age = age

    def __lt__(self, other):
        if isinstance(other, Person):
            return self.name < other.name
        else:
            raise TypeError("Can't compare Person with non-Person object")

    def __str__(self):
        return f"{self.name}, age: {self.age}, gender: {self.gender}"
