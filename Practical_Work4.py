"""
Develop a class in which only 20 objects can be created.
Each object has information in the form of: "Name", "Last Name", "Age" and "Direction"
"""


class People:  # A  class for created a people
    __names = 0

    def __init__(self, name, last_name, age, direction):
        self.name = name.title()
        self.last_name = last_name.title()
        self.age = age
        self.direction = direction.title()
        People.__names += 1

    def __del__(self):
        print(f'{self.name.title()} {self.last_name.title()} has been removed')
        People.__names -= 1

    def get_person(self):  # A function for displaying information about a person
        print(f'Name: {self.name.capitalize()}\n'
              f'Last Name: {self.last_name.capitalize()}\n'
              f'Age: {self.age}\n'
              f'Direction: {self.direction.capitalize()}')

    @staticmethod  # A function for displaying the numbers of seats
    def len_list_names():
        print(f'Used {People.__names} names out of 20')


def create_person(name, last_name, age, direction):
    """
    A function for creating a new instance of a class and adding it to the dictionary
    """
    peoples[(name, last_name)] = People(name, last_name, age, direction)
    print("The person has been added successfully")


def view_person():
    k = True
    while k:
        answer1 = int(input('Shall all people or just one?\n1-All\n0-One\n'))
        if answer1 == 0:
            name = input('Enter a name: ').lower().strip()
            last_name = input('Enter a last name: ').lower().strip()
            if (name, last_name) in peoples.keys():
                peoples[(name, last_name)].get_person()
                input()
                k = input('Do you want to continue?\nAnswer: ').lower().strip()
                if k == 'yes':
                    k = True
                else:
                    k = False
            else:
                k = input('Sorry, but such person is not on the list. Will you try again?\nAnswer: ').lower().strip()
                if k == 'yes':
                    k = True
                else:
                    k = False
        else:
            for x in peoples.keys():
                peoples[x].get_person()
                print()
            k = input('Do you want to continue?\nAnswer: ').lower().strip()
            if k == 'yes':
                k = True
            else:
                k = False


def delete_person():  # A function for deleting an object
    k = True
    while k:
        name = input('Enter the name: ').lower().strip()
        last_name = input('Enter the last name: ').lower().strip()
        if (name, last_name) in peoples.keys():
            del peoples[(name, last_name)]
            input()
            k = input('Do you want to continue?\nAnswer: ').lower().strip()
            if k == 'yes':
                k = True
            else:
                k = False
        else:
            k = input('Sorry, but such person is not on the list. Will you try again?\nAnswer: ').lower().strip()
            if k == 'yes':
                k = True


def create_list_person():  # A function for filling in the list of people
    k = True
    while k:
        name = input('Enter the name: ').lower().strip()
        last_name = input('Enter the Last_name: ').lower().strip()
        if (name, last_name) not in peoples.keys():
            age = int(input('Enter a age: '))
            direction = input('Enter a direction: ').lower()
            create_person(name, last_name, age, direction)
            input()
            k = input('Do you want to continue?\nAnswer: ').lower().strip()
            if k == 'yes':
                k = True
            else:
                k = False
        else:
            k = input('Sorry, but there is already such a person, do you want to continue?\nAnswer: ')
            if k == 'yes':
                k = True
            else:
                k = False


peoples = {}
print("Hello, it is a program for creating a list of people.\nLets get started.\n")
f = True
while f:
    print('Commands:\n'
          '"Create a new person"\n'
          '"Delete a person"\n'
          '"Number of seats"\n'
          '"View information"\n'
          '"Close"')
    user = input('Command: ').lower()
    if user == 'create a new person':
        create_list_person()
    elif user == 'delete a person':
        delete_person()
    elif user == 'number of seats':
        People.len_list_names()
        input()
    elif user == 'view information':
        view_person()
    elif user == 'close':
        f = False
    else:
        print('Sorry the command is not recognized, try again\n')
        f = True
print('Goodbye!!!')
