import os
import pandas as pd
excel_file = pd.read_excel('CStat.xlsx')
      
# Characters Stats==============================
class Unit:
    def __init__(self):
        self.RANK = 0
        self.EXP = 40
        self.FIGHTABLE = True
        self.ALIVE = True
        self.FROZEN = True
        self.POISONED = False

    def set_NT(self, NAME, TEAM):
        self.NAME = NAME
        self.TEAM = TEAM

    def show_stats(self):
        return self.NAME, self.RACE, self.HP, self.ATK, self.DEF, self.FROZEN, self.POISONED, self.EXP, self.RANK, self.ALIVE

    def exp_system(self):
        self.EXP += 19
    
    def attack_system(self):
        pass
    
    def special_power_system(self):
        pass

    def rank_up(self):
        if self.EXP >= 40:
            if self.ID < self.MAX_ID:
                self.EXP = 0
                self.RACE = str(excel_file['Race'][self.ID])
                self.HP = int(excel_file['HP'][self.ID])
                self.ATK = int(excel_file['ATK'][self.ID])
                self.DEF = int(excel_file['DEF'][self.ID])
                self.RANK += 1
                self.ID += 1
            else:
                self.ID = self.MAX_ID

class Ogre(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][0])
        self.MAX_ID = self.ID + 3

class Knight(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][3])
        self.MAX_ID = self.ID + 3

class Sorcerer(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][6])
        self.MAX_ID = self.ID + 3

# FUNCTIONS ===============================================
# Main Menu
def main_menu():
    global menu_input
    clean_screen()
    # WELCOME PAGE
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃            WELCOME TO THE GAME             ┃")
    print("┃                                            ┃")
    print("┃    <PLEASE CHOOSE WHAT YOU WANT TO DO>     ┃")
    print("┃                                            ┃")
    print("┃             1. START NEW GAME              ┃")
    print("┃             2. LOAD NEW GAME               ┃")
    print("┃             3. QUIT THE GAME               ┃")
    print("┃                                            ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    # Input Check
    menu_input = input("\nPlease Enter the Number (1~3) : ")
    while not menu_input.isdigit() or int(menu_input) <= 0 or int(menu_input) > 3:
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃         You Entered Wrong Value            ┃")
        print("┃                                            ┃")
        print("┃             1. START NEW GAME              ┃")
        print("┃             2. LOAD NEW GAME               ┃")
        print("┃             3. QUIT THE GAME               ┃")
        print("┃                                            ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        menu_input = input("\nPlease Enter the Number (1~3) : ")
    menu_input = int(menu_input)

# Setting Enemy
def setting_enemy():
    global game_type
    clean_screen()
    # Choosing between PvP and Player vs A.I.
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃  <CHOOSE THE ENEMY BETWEEN AI and PLAYER>  ┃")
    print("┃                                            ┃")
    print("┃             1. Player vs Player            ┃")
    print("┃             2. Player vs A.I.              ┃")
    print("┃                                            ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    # Input Check
    game_type = input("\nPlease Enter the Number (1~2) : ")
    while not game_type.isdigit() or int(game_type) <= 0 or int(game_type) > 3:
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃           You Entered Wrong Value          ┃")
        print("┃                                            ┃")
        print("┃             1. Player vs Player            ┃")
        print("┃             2. Player vs A.I.              ┃")
        print("┃                                            ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        game_type = input("\nPlease Enter the Number (1~2) : ")
    game_type = int(game_type)

# Number of Players
def setting_size():
    global num_players
    clean_screen()
    # Choosing between PvP and Player vs A.I.
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃     <CHOOSE HOW MANY PLAYERS YOU WANT>     ┃")
    print("┃                                            ┃")
    print("┃                 1. 1 vs 1                  ┃")
    print("┃                 2. 2 vs 2                  ┃")
    print("┃                 3. 3 vs 3                  ┃")
    print("┃                 4. 4 vs 4                  ┃")
    print("┃                 5. 5 vs 5                  ┃")
    print("┃                                            ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    # Input Check
    num_players = input("\nPlease Enter the Number (1~5) : ")
    while not num_players.isdigit() or int(num_players) <= 0 or int(num_players) > 5:
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃           You Entered Wrong Value          ┃")
        print("┃                                            ┃")
        print("┃                 1. 1 vs 1                  ┃")
        print("┃                 2. 2 vs 2                  ┃")
        print("┃                 3. 3 vs 3                  ┃")
        print("┃                 4. 4 vs 4                  ┃")
        print("┃                 5. 5 vs 5                  ┃")
        print("┃                                            ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        num_players = input("\nPlease Enter the Number (1~5) : ")
    num_players = int(num_players)

# Setting Race & Name
def setting_RN():
    for num in range(num_players):
        # For ALLY ===================================================================
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃               <CHOOSE THE RACE OF THE ALLY>                    ┃")
        print("┃                                                                ┃")
        print("┃       1. [OGRE]                                                ┃")
        print("┃          Have Strong Power, but have 50% to miss               ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┃       2. [KNIGHT]                                              ┃")
        print("┃          Have Decent Power and Strong Defence                  ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┃       3. [SORCERER]                                            ┃")
        print("┃          Have Weak Power and Defence, but can cast magic       ┃")
        print("┃               Magic Skills : {0}, {1}, and {2}          ┃" .format(excel_file['SP 1'][6], excel_file['SP 2'][6], excel_file['SP 3'][6]))
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                    ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        
        # Check Input
        race_input = input("\nPlease Enter the Number (1~3) : ")
        while not race_input.isdigit() or int(race_input) <= 0 or int(race_input) > 3:
            clean_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃                     You Entered Wrong Value                    ┃")
            print("┃                                                                ┃")
            print("┃       1. [OGRE]                                                ┃")
            print("┃          Have Strong Power, but have 50% to miss               ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
            print("┃               [One Hidden Skill in Rank 3]                     ┃")
            print("┃                                                                ┃")
            print("┃       2. [KNIGHT]                                              ┃")
            print("┃          Have Decent Power and Strong Defence                  ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
            print("┃               [One Hidden Skill in Rank 3]                     ┃")
            print("┃                                                                ┃")
            print("┃       3. [SORCERER]                                            ┃")
            print("┃          Have Weak Power and Defence, but can cast magic       ┃")
            print("┃               Magic Skills : {0}, {1}, and {2}          ┃" .format(excel_file['SP 1'][6], excel_file['SP 2'][6], excel_file['SP 3'][6]))
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                    ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
            print("┃               [One Hidden Skill in Rank 3]                     ┃")
            print("┃                                                                ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            race_input = input("\nPlease Enter the Number (1~3) : ")
        race_input = int(race_input)

        # Assign Object in List
        if race_input == 1:
            ally_object[num] = Ogre()
            race_input = "'Ogre'?    "
        elif race_input == 2:
            ally_object[num] = Knight()
            race_input = "'Knight'?  "
        elif race_input == 3:
            ally_object[num] = Sorcerer()
            race_input = "'Sorcerer'?"

        # Naming the Object
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃          <GIVE A NAME TO YOUR ALLY>        ┃")
        print("┃                                            ┃")
        print("┃        * Do not type blank or space        ┃")
        print("┃                                            ┃")
        print("┃     What is the name of your {0}   ┃" .format(race_input))
        print("┃                                            ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

        # Check Input
        name = input("\nPlease Write the NAME : ")
        name = name.strip()
        while name == '':
            clean_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃           You Entered Wrong Value          ┃")
            print("┃                                            ┃")
            print("┃        * Do not type blank or space        ┃")
            print("┃                                            ┃")
            print("┃     What is the name of your {0}   ┃" .format(race_input))
            print("┃                                            ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            name = input("\nPlease Write the NAME : ")
            name = name.strip()

        ally_object[num].set_NT(name, "ALLY")

    for num in range(num_players):
        # For ENEMY ======================================================================
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃               <CHOOSE THE RACE OF THE ENEMY>                   ┃")
        print("┃                                                                ┃")
        print("┃       1. [OGRE]                                                ┃")
        print("┃          Have Strong Power, but have 50% to miss               ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┃       2. [KNIGHT]                                              ┃")
        print("┃          Have Decent Power and Strong Defence                  ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┃       3. [SORCERER]                                            ┃")
        print("┃          Have Weak Power and Defence, but can cast magic       ┃")
        print("┃               Magic Skills : {0}, {1}, and {2}          ┃" .format(excel_file['SP 1'][6], excel_file['SP 2'][6], excel_file['SP 3'][6]))
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                    ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        
        # Check Input
        race_input = input("\nPlease Enter the Number (1~3) : ")
        while not race_input.isdigit() or int(race_input) <= 0 or int(race_input) > 3:
            clean_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃                     You Entered Wrong Value                    ┃")
            print("┃                                                                ┃")
            print("┃       1. [OGRE]                                                ┃")
            print("┃          Have Strong Power, but have 50% to miss               ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
            print("┃               [One Hidden Skill in Rank 3]                     ┃")
            print("┃                                                                ┃")
            print("┃       2. [KNIGHT]                                              ┃")
            print("┃          Have Decent Power and Strong Defence                  ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                   ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
            print("┃               [One Hidden Skill in Rank 3]                     ┃")
            print("┃                                                                ┃")
            print("┃       3. [SORCERER]                                            ┃")
            print("┃          Have Weak Power and Defence, but can cast magic       ┃")
            print("┃               Magic Skills : {0}, {1}, and {2}          ┃" .format(excel_file['SP 1'][6], excel_file['SP 2'][6], excel_file['SP 3'][6]))
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                    ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
            print("┃               [One Hidden Skill in Rank 3]                     ┃")
            print("┃                                                                ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            race_input = input("\nPlease Enter the Number (1~3) : ")
        race_input = int(race_input)

        # Assign Object in List
        if race_input == 1:
            enemy_object[num] = Ogre()
            race_input = "'Ogre'?    "
        elif race_input == 2:
            enemy_object[num] = Knight()
            race_input = "'Knight'?  "
        elif race_input == 3:
            enemy_object[num] = Sorcerer()
            race_input = "'Sorcerer'?"

        # Naming the Object
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳")
        print("┃         <GIVE A NAME TO YOUR ENEMY>        ┃")
        print("┃                                            ┃")
        print("┃        * Do not type blank or space        ┃")
        print("┃                                            ┃")
        print("┃     What is the name of your {0}   ┃" .format(race_input))
        print("┃                                            ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

        # Check Input
        name = input("\nPlease Write the NAME : ")
        name = name.strip()
        while name == '':
            clean_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃           You Entered Wrong Value          ┃")
            print("┃                                            ┃")
            print("┃        * Do not type blank or space        ┃")
            print("┃                                            ┃")
            print("┃     What is the name of your {0}   ┃" .format(race_input))
            print("┃                                            ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            name = input("\nPlease Write the NAME : ")
            name = name.strip()

        enemy_object[num].set_NT(name, "ENEMY")

# MAIN UI
def main_UI():
    GAME = True
    turn = 1
    while GAME:
        clean_screen()

        # INIT and Check for Rank Up
        for num in range(num_players):
            ally_object[num].rank_up()
            enemy_object[num].rank_up()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃  [STATS]                                                       ┃  [AVAILABLE UNITS]          ┃  [AVAILABLE MOVES]         ┃")
        print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
        print("┃  -ALLY'S TEAM-                                                 ┃   -ALLY'S TEAM-             ┃   -ALLY'S TEAM-            ┃")
        print("┃                                                                ┃                             ┃                            ┃")
        for num in range(num_players):
            unit_stat = ally_object[num].show_stats()
            if unit_stat[1] == "Ogre" or unit_stat[1] == "Knight":
                if unit_stat[5] == True and unit_stat[6] == True:
                    # First row
                    print("┃   {name} (Frozen & Poisoned) : " .format(name = unit_stat[0]) + " " * (38 - len(unit_stat[0])) + "┃                             ┃                            ┃")
                    # Second row
                    print("┃        HP : {0}        ATK : {1}        DEF : {2}" .format(unit_stat[2], unit_stat[3], unit_stat[4]) + " "*(15 - len(str(unit_stat[2])) + len(str(unit_stat[3])) + len(str(unit_stat[4]))) + "┃                             ┃                            ┃")
                    # Third row
                    print("┃                 EXP : {0}       RANK : {1}" . format(unit_stat[7], unit_stat[8]) + " "*(26 - len(str(unit_stat[7]))) + "┃                             ┃                            ┃")
                    print("┃                                                                ┃                             ┃                            ┃")
                elif unit_stat[5] == True:
                    # First row
                    print("┃   {name} (Frozen) : " .format(name = unit_stat[0]) + " " * (49 - len(unit_stat[0])) + "┃                             ┃                            ┃")
                    # Second row
                    print("┃        HP : {0}        ATK : {1}        DEF : {2}" .format(unit_stat[2], unit_stat[3], unit_stat[4]) + " "*(15 - len(str(unit_stat[2])) + len(str(unit_stat[3])) + len(str(unit_stat[4]))) + "┃                             ┃                            ┃")
                    # Third row
                    print("┃        EXP : {0}       RANK : {1}       RACE : {2}" . format(unit_stat[7], unit_stat[8], unit_stat[1]) + " "*(14 - len(str(unit_stat[7])) + len(str(unit_stat[1]))) + "┃                             ┃                            ┃")
                    print("┃                                                                ┃                             ┃                            ┃")
                    
                elif unit_stat[6] == True:
                    pass
                else:
                    if unit_stat[9] == True:
                        pass
                    else:
                        pass
            elif unit_stat[1] == "Sorcerer":
                print("")

        turn += 1
        GAME = False

# List for Objects
def list_objects():
    global ally_object
    global enemy_object
    ally_object = []
    enemy_object = []

    for _ in range(1, num_players + 1):
        ally_object.append('ally')
        enemy_object.append('enemy')

# Cleaning Screen
def clean_screen():
   if os.name == 'posix':
        os.system('clear')
   else:
        os.system('cls')

# GAME LOGIC ===========================================================
def main():
    main_menu()
    if menu_input == 1:
        setting_enemy()
        if game_type == 1:
            setting_size()
            list_objects()
            setting_RN()
            main_UI()

# Start the game
main()

# ┳ ┣ ┫ ┻ ╋