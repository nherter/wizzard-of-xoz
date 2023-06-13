class Hero:

    """In this class you can create ur hero and do aktions with your hero. """

    def __init__(self, name, sex, age, level=1, healpoints=150, attackpoints=25, defensivepoints=5):

        """ Set infromation about the hero """

        self.name = name # diffine heros name
        self.sex = sex # diffine heros gender
        self.age = age # diffine heros age 
        self.level = level # diffine heros level (starting value = 1)
        self.hero_class = None # is set on none as an placeholder, to diffine it later in select_class()
        self.healpoints = healpoints
        self.attackpoints = attackpoints
        self.defensivepoints = defensivepoints

    def select_class(self):

        """ You can select which class you wont to choose, there are 3 classes: Mage, Worrier and Templer. """

        print("""
In the world of XOZ you can choose between 3 classes,

1. Mage
2. Worrier
3. Templer

Press the nummber for the selection!""")

        selection = input()

        if selection == '1':

            self.hero_class = 'Mage'

        elif selection == '2':

            self.hero_class = 'Worrier'

        elif selection == '3':

            self.hero_class = 'Templer'

        else:
            print('This claas dont exist jet! Try again.')

            self.select_class()

    def show_hero_stats(self):

        """ This Method is for showing your information (stats, name, age, class etc.) in a compact form. """

        print(f"""
        Hero  : {self.name} ({self.sex})
        Age   : {self.age} years
        Level : {self.level}, {self.hero_class}
        -----------------------
        Heal ponits      : {self.healpoints}
        Attack points    : {self.attackpoints}
        Defensive points : {self.defensivepoints}
        """)

    def level_up(self):

        """ Update the stats for the new level of your hero and shows it in a new view. """

        past_level = self.level
        
        self.level += 1
        self.healpoints += 150
        self.attackpoints += 40
        self.defensivepoints += 5

        if self.level <= 3:

            print(f"""
                LEVEL UP! 

            Hero  : {self.name} ({self.sex})
            Age   : {self.age} years
            Level : {past_level} -> {self.level}, {self.hero_class}
            -----------------------------
            Heal ponits      : {150 * past_level} -> {self.healpoints}
            Attack points    : {40 * past_level} -> {self.attackpoints}
            Defensive points : {15 * past_level} -> {self.defensivepoints} 
            """)

        else: 
            print("Your are already on the highest level possibal")