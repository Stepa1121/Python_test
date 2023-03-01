from random import randint, seed, choice


class Person:  # A class with common characteristics of "Soldier" and "Hero"
    __a = 0
    seed(__a)  # Parameter for setting the time in the randomization method

    def __init__(self):  # Function for assigning an id to the created instance
        self.id_player = randint(1, 1000)  # Random id selection
        Person.__a += 1
        seed()


class Hero(Person):  # A class for creating heroes
    def __init__(self, color):  # A function for the initialization a hero
        super().__init__()  # Assigning an id
        self.color = color  # Assigning a team color
        self.team = []  # A list for team members
        self.level = 0  # Level parameter

    def level_up(self):  # A function for raising the level
        self.level += 1

    def hero_team(self, soldier):  # A function for adding a member to the team
        self.team.append(soldier)

    def del_team(self):  # A function for delete a team
        self.team = []


class Soldier(Person):  # A class for creating soldiers
    def __init__(self):  # A function for initialization a soldiers
        super().__init__()  # Assigning an id

    def go_to_hero(self, hero):
        hero.hero_team(self.id_player)


h1 = Hero('Blue')
h2 = Hero('Red')
for _ in range(11):
    for _ in range(randint(10, 30)):
        a = Soldier()
        a.go_to_hero(choice([h1, h2]))
    if len(h1.team) < len(h2.team):
        h1.level_up()
    elif len(h2.team) < len(h1.team):
        h2.level_up()
    for x in (h1, h2):
        x.del_team()
    print(h1.level, h2.level)
print((f'The {(h1.color, h2.color)[h1.level > h2.level]} team winner'))
