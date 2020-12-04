import sys, os
from random import random, randint, choice
import pandas as pd

# For absolute path in any devices ===============================================
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

try:
    excel_file = pd.read_excel(resource_path('../CStat.xlsx'), 'Character_Stats')
except:
    excel_file = pd.read_excel('./CStat.xlsx', 'Character_Stats')

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
        return self.NAME, self.RACE, self.HP, self.ATK, self.DEF, self.FROZEN, self.POISONED, self.EXP, self.RANK, self.ALIVE, self.MAX_HP
    
    def attack(self, TARGET):
        if self.ACCURACY >= random():
            missed = False
            if self.ATK < TARGET.DEF:
                total_damage = randint(0,5)
            else:    
                total_damage = self.ATK - TARGET.DEF + randint(0,5)
            self.HP -= TARGET.DEF
            TARGET.HP -= total_damage

            # EXP system
            self.EXP += total_damage
            TARGET.EXP += TARGET.DEF
            
            if total_damage >= 10:
                self.EXP += int(total_damage * 1.2)
        else:
            missed = True
            total_damage = 0

        if TARGET.HP <= 0:
            TARGET.ALIVE = False
            self.EXP += int(self.EXP * 1.5)

        if self.HP <= 0:
            if self.TEAM == "ALLY":
                Unit.ally_counter -= 1
            else:
                Unit.enemy_counter -= 1

        if TARGET.HP <= 0:
            if TARGET.TEAM == "ALLY":
                Unit.ally_counter -= 1
            else:
                Unit.enemy_counter -= 1

        self.rank_up()
        TARGET.rank_up()

        return missed, total_damage
    
    def rank_up(self):
        if self.EXP >= 40:
            if self.ID < self.MAX_ID:
                self.EXP = 0
                self.RACE = str(excel_file['Race'][self.ID])
                self.HP = int(excel_file['HP'][self.ID])
                self.MAX_HP = int(excel_file['HP'][self.ID])
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
        self.RACE = 'Ogre'
        self.rank_up()

class Knight(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][3])
        self.MAX_ID = self.ID + 3
        self.ACCURACY = 1
        self.RACE = 'Knight'
        self.rank_up()

class Sorcerer(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.ID = int(excel_file['ID'][6])
        self.MAX_ID = self.ID + 3
        self.ACCURACY = 1
        self.RACE = 'Sorcerer'
        self.rank_up()

    def heal(self,TARGET):      
        total_heal = 0
        if TARGET.TEAM == self.TEAM:
            if self.RANK == 1:
                TARGET.HP += 5
                self.EXP += 5
                total_heal = 5
            elif self.RANK == 2:
                TARGET.HP += 8
                self.EXP += 5
                total_heal = 8
            else:
                TARGET.HP += 10
                self.EXP += 5
                total_heal = 10

        if TARGET.HP > TARGET.MAX_HP:
            TARGET.HP = TARGET.MAX_HP
        
        self.rank_up()
        TARGET.rank_up()
        
        return total_heal