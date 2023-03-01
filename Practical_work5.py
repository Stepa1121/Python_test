class People:
    __people = []

    def __init__(self, name=input(), age=int(input()), orientation=input()):
        self.__name = name
        self.__age = age
        self.__orientation = orientation

    def __setattr__(self, key, value):
        if key in ['_People__name', '_People__age', '_People__orientation']:
            if key == '_People__orientation' and value.lower() not in ['men', 'women']:
                self.__dict__[key] = value
            elif key == '_People__age' and isinstance(value, int) and 0 <= value <= 100:
                self.__dict__[key] = value
            else:
                ValueError('Invalid value')
        else:
            raise AttributeError('You cannot create new attributes')
        People.__people.append(self.__name)

    def change_user(self):
        __user = input('Enter the number:\n1 - change name\n2 - change age\n3-change direction')
        if __user == 1:
            self.__name = input('Enter the name: ')
        elif __user == 2:
            self.__age = input('Enter the age: ')
        else:
            raise ValueError('Invalid value')

    def __add__(self, other):
        if self.__orientation != other.__orientation:
            People()

    def delete_user(self):
        print('User was delete')
        People.__people.remove(self.__name)

    @staticmethod
    def show_people():
        print(*People.__people)


user1 = People('Stepa', 18, )
