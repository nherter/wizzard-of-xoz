from src.Hero import Hero
import json
import random


class Monster:

    """ All about the monsters and there acions. """

    def __init__(self, level=1):

        self.level = level

        self.random_monster()

    def random_monster(self):

        """ Select a random monster from the monster.jason file and convert it into a python file. """

        monster_selection = random.randint(0,4)

        with open('./src/monster.json','r') as json_monster:
            
                py_monster = json.load(json_monster)

                self.monster = py_monster[monster_selection]

                print(f"Your enemy is {self.monster['Name']} it is a {self.monster['Race']} in the age of {self.monster['Age']}!")

                self.monster_takeover()


    def show_monster_stats(self):

        """ Shows information about the monster. """

        print(f"""
        Name : {self.name}
        Age  : {self.age}
        Race : {self.race}
        ---------------------
        Healpoints      : {self.healpoints}
        Attackpoints    : {self.attackpoints}
        Defenisvepoints : {self.defensivepoints}
        """)

    def monster_takeover(self):

        """ Makes it in a form to get it into other files like Game_Move.py. """

        self.name = self.monster['Name']
        self.race = self.monster['Race']
        self.age = self.monster['Age']
        self.healpoints = self.level * int(self.monster['Healpoints'])
        self.attackpoints = self.level * int(self.monster['Attackpoints'])
        self.defensivepoints = self.level * int(self.monster['Defensivepoints'])
