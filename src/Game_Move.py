from src.Hero import Hero
from src.Monster import Monster
import json
import time

class Game_Move:

    """ Dictates how the game works, like creating a hero or whos turn is it to attack etc. """

    def __init__(self):

        """ By creating a game, you automatically a hero aswell. """

        self.create_hero()

    def create_hero(self):

        """ You create a hero by giving him/her a name, gender and set an age. """

        name = input('How should your Hero be called?: ')
        time.sleep(0.25)
        sex = input('What should your Gender be?: ')
        time.sleep(0.25)
        age = input('What will be your age?: ')
        time.sleep(0.25)
       

        self.hero = Hero(name, sex, age)

        self.hero.select_class()

        time.sleep(0.25)

        self.hero.show_hero_stats()


    def start_game(self):

        """ This method is the startingpoint of every new begining battle, first bei checking ob you are ready for it and than end or start the gam eon the outcome of the question """

        answer_yes_or_no = input('Are you ready to enter the fight? (YES / NO) : ')

        if answer_yes_or_no.lower() == 'yes':

            self.monster = Monster()

            self.monster.level = self.hero.level

            print('Press ENTER for the battle to begin!')
            input()

            self.hero_fight()

        elif answer_yes_or_no.lower() == 'no':

            print('GAME OVER! - YOU FAILED BEFOR IT EVEN STARTED!')

        else:
            print('Invalid answer! Try again')

            self.start_game()
        
    def hero_fight(self):

        """ Heros stats updater and actions he can choose in a fight (attack, heal etc.)"""

        if self.monster.healpoints <= 0:

            if self.hero.level < 3:

                self.hero.healpoints = self.hero.level * 150
                self.hero.attackpoints = self.hero.level * 40
                self.hero.defensivepoints = self.hero.level * 15
                
                print("""
                YOU HAVE WON!
                """)

                time.sleep(1)

                self.hero.level_up()

                self.start_game()

            else: 
                time.sleep(0.25)
                print(f'You saved XOZ! - Thank you {self.hero.name}')

        elif self.hero.healpoints <= 0:

            print('YOU HAVED FAILD! - YOU ARE DAED!')


        else:
            self.hero.show_hero_stats()

            self.monster.show_monster_stats()

            print('PRESS ENTER!')
            input()


            answer = input("""

What do you wonna do? :

1. Attack
2. Heal
3. Give up and Die!

    """)

            time.sleep(0.25)

            if answer == '1':

                hero_damage = self.hero.attackpoints - self.monster.defensivepoints

                self.monster.healpoints -= hero_damage

                print(f'{self.hero.name} dealed {hero_damage} damage, {self.monster.name} health is now on {self.monster.healpoints}')

                self.monster_fight()

            elif answer == '2':

                self.hero.healpoints += 20

                print(f'{self.hero.name} has healt for 20 healthpoints and is now on {self.hero.healpoints}!')

                self.monster_fight()

            elif answer == '3':

                print('YOU HAVED FAILD! - YOU ARE DAED!')

            else:
                print('Invalid answer! Try again')

                self.hero_fight()



    def monster_fight(self):

        """ Same as the hero_fight() Method this the exception that the Mosnters can only attack. """

        time.sleep(0.5)

        monster_damage = self.monster.attackpoints - self.hero.defensivepoints

        self.hero.healpoints -= monster_damage

        print(f'{self.monster.name} dealed {monster_damage} damage, {self.hero.name} health is now on {self.hero.healpoints}')

        self.hero_fight()

        
