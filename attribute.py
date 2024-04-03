import random

class Attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    @classmethod
    def random_value(cls):
        return random.randint(1, 8)