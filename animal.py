class Animal(object):
    MATURE_AGE = 5

    name = None
    age = 0

    def __init__(self, name, age=6):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def is_mature(self):
        if self.age >= 18:
            return True
        else:
            return False

    def get_sound(self):
        return None


class Dog(Animal):
    def __srr__(self):
        animal_data = super().__str__()
        return f"species: DOG, {animal_data}"

    def get_sound(self):
        return "hau"


class Cat(Animal):
    def get_sound(self):
        return "meow"
