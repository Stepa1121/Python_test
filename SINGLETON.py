class Point:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance  is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            raise ValueError('You can created just one atribute')

    def __del__(self):
        Point.__instance = None

    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def information(self):
        print(f"My name is {self.name}, I'm {self.age} years old and I am work as a {self.profession}")


p1 = Point('Stepa', '18', 'developer')
p1.information()




