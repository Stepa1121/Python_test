class People:
    __people = dict()

    def __init__(self, name, age, orientation):
        self.__name = name
        self.__age = age
        self.__orientation = orientation
        People.__people[name] = self

    def __setattr__(self, key, value):  # Function for checking user data
        if key in ['_People__name', '_People__age', '_People__orientation']:
            if key == '_People__orientation' and value.lower() not in ['men', 'women']:
                if key == '_People__name' and value.isalpha():
                    self.__dict__[key] = value
                else:
                    raise TypeError('Invalid value')
            elif key == '_People__age' and isinstance(value, int) and 0 <= value <= 100:
                self.__dict__[key] = value
            else:
                ValueError('Invalid value')
        else:
            raise AttributeError('You cannot create new attributes')

    def change_user(self):  # Function for changing user data
        __user = input('Enter the number:\n1 - change name\n2 - change age\n3-change direction')
        if __user == 1:
            self.__name = input('Enter the name: ')
        elif __user == 2:
            self.__age = input('Enter the age: ')
        else:
            raise ValueError('Invalid value')

    def __add__(self, other):  # Function for crossing users
        if self.__orientation != other.__orientation:
            create_person(age=0)

    def delete_user(self):
        print('User was delete')
        del People.__people[self.__name]

    @staticmethod
    def show_people():
        print(*People.__people)


def create_person(name=input(), age=int(input()), orientation=input()):
    People(name, age, orientation)


user = int(input())
while user == 1:
    create_person()
    user = int(input())





