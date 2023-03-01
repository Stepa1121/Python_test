class Point:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print(f"Hello, my name is {self.name} and i'm {self.age} years old")

    def __add__(self, other):
        if type(other) == int:
            return Point(self.age + other, name=input())
        else:
            return Point(self.age + other.age, name=input())

    def __radd__(self, other):
        return self.__add__(other)


a = Point(19, 'Stepa')
b = Point(18, 'Kamilla')
a + b
a + 20
30 + b
