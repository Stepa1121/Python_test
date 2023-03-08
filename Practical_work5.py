class People:
    __people = dict()

    def __init__(self, name, age, orientation):
        self.__name = name
        self.__age = age
        self.__orientation = orientation
        People.__people[name.lower()] = self

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
        if len(People.__people) == 0:
            print('There are no people')
        else:
            print(*People.__people)

    @staticmethod
    def people():
        return People.__people


def combine():
    person1 = input("Please enter the name first person")
    person2 = input("Please enter the name second person")
    if person1 in People.people() and person2 in People.people():
        print(1)
    else:
        print(0)


def create_person(name=input('Enter the name: '),
                  age=int(input('Enter the age: ')),
                  orientation=input('Enter the orientation: ')):
    People(name, age, orientation)


def menu():
    print("1 - Show people\n2 - Combine people\n3 - Create a person\n0 - Close")


print("Hello, let's get started")
menu()
user = int(input("Chose a command: "))
while user in [1, 2, 3, 0]:
    if user == 1:
        People.show_people()
        menu()
        user = int(input('Chose a command: '))
    elif user == 2:
        combine()
        menu()
        user = int(input('Chose a command: '))
    elif user == 3:
        create_person()
        menu()
        user = int(input('Chose a command: '))
    elif user == 0:
        break
    else:
        NameError ("I'm sorry you entered the wrong data! Try again")
        menu()
        user = int(input())








