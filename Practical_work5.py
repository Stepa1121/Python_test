class People:
    def __init__(self, name, age, direction):
        self.__name = name
        self.__age = age
        self.__direction = direction

    def __setattr__(self, key, value):
        if key in ['_People__name', '_People__age', '_People__direction']:
            self.__dict__[key] = value
        else:
            raise AttributeError('You cannot create new attributes')

    def change_user(self):
        __user = input('Enter the number:\n1 - change name\n2 - change age\n3-change direction')
        if __user == 1:
            self.__name = input('Enter the name: ')
        elif __user == 2:
            self.__age = input('Enter the age: ')
        elif __user == 3:
            self.__direction = input('Enter the direction: ')
        else:
            raise 