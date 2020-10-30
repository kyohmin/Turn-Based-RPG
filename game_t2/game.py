import os

from random import randrange

      
# Characters Stats============================== 
import random
class Unit:
    def __(init__self):
        self.RANK = 0
        self.EXP = 100
        self.FIGHTABLE = True
        self.ALIVE = True
        self.FROZEN = False
        self.POISONED = False

    def set_NT(self, NAME, TEAM):
        self.NAME = NAME
        self.TEAM = TEAM

    def show_stats(self):
        return self.NAME, self.RACE, self.HP, self.ATK, self.DEF, self.FROZEN, self.POISONED, self.EXP, self.RANK, self.ALIVE      #무슨 뜻인지 이해가 안감. Return?
    
    def attack(self, TARGET):
        
        if TARGET.ALIVE == True:    #내가 죽은지를 인지를 못하는것? 미리 인지를 할 수는 없나
            if self.ALIVE == False:
                 print("You are already dead")    
            elif TARGET.DEF > self.ATK:      #게임의 성사 여부를 판단하는 단계
                pass                         #pass 없애고 공격불가 넣기?
            else:                                    #게임 연산 처리
                TARGET.damage = self.ATK - TARGET.DEF + (random.sample(0,6),1)  #타켓의 데미지는 타겟의 공격력에서 타겟의 방어력을 빼고 보너스 랜덤 점수를 더한다.
                self.HP -= TARGET.DEF
                                                                #TARGET.HP = TARGET.HP + TARGET.DEF - self.ATK      #타겟의 체력는 타겟 체력 더하기 타겟의 방어력 빼기 내 공격력
                TARGET.HP -= TARGET.damage
                self.EXP += TARGET.damage                                    #상대방에게 준 피해 만큼 경험치 더함
                TARGET.EXP += TARGET.DEF
                    
                # EXP system
                self.EXP += self.ATK                              #왜 써져있는건지?
                TARGET.EXP += TARGET.DEF
                if self.EXP == 40:
                    self.rank_up()                 
                if TARGET.EXP == 40:
                    TARGET.rank_up()               #타겟도 레벨업 해야할텐데
        else:
            print("You are not able to attack the dead person")


    
    def special_power_system(self,TARGET):
        if TARGET == self.team:                     #TARGET.team이라고 써야하는지?
            if self.spell == "Heal": 
                TARGET.HP += 5                     #레벨업하면 더해야하는 숫자가 달라져야 하는데 어떻게 되는건지?
            else:
                TARGET != TARGET.poison
        else:
            if self.spell == "Poison":
                if TARGET != TARGET.CURE:
                    TARGET.EXP -= 3
                    
            else:
                TARGET.EXP = 3    #바꿔야함
        
        self.EXP += 5


    def rank_up(self):
        if self.EXP >= 100:
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
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                 ┃" .format(excel_file['HP'][0], excel_file['ATK'][0], excel_file['DEF'][0]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┃       2. [KNIGHT]                                              ┃")
        print("┃          Have Decent Power and Strong Defence                  ┃")
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                 ┃" .format(excel_file['HP'][3], excel_file['ATK'][3], excel_file['DEF'][3]))
        print("┃               [One Hidden Skill in Rank 3]                     ┃")
        print("┃                                                                ┃")
        print("┃       3. [SORCERER]                                            ┃")
        print("┃          Have Weak Power and Defence, but can cast magic       ┃")
        print("┃               Magic Skills : {0}, {1}, and {2}          ┃" .format(excel_file['SP 1'][6], excel_file['SP 2'][6], excel_file['SP 3'][6]))
        print("┃               HP = {0} / ATK = {1} / DEF = {2}                 ┃" .format(excel_file['HP'][6], excel_file['ATK'][6], excel_file['DEF'][6]))
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
            print("┃        HP : {0}        ATK : {1}        DEF : {2}" .format(unit_stat[2], unit_stat[3], unit_stat[4]) + " "*(23 - (len(str(unit_stat[2])) + len(str(unit_stat[3])) + len(str(unit_stat[4])))) + "┃                             ┃   2. CURE                  ┃")
            print("┃        EXP : {0}       RANK : {1}       RACE : {2}" . format(unit_stat[7], unit_stat[8], unit_stat[1]) + " "*(21 - (len(str(unit_stat[7])) + len(str(unit_stat[1])))) + "┃                             ┃   3. FREEZE                ┃")
            print("┃                                                                ┃                             ┃   4. POISON                ┃")
            print("┃                                                                ┃                             ┃                            ┃")

def big_seg_UI(num):
    global avaiablility
    availability = False

    if unit_stat[5] == True and unit_stat[6] == True:
        # FROZEN & POISONED
        # First row
        print("┃   {name} (Frozen & Poisoned) : " .format(name = unit_stat[0]) + " " * (38 - len(unit_stat[0])) + "┃                             ┃                            ┃")
        # Second row
        seg_UI(num)

    elif unit_stat[5] == True:
        # FROZEN
        # First row
        print("┃   {name} (Frozen) : " .format(name = unit_stat[0]) + " " * (49 - len(unit_stat[0])) + "┃                             ┃                            ┃")
        # Second row
        seg_UI(num)
        
    elif unit_stat[6] == True:
        # POISONED
        # First row
        print("┃   {name} (Poisoned) : " .format(name = unit_stat[0]) + " " * (47 - len(unit_stat[0])) + "┃   {num}. {name}" .format(num = num + 1, name = unit_stat[0]) + " " * (24 - (len(str(num)) + len(str(unit_stat[0])))) + "┃   1. ATTACK                ┃")
        # Second row
        seg_UI(num)
        availability = True
        
    else:
        if unit_stat[9] == True:
            # ALIVE
            print("┃   {name} : " .format(name = unit_stat[0]) + " " * (58 - len(unit_stat[0])) + "┃   {num}. {name}" .format(num = num + 1, name = unit_stat[0]) + " " * (24 - (len(str(num)) + len(str(unit_stat[0])))) + "┃   1. ATTACK                ┃")
            seg_UI(num)
            avaiablility = True
            
        else:
            # DEAD
            print("┃   {name} : DEAD" .format(name = unit_stat[0]) + " " * (54 - len(unit_stat[0])) + "┃                             ┃                            ┃")
            print("┃                                                                ┃                             ┃                            ┃")


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
    global turn
    GAME = True
    turn = 1
    main_menu()
    if menu_input == 1:
        setting_enemy()
        if game_type == 1:
            setting_size()
            list_objects()
            setting_RN()
            while GAME:
                main_UI()
                
                # Game play
                ally_UI()
                if len(available_ally) > 0 and len(available.enemy) > 0 :
                    if len(available_ally) == 1:
                        unit_select = input("\n Choose the available unit in your team ({num}): " .format(num = len(available_ally)))
                        while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) != len(available_ally):
                            ally_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            unit_select = input("\n Choose the available unit in your team ({num}): " .format(num = len(available_ally)))
                        enemy_UI()
                        if len(available_enemy) == 1:
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_enemy)))          #어디다가 함수 넣을지
                            if unit_select == Sorcerer:   #ally_object[0] == Sorcerer:
                                self.special_power_system()     #
                            else:
                                self.attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) != len(available_enemy):
                            enemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_enemy)))
                        else:
                            opponent_select = input("\n Choose the enemy that you want to attack (1~{num}): " .format(num = len(available_enemy)))
                            if unit_select == Sorcerer:
                                def special_power_system(self)
                            else:
                                def attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) != len(available_enemy):
                            enemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack (1~{num}): " .format(num = len(available_ally)))

                        ally_object[int(unit_select) - 1].attack(enemy_object[int(opponent_select)-1])
                    else:
                        unit_select = input("\n Choose the available unit in your team (1~{num}): " .format(num = len(available_ally)))
                        while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) > len(available_ally):
                            ally_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            unit_select = input("\n Choose the available unit in your team (1~{num}): " .format(num = len(available_ally)))
                        enemy_UI()
                        if len(available_enemy) == 1:
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_enemy)))          #어디다가 함수 넣을지
                            if unit_select = Sorcerer:
                                def special_power_system(self)
                            else:
                                def attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) != len(available_enemy):
                            enemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_enemy)))
                        else:
                            opponent_select = input("\n Choose the enemy that you want to attack (1~{num}): " .format(num = len(available_enemy)))
                            if unit_select = Sorcerer:
                                def special_power_system(self)
                            else:
                                def attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) != len(available_enemy):
                            enemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack (1~{num}): " .format(num = len(available_ally)))

                        ally_object[int(unit_select) - 1].attack(enemy_object[int(opponent_select)-1])           #위치 알아내야함

                else:
                    if len(available_ally) = 0 and len(availalbe.enemy) = 0: 
                        print("\n You have no available unit in your team or every enemy unit is dead.\n Please press Enter. ")
                        print("Game over")         #둘다 다 죽는게 가능하지 않을려나?
                    elif len(avaliable_ally) = 0:
                        print("Game over and your enemy won the game.\n Please press Enter. ")
                    else:
                        print("Game over and your team won the game.\n Please press Enter. ")

                a = input("quit? ")
                if a == 'quit':
                    GAME = False
                turn += 1

                main_UI()

                enemy_UI()
                if len(available_enemy) > 0 and len(available.ally) > 0
                    if len(available_enemy) == 1:
                        unit_select = input("\n Choose the available unit in your team ({num}): " .format(num = len(available_enemy)))
                        while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) != len(available_enemy):
                            enemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            unit_select = input("\n Choose the available unit in your team ({num}): " .format(num = len(available_enemy)))
                        ally_UI()
                        if len(available_ally) == 1:
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_ally)))
                            if unit_select = Sorcerer:
                                def special_power_system(self)
                            else:
                                def attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) != len(available_ally):
                            ally_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_ally)))                                                                                                   #enemy_object[int(unit_select) - 1].attack(ally_object[int(opponent_select)-1])
                        else:
                            opponent_select = input("\n Choose the enemy that you want to attack (1~{num}): " .format(num = len(available_ally)))
                            if unit_select == Sorcerer:
                                def special_power_system(self)
                            else:
                                def attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) > len(available_ally):
                            ally_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack (1~{num}): " .format(num = len(available_ally)))
                        enemy_object[int(unit_select) - 1].attack(ally_object[int(opponent_select)-1])  #ally_UI()
                    else:
                        unit_select = input("\n Choose the available unit in your team (1~{num}): " .format(num = len(available_enemy)))
                        while not unit_select.isdigit() or int(unit_select) < 0 or int(unit_select) != len(available_enemy):
                            enemy_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            unit_select = input("\n Choose the available unit in your team ({num}): " .format(num = len(available_enemy)))
                        ally_UI()
                        if len(available_ally) == 1:
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_ally)))
                            if unit_select = Sorcerer:
                                def special_power_system(self)
                            else:
                                def attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) != len(available_ally):
                            ally_UI()  #
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_ally)))
                        else:
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_ally)))
                            if unit_select = Sorcerer:
                                def special_power_system(self)
                            else:
                                def attack(self, TARGET)
                        while not opponent_select.isdigit() or int(opponent_select) < 0 or int(opponent_select) != len(available_ally):
                            ally_UI()
                            print("\n YOU ENTERED WRONG VALUE")
                            opponent_select = input("\n Choose the enemy that you want to attack ({num}): " .format(num = len(available_ally)))
                            
                        enemy_object[int(unit_select) - 1].attack(ally_object[int(opponent_select)-1])

                else:
                    if len(available_ally) = 0 and len(availalbe.enemy) = 0:
                        print("\n You have no available unit in your team or every enemy unit is dead.\n Please press Enter. ")
                    elif len(avaliable_ally) = 0:
                        print("Game over and your enemy won the game.\n Please press Enter. ")
                    else:
                        print("Game over and your team won the game.\n Please press Enter. ")

                a = input("quit? ")
                if a == 'quit':
                    GAME = False
                turn += 1

# Start the game
main()
print(available_ally)
