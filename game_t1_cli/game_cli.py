import os
import pandas as pd
import time
from random import randint, random, choice


# For absolute path in any devices ===============================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

try:
    excel_file = pd.read_excel(resource_path('./game_t1_cli/CStat.xlsx'), 'Character_Stats')
except:
    excel_file = pd.read_excel('./CStat.xlsx', 'Character_Stats')

# Characters Stats==============================
class Unit:
    ally_counter = 0
    enemy_counter = 0

    def __init__(self):
        self.RANK = 0
        self.EXP = 40
        self.FIGHTABLE = True
        self.ALIVE = True
        self.FROZEN = False
        self.POISONED = False

    def set_NT(self, NAME, TEAM):
        self.NAME = NAME
        self.TEAM = TEAM

    def show_stats(self):
        return self.NAME, self.RACE, self.HP, self.ATK, self.DEF, self.FROZEN, self.POISONED, self.EXP, self.RANK, self.ALIVE
    
    def attack(self, TARGET):
        if self.ACCURACY >= random():
            if self.ATK < TARGET.DEF:
                total_damage = randint(0,6)
            else:    
                total_damage = self.ATK - TARGET.DEF + randint(0,6)
            self.HP -= TARGET.DEF
            TARGET.HP -= total_damage

            # EXP system
            self.EXP += total_damage
            TARGET.EXP += TARGET.DEF
            
            if total_damage >= 10:
                self.EXP += int(self.EXP * 1.2)

        if TARGET.HP == 0:
            TARGET.ALIVE = False
            self.EXP += int(self.EXP * 1.5)

        self.rank_up()
        TARGET.rank_up()

        if TARGET.HP <= 0:
            if TARGET.TEAM == "ALLY":
                Unit.ally_counter -= 1
            else:
                Unit.enemy_counter -= 1
    
    def heal(self,TARGET):                            
        if TARGET.TEAM == self.TEAM:
            if self.RANK == 1:
                TARGET.HP += 5
                self.EXP += 5
            elif self.RANK == 2:
                TARGET.HP += 8
                self.EXP += 5
            else:
                TARGET.HP += 10
                self.EXP += 5
        
        self.rank_up()
        TARGET.rank_up()
    
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
        
        if self.HP <= 0:
            self.ALIVE = False

class Ogre(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][0])
        self.MAX_ID = self.ID + 3
        self.ACCURACY = 0.5

class Knight(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][3])
        self.MAX_ID = self.ID + 3
        self.ACCURACY = 1

class Sorcerer(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][6])
        self.MAX_ID = self.ID + 3
        self.ACCURACY = 1

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
        clean_screen()
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
    clean_screen()
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
        clean_screen()
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
    clean_screen()
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
        clean_screen()
    num_players = int(num_players)
    for _ in range(num_players):
        Unit.ally_counter += 1
        Unit.enemy_counter += 1

# Setting Race & Name
def setting_RN():
    names_list = []
    for num in range(num_players):
        # For ALLY ===================================================================
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃               <CHOOSE THE RACE OF THE ALLY>                    ┃")
        print("┃                                                                ┃")
        print("┃       1. [OGRE]                                                ┃")
        print("┃          Have Strong Power, but have 50% to miss               ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
        print("┃                                                                ┃")
        print("┃       2. [KNIGHT]                                              ┃")
        print("┃          Have Decent Power and Strong Defence                  ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
        print("┃                                                                ┃")
        print("┃       3. [SORCERER]                                            ┃")
        print("┃          Have Weak Power and Defence, but can cast magic       ┃")
        print("┃               Magic Skills : Heal                              ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
        print("┃                                                                ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        # Check Input
        race_input = input("\nPlease Enter the Number (1~3) : ")
        clean_screen()

        while not race_input.isdigit() or int(race_input) <= 0 or int(race_input) > 3:
            clean_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃                     You Entered Wrong Value                    ┃")
            print("┃                                                                ┃")
            print("┃       1. [OGRE]                                                ┃")
            print("┃          Have Strong Power, but have 50% to miss               ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
            print("┃                                                                ┃")
            print("┃       2. [KNIGHT]                                              ┃")
            print("┃          Have Decent Power and Strong Defence                  ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
            print("┃                                                                ┃")
            print("┃       3. [SORCERER]                                            ┃")
            print("┃          Have Weak Power and Defence, but can cast magic       ┃")
            print("┃               Magic Skills : Heal                              ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
            print("┃                                                                ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            race_input = input("\nPlease Enter the Number (1~3) : ")
            clean_screen()
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
        clean_screen()
        name = name.strip()
        while name == '' or len(name) > 20 or name in names_list:
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
            clean_screen()
        names_list.append(name)

        ally_object[num].set_NT(name, "ALLY")

    for num in range(num_players):
        # For ENEMY ======================================================================
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃               <CHOOSE THE RACE OF THE ENEMY>                   ┃")
        print("┃                                                                ┃")
        print("┃       1. [OGRE]                                                ┃")
        print("┃          Have Strong Power, but have 50% to miss               ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
        print("┃                                                                ┃")
        print("┃       2. [KNIGHT]                                              ┃")
        print("┃          Have Decent Power and Strong Defence                  ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
        print("┃                                                                ┃")
        print("┃       3. [SORCERER]                                            ┃")
        print("┃          Have Weak Power and Defence, but can cast magic       ┃")
        print("┃               Magic Skills : Heal                              ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
        print("┃                                                                ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        
        # Check Input
        race_input = input("\nPlease Enter the Number (1~3) : ")
        clean_screen()
        while not race_input.isdigit() or int(race_input) <= 0 or int(race_input) > 3:
            clean_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃                     You Entered Wrong Value                    ┃")
            print("┃                                                                ┃")
            print("┃       1. [OGRE]                                                ┃")
            print("┃          Have Strong Power, but have 50% to miss               ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
            print("┃                                                                ┃")
            print("┃       2. [KNIGHT]                                              ┃")
            print("┃          Have Decent Power and Strong Defence                  ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
            print("┃                                                                ┃")
            print("┃       3. [SORCERER]                                            ┃")
            print("┃          Have Weak Power and Defence, but can cast magic       ┃")
            print("┃               Magic Skills : Heal                              ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
            print("┃                                                                ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            race_input = input("\nPlease Enter the Number (1~3) : ")
            clean_screen()
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
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃         <GIVE A NAME TO YOUR ENEMY>        ┃")
        print("┃                                            ┃")
        print("┃        * Do not type blank or space        ┃")
        print("┃                                            ┃")
        print("┃     What is the name of your {0}   ┃" .format(race_input))
        print("┃                                            ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

        # Check Input
        name = input("\nPlease Write the NAME : ")
        clean_screen()
        name = name.strip()
        while name == '' or len(name) > 20 or name in names_list:
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
            clean_screen()
        names_list.append(name)

        enemy_object[num].set_NT(name, "ENEMY")
        clean_screen()

def setting_RN_AI():
    sample_names = ['James', 'Julio', 'Nick', 'John', 'Franklin', 'Bryan']
    names_list = []
    for num in range(num_players):
        # For ALLY ===================================================================
        clean_screen()
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("┃               <CHOOSE THE RACE OF THE ALLY>                    ┃")
        print("┃                                                                ┃")
        print("┃       1. [OGRE]                                                ┃")
        print("┃          Have Strong Power, but have 50% to miss               ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
        print("┃                                                                ┃")
        print("┃       2. [KNIGHT]                                              ┃")
        print("┃          Have Decent Power and Strong Defence                  ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
        print("┃                                                                ┃")
        print("┃       3. [SORCERER]                                            ┃")
        print("┃          Have Weak Power and Defence, but can cast magic       ┃")
        print("┃               Magic Skills : Heal                              ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
        print("┃                                                                ┃")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        # Check Input
        race_input = input("\nPlease Enter the Number (1~3) : ")
        clean_screen()

        while not race_input.isdigit() or int(race_input) <= 0 or int(race_input) > 3:
            clean_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("┃                     You Entered Wrong Value                    ┃")
            print("┃                                                                ┃")
            print("┃       1. [OGRE]                                                ┃")
            print("┃          Have Strong Power, but have 50% to miss               ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
            print("┃                                                                ┃")
            print("┃       2. [KNIGHT]                                              ┃")
            print("┃          Have Decent Power and Strong Defence                  ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
            print("┃                                                                ┃")
            print("┃       3. [SORCERER]                                            ┃")
            print("┃          Have Weak Power and Defence, but can cast magic       ┃")
            print("┃               Magic Skills : Heal                              ┃")
            print("┃               HP = {0} / ATK = {1} / DEF = {2}                      ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
            print("┃                                                                ┃")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            race_input = input("\nPlease Enter the Number (1~3) : ")
            clean_screen()
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
        clean_screen()
        name = name.strip()
        while name == '' or len(name) > 20 or name in names_list:
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
            clean_screen()
        names_list.append(name)

        ally_object[num].set_NT(name, "ALLY")

        if Unit.ally_counter == 1:
            enemy_object[0] = Knight()
            enemy_object[0].set_NT(choice(sample_names) + '_1', "ENEMY")
        elif Unit.ally_counter == 2:
            if randint(0,2) == 1:
                enemy_object[0] = Knight()
                enemy_object[0].set_NT(choice(sample_names) + '_1', "ENEMY")
                enemy_object[1] = Knight()
                enemy_object[1].set_NT(choice(sample_names) + '_2', "ENEMY")
            elif randint(0,2) == 2:
                enemy_object[0] = Sorcerer()
                enemy_object[0].set_NT(choice(sample_names) + '_1', "ENEMY")
                enemy_object[1] = Knight()
                enemy_object[1].set_NT(choice(sample_names) + '_2', "ENEMY")
            else:
                enemy_object[0] = Ogre()
                enemy_object[0].set_NT(choice(sample_names) + '_1', "ENEMY")
                enemy_object[1] = Knight()
                enemy_object[1].set_NT(choice(sample_names) + '_2', "ENEMY")
        elif Unit.ally_counter == 3:
            pass
        elif Unit.ally_counter == 4:
            pass
        elif Unit.ally_counter == 5:
            pass

def seg_UI(num):
    if unit_stat[1] == "Ogre" or unit_stat[1] == "Knight":
        print("┃        HP : {0}        ATK : {1}        DEF : {2}" .format(unit_stat[2], unit_stat[3], unit_stat[4]) + " "*(23 - (len(str(unit_stat[2])) + len(str(unit_stat[3])) + len(str(unit_stat[4])))) + "┃                             ┃                            ┃")
        print("┃        EXP : {0}       RANK : {1}       RACE : {2}" . format(unit_stat[7], unit_stat[8], unit_stat[1]) + " "*(21 - (len(str(unit_stat[7])) + len(str(unit_stat[1])))) + "┃                             ┃                            ┃")
        print("┃                                                                ┃                             ┃                            ┃")
    elif unit_stat[1] == "Sorcerer":
        if unit_stat[5] == True:
            print("┃        HP : {0}        ATK : {1}        DEF : {2}" .format(unit_stat[2], unit_stat[3], unit_stat[4]) + " "*(23 - (len(str(unit_stat[2])) + len(str(unit_stat[3])) + len(str(unit_stat[4])))) + "┃                             ┃                            ┃")
            print("┃        EXP : {0}       RANK : {1}       RACE : {2}" . format(unit_stat[7], unit_stat[8], unit_stat[1]) + " "*(21 - (len(str(unit_stat[7])) + len(str(unit_stat[1])))) + "┃                             ┃                            ┃")
            print("┃                                                                ┃                             ┃                            ┃")
        else:
            print("┃        HP : {0}        ATK : {1}        DEF : {2}" .format(unit_stat[2], unit_stat[3], unit_stat[4]) + " "*(23 - (len(str(unit_stat[2])) + len(str(unit_stat[3])) + len(str(unit_stat[4])))) + "┃                             ┃   2. HEAL                  ┃")
            print("┃        EXP : {0}       RANK : {1}       RACE : {2}" . format(unit_stat[7], unit_stat[8], unit_stat[1]) + " "*(21 - (len(str(unit_stat[7])) + len(str(unit_stat[1])))) + "┃                             ┃                            ┃")
            print("┃                                                                ┃                             ┃                            ┃")
            print("┃                                                                ┃                             ┃                            ┃")


def big_seg_UI(num):
    global avaiablility
    availability = False
    if unit_stat[9] == True:
        # ALIVE
        print("┃   {name} : " .format(name = unit_stat[0]) + " " * (58 - len(unit_stat[0])) + "┃   {num}. {name}" .format(num = num + 1, name = unit_stat[0]) + " " * (24 - (len(str(num)) + len(str(unit_stat[0])))) + "┃   1. ATTACK                ┃")
        seg_UI(num)
        avaiablility = True
    else:
        # DEAD
        print("┃   {name} : DEAD" .format(name = unit_stat[0]) + " " * (54 - len(unit_stat[0])) + "┃                             ┃                            ┃")
        print("┃                                                                ┃                             ┃                            ┃")

# SETTING COUNTDOWN TIMER
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:01d}'.format(secs) 
        print(timer,'...',sep='',end="\r") 
        time.sleep(1) 
        t -= 1      
t = 3  

# MAIN UI
def main_UI():
    global unit_stat
    global available_ally
    global available_enemy
    available_ally = []
    available_enemy = []

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
        big_seg_UI(num)
        if avaiablility == True:
            available_ally.append(num+1)
    
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃  -ENEMY'S TEAM-                                                ┃   -ENEMY'S TEAM-            ┃   -ENEMY'S TEAM-           ┃")
    print("┃                                                                ┃                             ┃                            ┃")

    for num in range(num_players):
        unit_stat = enemy_object[num].show_stats()
        big_seg_UI(num)
        if avaiablility == True:
            available_enemy.append(num+1)

    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    input("\n Press Enter ")

def ally_UI():
    global unit_stat
    clean_screen()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃  [ALLY STAT - TURN {turn}]" .format(turn = turn) + " "*(43 - len(str(turn))) + "┃  [AVAILABLE UNITS]          ┃  [AVAILABLE MOVES]         ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃  -ALLY'S TEAM-                                                 ┃   -ALLY'S TEAM-             ┃   -ALLY'S TEAM-            ┃")
    print("┃                                                                ┃                             ┃                            ┃")
    for num in range(num_players):
        unit_stat = ally_object[num].show_stats()
        big_seg_UI(num)
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def enemy_UI():                                                    
    global unit_stat
    clean_screen()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃  [ENEMY STAT - TURN {turn}]" .format(turn = turn) + " "*(42 - len(str(turn))) + "┃  [AVAILABLE UNITS]          ┃  [AVAILABLE MOVES]         ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃  -ENEMY'S TEAM-                                                ┃   -ENEMY'S TEAM-            ┃   -ENEMY'S TEAM-           ┃")
    print("┃                                                                ┃                             ┃                            ┃")
    for num in range(num_players):
        unit_stat = enemy_object[num].show_stats()
        big_seg_UI(num)
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")


def sorcererheal_UI():
    global unit_stat
    clean_screen()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃  [ALLY STAT - TURN {turn}]" .format(turn = turn) + " "*(43 - len(str(turn))) + "┃  [AVAILABLE UNITS]          ┃  [AVAILABLE MOVES]         ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃  -ALLY'S TEAM-                                                 ┃   -ALLY'S TEAM-             ┃   -ALLY'S TEAM-            ┃")
    print("┃                                                                ┃                             ┃                            ┃")
    for num in range(num_players):
        unit_stat = ally_object[num].show_stats()
        big_seg_UI(num)
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def sorcererattack_UI():
    global unit_stat
    clean_screen()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃  [ENEMY STAT - TURN {turn}]" .format(turn = turn) + " "*(42 - len(str(turn))) + "┃  [AVAILABLE UNITS]          ┃  [AVAILABLE MOVES]         ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃  -ENEMY'S TEAM-                                                ┃   -ENEMY'S TEAM-            ┃   -ENEMY'S TEAM-           ┃")
    print("┃                                                                ┃                             ┃                            ┃")
    for num in range(num_players):
        unit_stat = enemy_object[num].show_stats()
        big_seg_UI(num)
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

def sorcererenemy_UI():
    global unit_stat
    clean_screen()
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃  [ENEMY STAT - TURN {turn}]" .format(turn = turn) + " "*(42 - len(str(turn))) + "┃  [AVAILABLE UNITS]          ┃  [AVAILABLE MOVES]         ┃")
    print("┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫")
    print("┃  -ENEMY'S TEAM-                                                ┃   -ENEMY'S TEAM-            ┃   -ENEMY'S TEAM-           ┃")
    print("┃                                                                ┃                             ┃                            ┃")
    for num in range(num_players):
        unit_stat = enemy_object[num].show_stats()
        big_seg_UI(num)
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    
# List for Objects
def list_objects():
    global ally_object
    global enemy_object
    ally_object = []
    enemy_object = []

    for _ in range(1, num_players + 1):
        ally_object.append('ally')
        enemy_object.append('enemy')

def game_logic():
    global turn
    global GAME

    turn = 0
    GAME = True
    while GAME:
        main_UI()
        ally_UI()
        
        # Ally's turn - Ally select who attacks who
        if len(available_ally) > 0 and len(available_enemy) > 0:
            unit_select = input("\n Choose the available unit in your team (#) : ")
            while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) > len(available_ally) or ally_object[int(unit_select) - 1].show_stats()[9] == False:
                ally_UI()
                print("\n YOU ENTERED WRONG VALUE")
                unit_select = input("\n Choose the available unit in your team (#) : ")

            if ally_object[int(unit_select) - 1].show_stats()[1] == "Sorcerer":
                sorcererheal_UI()
                move_select = input("\n Choose your move (1~2) : ")
                while not move_select.isdigit() or int(move_select) < 0 or int(move_select) > 2:
                    sorcererheal_UI()
                    print("\n YOU ENTERED WRONG VALUE")
                    move_select = input("\n Choose your move (1~2) : ")

                if int(move_select) == 1:
                    sorcererattack_UI()
                    opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or enemy_object[int(opponent_select) - 1].show_stats()[9] == False:
                        sorcererattack_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    ally_object[int(unit_select) - 1].attack(enemy_object[int(opponent_select)-1])
                    print(ally_object[int(unit_select) - 1].show_stats()[0],"attacked",enemy_object[int(unit_select) - 1].show_stats()[0])
                    countdown(int(t))
                    

                elif int(move_select) == 2:
                    sorcererheal_UI()
                    opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                    while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or enemy_object[int(opponent_select) - 1].show_stats()[9] == False:
                        sorcererheal_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                    ally_object[int(unit_select) - 1].heal(ally_object[int(opponent_select)-1])
                    print(ally_object[int(unit_select) - 1].show_stats()[0],"healed",ally_object[int(unit_select) - 1].show_stats()[0])
                    countdown(int(t))

            else:
                enemy_UI()
                opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or enemy_object[int(opponent_select) - 1].show_stats()[9] == False:
                    enemy_UI()
                    print("\n YOU ENTERED WRONG VALUE")
                    opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                ally_object[int(unit_select) - 1].attack(enemy_object[int(opponent_select)-1])
                print(ally_object[int(unit_select) - 1].show_stats()[0],"attacked",enemy_object[int(unit_select) - 1].show_stats()[0])
                countdown(int(t))

            if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                main_UI()
                break
        
            main_UI()
            enemy_UI()

            # Enemy's turn - Enemy select who attacks who
            if len(available_ally) > 0 and len(available_enemy) > 0:
                unit_select = input("\n Choose the available unit in your team (#) : ")
                while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) > len(available_ally) or enemy_object[int(unit_select) - 1].show_stats()[9] == False:
                    enemy_UI()
                    print("\n YOU ENTERED WRONG VALUE")
                    unit_select = input("\n Choose the avaiable unit in your team (#) : ")

                if enemy_object[int(unit_select) - 1].show_stats()[1] == "Sorcerer":
                    sorcererenemy_UI()
                    move_select = input("\n Choose your move (1~2) : ")
                    while not move_select.isdigit() or int(move_select) < 0 or int(move_select) > 2:
                        sorcererenemy_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        move_select = input("\n Choose your move (1~2) : ")

                    if int(move_select) == 1:
                        ally_UI()
                        opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or ally_object[int(opponent_select) - 1].show_stats()[9] == False:
                            ally_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                        enemy_object[int(unit_select) - 1].attack(ally_object[int(opponent_select)-1])
                        print(enemy_object[int(unit_select) - 1].show_stats()[0],"attacked",ally_object[int(unit_select) - 1].show_stats()[0])
                        countdown(int(t))

                    elif int(move_select) == 2:
                        sorcererenemy_UI()
                        opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or ally_object[int(opponent_select) - 1].show_stats()[9] == False:
                            sorcererenemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                        enemy_object[int(unit_select) - 1].heal(enemy_object[int(opponent_select)-1])
                        print(enemy_object[int(unit_select) - 1].show_stats()[0],"healed",enemy_object[int(unit_select) - 1].show_stats()[0])
                        countdown(int(t))
                    
                else:
                    ally_UI()
                    opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or ally_object[int(opponent_select) - 1].show_stats()[9] == False:
                        ally_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    enemy_object[int(unit_select) - 1].attack(ally_object[int(opponent_select)-1])
                    print(enemy_object[int(unit_select) - 1].show_stats()[0],"attacked",ally_object[int(unit_select) - 1].show_stats()[0])
                    countdown(int(t))
                    

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    main_UI()
                    break

        turn += 1

def game_logic_AI():
    global turn
    global GAME

    turn = 0
    GAME = True
    while GAME:
        main_UI()
        ally_UI()
        
        # Ally's turn - Ally select who attacks who
        if len(available_ally) > 0 and len(available_enemy) > 0:
            unit_select = input("\n Choose the available unit in your team (#) : ")
            while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) > len(available_ally) or ally_object[int(unit_select) - 1].show_stats()[9] == False:
                ally_UI()
                print("\n YOU ENTERED WRONG VALUE")
                unit_select = input("\n Choose the available unit in your team (#) : ")

            if ally_object[int(unit_select) - 1].show_stats()[1] == "Sorcerer":
                sorcererheal_UI()
                move_select = input("\n Choose your move (1~2) : ")
                while not move_select.isdigit() or int(move_select) < 0 or int(move_select) > 2:
                    sorcererheal_UI()
                    print("\n YOU ENTERED WRONG VALUE")
                    move_select = input("\n Choose your move (1~2) : ")

                if int(move_select) == 1:
                    sorcererattack_UI()
                    opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or enemy_object[int(opponent_select) - 1].show_stats()[9] == False:
                        sorcererattack_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    ally_object[int(unit_select) - 1].attack(enemy_object[int(opponent_select)-1])
                    print(ally_object[int(unit_select) - 1].show_stats()[0],"attacked",enemy_object[int(unit_select) - 1].show_stats()[0])
                    countdown(int(t))
                    

                elif int(move_select) == 2:
                    sorcererheal_UI()
                    opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                    while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or enemy_object[int(opponent_select) - 1].show_stats()[9] == False:
                        sorcererheal_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                    ally_object[int(unit_select) - 1].heal(ally_object[int(opponent_select)-1])
                    print(ally_object[int(unit_select) - 1].show_stats()[0],"healed",ally_object[int(unit_select) - 1].show_stats()[0])
                    countdown(int(t))

            else:
                enemy_UI()
                opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or enemy_object[int(opponent_select) - 1].show_stats()[9] == False:
                    enemy_UI()
                    print("\n YOU ENTERED WRONG VALUE")
                    opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                ally_object[int(unit_select) - 1].attack(enemy_object[int(opponent_select)-1])
                print(ally_object[int(unit_select) - 1].show_stats()[0],"attacked",enemy_object[int(unit_select) - 1].show_stats()[0])
                countdown(int(t))

            if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                main_UI()
                break
        
            main_UI()
            enemy_UI()

            # Enemy's turn - Enemy select who attacks who
            if len(available_ally) > 0 and len(available_enemy) > 0:
                unit_select = input("\n Choose the available unit in your team (#) : ")
                while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) > len(available_ally) or enemy_object[int(unit_select) - 1].show_stats()[9] == False:
                    enemy_UI()
                    print("\n YOU ENTERED WRONG VALUE")
                    unit_select = input("\n Choose the avaiable unit in your team (#) : ")

                if enemy_object[int(unit_select) - 1].show_stats()[1] == "Sorcerer":
                    sorcererenemy_UI()
                    move_select = input("\n Choose your move (1~2) : ")
                    while not move_select.isdigit() or int(move_select) < 0 or int(move_select) > 2:
                        sorcererenemy_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        move_select = input("\n Choose your move (1~2) : ")

                    if int(move_select) == 1:
                        ally_UI()
                        opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or ally_object[int(opponent_select) - 1].show_stats()[9] == False:
                            ally_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                        enemy_object[int(unit_select) - 1].attack(ally_object[int(opponent_select)-1])
                        print(enemy_object[int(unit_select) - 1].show_stats()[0],"attacked",ally_object[int(unit_select) - 1].show_stats()[0])
                        countdown(int(t))

                    elif int(move_select) == 2:
                        sorcererenemy_UI()
                        opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or ally_object[int(opponent_select) - 1].show_stats()[9] == False:
                            sorcererenemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the unit that you want to spell (#) : ")
                        enemy_object[int(unit_select) - 1].heal(enemy_object[int(opponent_select)-1])
                        print(enemy_object[int(unit_select) - 1].show_stats()[0],"healed",enemy_object[int(unit_select) - 1].show_stats()[0])
                        countdown(int(t))
                    
                else:
                    ally_UI()
                    opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_enemy) or ally_object[int(opponent_select) - 1].show_stats()[9] == False:
                        ally_UI()
                        print("\n YOU ENTERED WRONG VALUE")
                        opponent_select = input("\n Choose the enemy that you want to attack (#) : ")
                    enemy_object[int(unit_select) - 1].attack(ally_object[int(opponent_select)-1])
                    print(enemy_object[int(unit_select) - 1].show_stats()[0],"attacked",ally_object[int(unit_select) - 1].show_stats()[0])
                    countdown(int(t))
                    

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    main_UI()
                    break

        turn += 1

# Cleaning Screen
def clean_screen():
   if os.name == 'posix':
        os.system('clear')
   else:
        os.system('cls')

# GAME LOGIC ===========================================================
def main():
    global turn
    turn = 1
    main_menu()
    if menu_input == 1:
        setting_enemy()
        if game_type == 1:
            setting_size()
            list_objects()
            setting_RN()
            game_logic()
        elif game_type == 2:
            setting_size()
            list_objects()
            setting_RN_AI()
            game_logic()
            

# Start the game
main()
# ┳ ┣ ┫ ┻ ╋
