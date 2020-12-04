import os, sys
import pygame
from class_file import *
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


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def list_maker(team_size):
    ally_obj_list, enemy_obj_list = [], []
    for _ in range(team_size):
        ally_obj_list.append('0')
        enemy_obj_list.append('0')

    return ally_obj_list, enemy_obj_list


def attack(unit,target):
    missed, total_damage = unit.attack(target)

    return missed, total_damage


def heal(unit,target):
    total_heal = unit.heal(target)

    return total_heal

def resurrect(unit,target):
    total_ressurect = unit.resurect(target)

    return total_ressurect


def selected_character_ally(location,character_size,unit,unit_btn,click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target):
    # Selected Character
    if unit.show_stats()[9] == True:
        if player_turn == 0:
            if click == True and location[0] <= mx <= location[0] + character_size[0] and location[1] <= my <= location[1] + character_size[1] or selected_unit == unit:
                click = False
                if unit.show_stats()[1] == 'Ogre': 
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre_Selected.png'))
                elif unit.show_stats()[1] == 'Knight':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight_Selected.png'))
                elif unit.show_stats()[1] == 'Sorcerer':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer_Selected.png'))
                # Selected Unit
                unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
                selection = True
                selected_unit = unit

            # Make Character
            elif selection == False:
                if unit.show_stats()[1] == 'Ogre':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre.png'))
                elif unit.show_stats()[1] == 'Knight':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight.png'))
                elif unit.show_stats()[1] == 'Sorcerer':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer.png'))
                unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
        if player_turn == 1:
            if selected_target != 0:
                if click == True and location[0] <= mx <= location[0] + character_size[0] and location[1] <= my <= location[1] + character_size[1] or selected_unit == unit:
                    click = False
                    if unit.show_stats()[1] == 'Ogre': 
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre_Selected.png'))
                    elif unit.show_stats()[1] == 'Knight':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight_Selected.png'))
                    elif unit.show_stats()[1] == 'Sorcerer':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer_Selected.png'))
                    # Selected Unit
                    unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
                    selection = True
                    selected_unit = unit

                # Make Character
                elif selection == False:
                    if unit.show_stats()[1] == 'Ogre':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre.png'))
                    elif unit.show_stats()[1] == 'Knight':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight.png'))
                    elif unit.show_stats()[1] == 'Sorcerer':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer.png'))
                    unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
            else:
                if unit.show_stats()[1] == 'Ogre':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre.png'))
                elif unit.show_stats()[1] == 'Knight':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight.png'))
                elif unit.show_stats()[1] == 'Sorcerer':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer.png'))
                unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))

    else:
        if unit.show_stats()[1] == 'Ogre':
            unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre_Dead.png'))
        elif unit.show_stats()[1] == 'Knight':
            unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight_Dead.png'))
        elif unit.show_stats()[1] == 'Sorcerer':
            unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer_Dead.png'))
        unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))

    # Showing Stats
    stat_screen = pygame.image.load(resource_path('./Game_Assets/Battleground/character_stats.png'))

    if selection == True:
        selected_unit = unit

    exp_len = int((unit.show_stats()[7]/40) * 90)
    if exp_len > 97: exp_len = 90
    hp_len = int((unit.show_stats()[2]/unit.show_stats()[10]) * 90)
    if hp_len > 97: hp_len = 90
    elif hp_len < 0: hp_len = 0
    
    # return self.NAME, self.RACE, self.HP, self.ATK, self.DEF, self.FROZEN, self.POISONED, self.EXP, self.RANK, self.ALIVE
    base_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 18)
    stat_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 14)

    rank_num = base_font.render(str(unit.show_stats()[8]),True,(255,255,255))
    name = base_font.render(str(unit.show_stats()[0]),True,(0,0,0))
    hp_num = base_font.render(str(unit.show_stats()[2]),True,(0,0,0))
    atk_num = stat_font.render(str(unit.show_stats()[3]),True,(255,255,255))
    def_num = stat_font.render(str(unit.show_stats()[4]),True,(255,255,255))




    exp_num = pygame.image.load(resource_path('./Game_Assets/Battleground/exp_bar_thin_green.png'))
    exp_num = pygame.transform.scale(exp_num,(exp_len,3))

    hp_val = pygame.image.load(resource_path('./Game_Assets/Battleground/lowHealth_Bar.png'))
    hp_val = pygame.transform.scale(hp_val,(hp_len,19))

    stat_screen = pygame.transform.scale(stat_screen,screen_size)

    screen.blit(stat_screen,(location[0] - (screen_size[0]+5),location[1]+(character_size[1]*0.3)))
    screen.blit(rank_num,(location[0] - (screen_size[0]-2),location[1]+(character_size[1]*0.3)+2))

    screen.blit(name,(location[0]+character_size[0]*0.2,location[1]+(character_size[1]-5)))
    screen.blit(hp_val,(location[0] - (screen_size[0]-22),location[1]+(character_size[1]*0.3+4)))
    if unit.show_stats()[2] <= 0 :
        hp_num = base_font.render('DEAD',True,(0,0,0))
        screen.blit(hp_num,(location[0] - (screen_size[0]-47),location[1]+(character_size[1]*0.3+3)))
    else:
        screen.blit(hp_num,(location[0] - (screen_size[0]-55),location[1]+(character_size[1]*0.3+3)))
    screen.blit(atk_num,(location[0] - (screen_size[0]-84),location[1]+(character_size[1]*0.3+31)))
    screen.blit(def_num,(location[0] - (screen_size[0]-84),location[1]+(character_size[1]*0.3+47)))
    screen.blit(exp_num,(location[0] - (screen_size[0]-22),location[1]+(character_size[1]*0.3-5)))
    screen.blit(unit_btn,(location))

    return selected_unit

def selected_character_enemy(location,character_size,unit,unit_btn,click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target):
    # Selected Character
    if unit.show_stats()[9] == True:
        if player_turn == 1:
            if click == True and location[0] <= mx <= location[0] + character_size[0] and location[1] <= my <= location[1] + character_size[1] or selected_unit == unit:
                click = False
                if unit.show_stats()[1] == 'Ogre':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre_Selected.png'))
                elif unit.show_stats()[1] == 'Knight':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight_Selected.png'))
                elif unit.show_stats()[1] == 'Sorcerer':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer_Selected.png'))
                
                # Selected Unit
                unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
                unit_btn = pygame.transform.flip(unit_btn,True,False)
                selection = True

            # Make Character
            elif selection == False:
                if unit.show_stats()[1] == 'Ogre':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre.png'))
                elif unit.show_stats()[1] == 'Knight':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight.png'))
                elif unit.show_stats()[1] == 'Sorcerer':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer.png'))
                
                unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
                unit_btn = pygame.transform.flip(unit_btn,True,False)

        if player_turn == 0:
            if selected_target != 0:
                if click == True and location[0] <= mx <= location[0] + character_size[0] and location[1] <= my <= location[1] + character_size[1] or selected_unit == unit:
                    click = False
                    if unit.show_stats()[1] == 'Ogre':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre_Selected.png'))
                    elif unit.show_stats()[1] == 'Knight':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight_Selected.png'))
                    elif unit.show_stats()[1] == 'Sorcerer':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer_Selected.png'))
                    
                    # Selected Unit
                    unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
                    unit_btn = pygame.transform.flip(unit_btn,True,False)
                    selection = True

                # Make Character
                elif selection == False:
                    if unit.show_stats()[1] == 'Ogre':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre.png'))
                    elif unit.show_stats()[1] == 'Knight':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight.png'))
                    elif unit.show_stats()[1] == 'Sorcerer':
                        unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer.png'))
                    unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
                    unit_btn = pygame.transform.flip(unit_btn,True,False)
            else:
                if unit.show_stats()[1] == 'Ogre':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre.png'))
                elif unit.show_stats()[1] == 'Knight':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight.png'))
                elif unit.show_stats()[1] == 'Sorcerer':
                    unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer.png'))
                    

                unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
                unit_btn = pygame.transform.flip(unit_btn,True,False)

    else:
        if unit.show_stats()[1] == 'Ogre':
            unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/ogre_states/Ogre_Dead.png'))
        elif unit.show_stats()[1] == 'Knight':
            unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/knight_states/Knight_Dead.png'))
        elif unit.show_stats()[1] == 'Sorcerer':
            unit_btn = pygame.image.load(resource_path('./Game_Assets/Battleground/sorcerer_states/Sorcerer_Dead.png'))
        
        unit_btn = pygame.transform.scale(unit_btn,(character_size[0],character_size[1]))
        unit_btn = pygame.transform.flip(unit_btn,True,False)

    
    if selection == True:
        selected_unit = unit

    # Showing Stats
    stat_screen = pygame.image.load(resource_path('./Game_Assets/Battleground/character_stats.png'))

    exp_len = int((unit.show_stats()[7]/40) * 90)
    if exp_len > 97: exp_len = 90
    hp_len = int((unit.show_stats()[2]/unit.show_stats()[10]) * 90)
    if hp_len > 97: hp_len = 90
    elif hp_len < 0: hp_len = 0
    
    # return self.NAME, self.RACE, self.HP, self.ATK, self.DEF, self.FROZEN, self.POISONED, self.EXP, self.RANK, self.ALIVE
    base_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 18)
    stat_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 14)

    rank_num = base_font.render(str(unit.show_stats()[8]),True,(255,255,255))
    name = base_font.render(str(unit.show_stats()[0]),True,(0,0,0))
    hp_num = base_font.render(str(unit.show_stats()[2]),True,(0,0,0))
    atk_num = stat_font.render(str(unit.show_stats()[3]),True,(255,255,255))
    def_num = stat_font.render(str(unit.show_stats()[4]),True,(255,255,255))


    exp_num = pygame.image.load(resource_path('./Game_Assets/Battleground/exp_bar_thin_green.png'))
    exp_num = pygame.transform.scale(exp_num,(exp_len,3))

    hp_val = pygame.image.load(resource_path('./Game_Assets/Battleground/lowHealth_Bar.png'))
    hp_val = pygame.transform.scale(hp_val,(hp_len,19))

    stat_screen = pygame.transform.scale(stat_screen,screen_size)

    screen.blit(stat_screen,(location[0]+character_size[0],location[1]+(character_size[1]*0.3)))
    screen.blit(rank_num,(location[0]+character_size[0]+7,location[1]+(character_size[1]*0.3)+2))

    screen.blit(name,(location[0]+character_size[0]*0.2,location[1]+(character_size[1]-5)))
    screen.blit(hp_val,(location[0]+character_size[0]+27,location[1]+(character_size[1]*0.3+4)))
    if unit.show_stats()[2] <= 0 :
        hp_num = base_font.render('DEAD',True,(0,0,0))
        screen.blit(hp_num,(location[0]+character_size[0]+52,location[1]+(character_size[1]*0.3+3)))
    else:
        screen.blit(hp_num,(location[0]+character_size[0]+60,location[1]+(character_size[1]*0.3+3)))
    screen.blit(atk_num,(location[0]+character_size[0]+89,location[1]+(character_size[1]*0.3+31)))
    screen.blit(def_num,(location[0]+character_size[0]+89,location[1]+(character_size[1]*0.3+47)))
    screen.blit(exp_num,(location[0]+character_size[0]+27,location[1]+(character_size[1]*0.3-5)))
    screen.blit(unit_btn,(location))

    return selected_unit

def message(unit,target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor):
    msg = ''
    msg_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 30)
    if unit != 0:
        if unit.show_stats()[1] == 'Sorcerer':
            msg = '[GAME MESSAGE] : Select the move.'

            sor_attack = pygame.image.load(resource_path('./Game_Assets/Battleground/attack_hover.png'))
            sor_attack = pygame.transform.scale(sor_attack,(108,33))

            sor_heal = pygame.image.load(resource_path('./Game_Assets/Battleground/heal_hover.png'))
            sor_heal = pygame.transform.scale(sor_heal,(108,33))

            screen.blit(sor_attack,(509,514))
            screen.blit(sor_heal,(509+108+10,514))

            if atk_sor == True:
                msg ='[GAME MESSAGE] : Select a unit.'
            elif heal_sor == True:
                msg = '[GAME MESSAGE] : Select a unit.'

        elif target != 0:

            if missed == True:
                msg = '[GAME MESSAGE] : ' + unit.show_stats()[0] + ' totally missed his attack!'
            else:
                msg = '[GAME MESSAGE] : ' + unit.show_stats()[0] + ' gave ' + str(total_damage) + ' damage to ' + target.show_stats()[0] + '.'
        else:
            msg = '[GAME MESSAGE] : Select a unit!'

    msg_surface = msg_font.render(msg,True,(0,0,0))
    screen.blit(msg_surface,(46,508))
    return msg

def ogre_stat(screen):
    color = (255,255,255)
    stat_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 25)
    lv1_hp = stat_font.render(str(excel_file['HP'][0]),True,color)
    lv2_hp = stat_font.render(str(excel_file['HP'][1]),True,color)
    lv3_hp = stat_font.render(str(excel_file['HP'][2]),True,color)

    lv1_atk = stat_font.render(str(excel_file['ATK'][0]),True,color)
    lv2_atk = stat_font.render(str(excel_file['ATK'][1]),True,color)
    lv3_atk = stat_font.render(str(excel_file['ATK'][2]),True,color)

    lv1_def = stat_font.render(str(excel_file['ATK'][0]),True,color)
    lv2_def = stat_font.render(str(excel_file['ATK'][1]),True,color)
    lv3_def = stat_font.render(str(excel_file['ATK'][2]),True,color)

    screen.blit(lv1_hp,(522,274))
    screen.blit(lv2_hp,(522,304))
    screen.blit(lv3_hp,(522,336))

    screen.blit(lv1_atk,(635,274))
    screen.blit(lv2_atk,(635,304))
    screen.blit(lv3_atk,(635,336))

    screen.blit(lv1_def,(747,274))
    screen.blit(lv2_def,(747,304))
    screen.blit(lv3_def,(747,336))

def knight_stat(screen):
    color = (255,255,255)
    stat_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 25)
    lv1_hp = stat_font.render(str(excel_file['HP'][3]),True,color)
    lv2_hp = stat_font.render(str(excel_file['HP'][4]),True,color)
    lv3_hp = stat_font.render(str(excel_file['HP'][5]),True,color)

    lv1_atk = stat_font.render(str(excel_file['ATK'][3]),True,color)
    lv2_atk = stat_font.render(str(excel_file['ATK'][4]),True,color)
    lv3_atk = stat_font.render(str(excel_file['ATK'][5]),True,color)

    lv1_def = stat_font.render(str(excel_file['ATK'][3]),True,color)
    lv2_def = stat_font.render(str(excel_file['ATK'][4]),True,color)
    lv3_def = stat_font.render(str(excel_file['ATK'][5]),True,color)

    screen.blit(lv1_hp,(522,274))
    screen.blit(lv2_hp,(522,304))
    screen.blit(lv3_hp,(522,336))

    screen.blit(lv1_atk,(630,274))
    screen.blit(lv2_atk,(630,304))
    screen.blit(lv3_atk,(630,336))

    screen.blit(lv1_def,(747,274))
    screen.blit(lv2_def,(747,304))
    screen.blit(lv3_def,(747,336))


def sorcerer_stat(screen):
    color = (255,255,255)
    stat_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 25)
    lv1_hp = stat_font.render(str(excel_file['HP'][6]),True,color)
    lv2_hp = stat_font.render(str(excel_file['HP'][7]),True,color)
    lv3_hp = stat_font.render(str(excel_file['HP'][8]),True,color)

    lv1_atk = stat_font.render(str(excel_file['ATK'][6]),True,color)
    lv2_atk = stat_font.render(str(excel_file['ATK'][7]),True,color)
    lv3_atk = stat_font.render(str(excel_file['ATK'][8]),True,color)

    lv1_def = stat_font.render(str(excel_file['ATK'][6]),True,color)
    lv2_def = stat_font.render(str(excel_file['ATK'][7]),True,color)
    lv3_def = stat_font.render(str(excel_file['ATK'][8]),True,color)

    lv1_heal = stat_font.render(str(5),True,color)
    lv2_heal = stat_font.render(str(8),True,color)
    lv3_heal = stat_font.render(str(10),True,color)

    screen.blit(lv1_hp,(523,251))
    screen.blit(lv2_hp,(523,284))
    screen.blit(lv3_hp,(523,316))

    screen.blit(lv1_atk,(635,251))
    screen.blit(lv2_atk,(635,284))
    screen.blit(lv3_atk,(635,316))

    screen.blit(lv1_def,(747,251))
    screen.blit(lv2_def,(747,284))
    screen.blit(lv3_def,(747,316))

    screen.blit(lv1_heal,(524,379))
    screen.blit(lv2_heal,(524,411))
    screen.blit(lv3_heal,(524,443))

