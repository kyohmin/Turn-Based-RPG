# Import Modules

# Classes
class Character_stat:
    def __init__(self, NAME, TEAM):
        self.TEAM = ""
        self.NAME = ""
        self.RACE = ""
        self.HP = 0
        self.ATK = 0
        self.DEF = 0
        self.POISONED = False
        self.FROZEN = False
        self.RANK = 1
        self.ALIVE = True
        self.EXP = 0
    
    def set_name(self, NAME):
        self.NAME = NAME

    def set_team(self, TEAM):
        self.TEAM = TEAM

    def set_race(self, RACE):
        self.RACE = RACE

    def show(self):
        return self.RACE, self.NAME, self.HP, self.ATK, self.DEF, self.TEAM

class Ogre(Character_stat):
    def __init__(self):
        self.HP = 40
        self.ATK = 7
        self.DEF = 3
        self.ACCURACY = .5

class Knight(Character_stat):
    def __init__(self):
        self.HP = 45
        self.ATK = 5
        self.DEF = 5

class Sorcerer(Character_stat):
    def __init__(self):
        self.HP = 30
        self.ATK = 3
        self.DEF = 2

# Functions
def inputChecker(Choice, End, Message):
    while not Choice.isdigit() or int(Choice) <= 0 or int(Choice) > End:
        print("\n=============Wrong Value==============")
        print("\nYou entered wrong value, Please Try again\n")
        print(Message)
        Choice = input("Choose one : ")
    return int(Choice)


# ==============Main Menu=================
def start_menu():
    global start

    print("===============Main menu==============\n")
    print("Welcome to the game!\n")
    print("1. Start the Game\n2. Look at the save files\n")
    start = input("Choose one : ")
    start = inputChecker(start, 2, "1. Start the Game\n2. Quit\n")

def setting_game():
    global type_game
    global num_player
    global numPlayer
    global numEnemy
    numPlayer = []
    numEnemy = []

    print("\n============Fight Enemy=============\n")
    print("1. Player vs Player\n2. Player vs A.I.\n")
    type_game = input("Choose one : ")
    type_game = inputChecker(type_game, 2, "1. Player vs Player\n2. Player vs A.I.\n")

    print("\n==========# of Players==============\n")
    print("1. 1vs1\n2. 2vs2\n3. 3vs3\n4. 4vs4\n5. 5vs5\n")
    num_player = input("Choose one : ")
    num_player = inputChecker(num_player, 5, "1. 1vs1\n2. 2vs2\n3. 3vs3\n4. 4vs4\n5. 5vs5\n")
    
    # Making list of Players
    for units in range(num_player):
        player = f'player_{str(units+1)}'
        enemy = f'enemy_{str(units+1)}'
        numPlayer.append(player)
        numEnemy.append(enemy)

    # Object setting [Player Side]
    for num in range(num_player):
        temp_1 = num
        print("\n=========Choose race of your team============\n")
        print("1. Ogre\n\tOgres have strong power, but have low accuracy\n")
        print("2. Knight\n\tKnight have decent power and strong defence power\n")
        print("3. Sorcerer\n\tSorcerer have weak body, but they can cast powerful magics\n")
        num = input("Choose one : ")
        num = inputChecker(num, 3, "1. Ogre\n\tOgres have strong power, but have low accuracy\n\n2. Knight\n\tKnight have decent power and strong defence power\n\n3. Sorcerer\n\tSorcerer have weak body, but they can cast powerful magics\n")
        if num == 1:
            numPlayer[temp_1] = Ogre()
            numPlayer[temp_1].set_race("Ogre")
        elif num == 2:
            numPlayer[temp_1] = Knight()
            numPlayer[temp_1].set_race("Knight")
        else:
            numPlayer[temp_1] = Sorcerer()
            numPlayer[temp_1].set_race("Sorcerer")

    # Object setting [Enemy Side]
    for num in range(num_player):
        temp_1 = num
        print("\n=========Choose the race of the enemy============\n")
        print("1. Ogre\n\tOgres have strong power, but have low accuracy\n")
        print("2. Knight\n\tKnight have decent power and strong defence power\n")
        print("3. Sorcerer\n\tSorcerer have weak body, but they can cast powerful magics\n")
        num = input("Choose one : ")
        num = inputChecker(num, 3, "1. Ogre\n\tOgres have strong power, but have low accuracy\n\n2. Knight\n\tKnight have decent power and strong defence power\n\n3. Sorcerer\n\tSorcerer have weak body, but they can cast powerful magics\n")
        if num == 1:
            numEnemy[temp_1] = Ogre()
            numEnemy[temp_1].set_race("Ogre")
        elif num == 2:
            numEnemy[temp_1] = Knight()
            numEnemy[temp_1].set_race("Knight")
        else:
            numEnemy[temp_1] = Sorcerer()
            numEnemy[temp_1].set_race("Sorcerer")


def naming_units():
    for num in range(num_player):
        print("\n=============Name TEAM===================\n")
        name = input(f'Please enter the name of the player_{num+1} : ')
        name = name.strip()
        while name == '':
            print("\n=============Wrong Value===================\n")
            name = input(f'Please enter the name of the player_{num+1} : ')
            name = name.strip()
        player = numPlayer[num]
        player.set_name(name)
        # Set TEAM
        player.set_team("ALLY")

    for num in range(num_player):
        print("\n=============Name Enemy===================\n")
        name = input(f'Please enter the name of the Enemy_{num+1} : ')
        name = name.strip()
        while name == '':
            print("\n=============Wrong Value===================\n")
            name = input(f'Please enter the name of the Enemy_{num+1} : ')
            name = name.strip()
        player = numEnemy[num]
        player.set_name(name)
        # Set TEAM
        player.set_team("ENEMY")


# Start
start_menu()

if start == 1:
    setting_game()
    naming_units()

for a in range(num_player):
    print(numPlayer[a].show())

for a in range(num_player):
    print(numEnemy[a].show())