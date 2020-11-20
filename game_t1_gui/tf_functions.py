import pygame,sys
from functions import resource_path
def tf_start(start_btn,box_size,mx,my,change_click,click):
    dest_start = False
    if 289 <= mx <= 289+355 and 261 <= my <= 261+52: # Play
        start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button_Hover.png'))
        start_btn = pygame.transform.scale(start_btn,box_size)
        if change_click:
            start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button_Clicked.png'))
            start_btn = pygame.transform.scale(start_btn,box_size)
        elif click:
            dest_start = True
    else:
        start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button.png'))
        start_btn = pygame.transform.scale(start_btn,box_size)
    return start_btn, dest_start

def tf_save(saved_btn,box_size,mx,my,change_click,click):
    dest_saved = False
    if 289 <= mx <= 289+355 and 338 <= my <= 338+52: # Save / Load
        saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_Files_Hover.png'))
        saved_btn = pygame.transform.scale(saved_btn,box_size)
        if change_click:
            saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_Files_Clicked.png'))
            saved_btn = pygame.transform.scale(saved_btn,box_size)
        elif click:
            dest_saved = True
    else:
        saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_Files.png'))
        saved_btn = pygame.transform.scale(saved_btn,box_size)
    return saved_btn, dest_saved
    
def tf_quit(quit_btn,box_size,mx,my,change_click,click):
    dest_quit = False
    if 289 <= mx <= 289+355 and 417 <= my <= 417+52: # Quit
        quit_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Exit_Button_Hover.png'))
        quit_btn = pygame.transform.scale(quit_btn,box_size)
        if change_click:
            quit_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Exit_Button_Clicked.png'))
            quit_btn = pygame.transform.scale(quit_btn,box_size)
        elif click:
            dest_quit = True
    else:
        quit_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Exit_Button.png'))
        quit_btn = pygame.transform.scale(quit_btn,box_size)
    return quit_btn, dest_quit

def tf_setting(mx,my,click):
    dest_setting = False
    if 805 <= mx <= 805+71 and 510 <= my <= 510+65: # Setting
        if click:
            dest_setting = True
    return dest_setting

def tf_pvp(pvp_btn,box_size,mx,my,change_click,click):
    dest_pvp = False
    if 40 <= mx <= 40+400 and 140 <= my <= 140+400:
        pvp_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_Player_Hover.png'))
        pvp_btn = pygame.transform.scale(pvp_btn,box_size)
        if change_click:
            pvp_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_Player_Clicked.png'))
            pvp_btn = pygame.transform.scale(pvp_btn,box_size)
        elif click:
            dest_pvp = True
    else:
        pvp_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_Player.png'))
        pvp_btn = pygame.transform.scale(pvp_btn,box_size)
    return pvp_btn, dest_pvp

def tf_pvai(pvai_btn,box_size,mx,my,change_click,click):
    dest_pvai = False
    if 460 <= mx <= 460+400 and 140 <= my <= 140+400:
        pvai_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_AI_Hover.png'))
        pvai_btn = pygame.transform.scale(pvai_btn,box_size)
        if change_click:
            pvai_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_AI_Clicked.png'))
            pvai_btn = pygame.transform.scale(pvai_btn,box_size)
        elif click:
            dest_pvai = True
    else:
        pvai_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_AI.png'))
        pvai_btn = pygame.transform.scale(pvai_btn,box_size)
    return pvai_btn, dest_pvai

def tf_one(one_btn,box_size,mx,my,change_click,click):
    dest_one = False
    if 61 <= mx <= 61+252 and 130 <= my <= 130+210:
        one_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/1v1_Hover.png'))
        one_btn = pygame.transform.scale(one_btn,box_size)
        if change_click:
            one_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/1v1_Clicked.png'))
            one_btn = pygame.transform.scale(one_btn,box_size)
        elif click:
            dest_one = True
    else:
        one_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/1v1.png'))
        one_btn = pygame.transform.scale(one_btn,box_size)
    return one_btn, dest_one

def tf_two(two_btn,box_size,mx,my,change_click,click):
    dest_two = False
    if 325 <= mx <= 325+252 and 130 <= my <= 130+210:
        two_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/2v2_Hover.png'))
        two_btn = pygame.transform.scale(two_btn,box_size)
        if change_click:
            two_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/2v2_Clicked.png'))
            two_btn = pygame.transform.scale(two_btn,box_size)
        elif click:
            dest_two = True
    else:
        two_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/2v2.png'))
        two_btn = pygame.transform.scale(two_btn,box_size)
    return two_btn, dest_two

def tf_three(three_btn,box_size,mx,my,change_click,click):
    dest_three = False
    if 589 <= mx <= 589+252 and 130 <= my <= 130+210:
        three_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/3v3_Hover.png'))
        three_btn = pygame.transform.scale(three_btn,box_size)
        if change_click:
            three_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/3v3_Clicked.png'))
            three_btn = pygame.transform.scale(three_btn,box_size)
        elif click:
            dest_three = True
    else:
        three_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/3v3.png'))
        three_btn = pygame.transform.scale(three_btn,box_size)
    return three_btn, dest_three

def tf_four(four_btn,box_size,mx,my,change_click,click):
    dest_four = False
    if 107 <= mx <= 107+329 and 346 <= my <= 346+240:
        four_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/4v4_Hover.png'))
        four_btn = pygame.transform.scale(four_btn,box_size)
        if change_click:
            four_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/4v4_Clicked.png'))
            four_btn = pygame.transform.scale(four_btn,box_size)
        elif click:
            dest_four = True
    else:
        four_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/4v4.png'))
        four_btn = pygame.transform.scale(four_btn,box_size)
    return four_btn, dest_four

def tf_five(five_btn,box_size,mx,my,change_click,click):
    dest_five = False
    if 470 <= mx <= 470+329 and 346 <= my <= 346+240:
        five_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/5v5_Hover.png'))
        five_btn = pygame.transform.scale(five_btn,box_size)
        if change_click:
            five_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/5v5_Clicked.png'))
            five_btn = pygame.transform.scale(five_btn,box_size)
        elif click:
            dest_five = True
    else:
        five_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/5v5.png'))
        five_btn = pygame.transform.scale(five_btn,box_size)
    return five_btn, dest_five

def tf_ogre_select(ogre_btn,box_size,mx,my,change_click,click):
    dest_ogre = False
    if 18 <= mx <= 18+272 and 147 <= my <= 147+363:
        ogre_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Ogre_Hover.png'))
        ogre_btn = pygame.transform.scale(ogre_btn,box_size)
        if change_click:
            ogre_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Ogre_Clicked.png'))
            ogre_btn = pygame.transform.scale(ogre_btn,box_size)
        elif click:
            dest_ogre = True
    else:
        ogre_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Ogre_Setting.png'))
        ogre_btn = pygame.transform.scale(ogre_btn,box_size)
    return ogre_btn, dest_ogre

def tf_knight_select(knight_btn,box_size,mx,my,change_click,click):
    dest_knight = False
    if 317 <= mx <= 317+264 and 153 <= my <= 153+350:
        knight_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Knight_Hover.png'))
        knight_btn = pygame.transform.scale(knight_btn,box_size)
        if change_click:
            knight_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Knight_Clicked.png'))
            knight_btn = pygame.transform.scale(knight_btn,box_size)
        elif click:
            dest_knight = True
    else:
        knight_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Knight_Setting.png'))
        knight_btn = pygame.transform.scale(knight_btn,box_size)
    return knight_btn, dest_knight

def tf_sorcerer_select(sorcerer_btn,box_size,mx,my,change_click,click):
    dest_sorcerer = False
    if 610 <= mx <= 610+272 and 147 <= my <= 147+363:
        sorcerer_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Sorcerer_Hover.png'))
        sorcerer_btn = pygame.transform.scale(sorcerer_btn,box_size)
        if change_click:
            sorcerer_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Sorcerer_Clicked.png'))
            sorcerer_btn = pygame.transform.scale(sorcerer_btn,box_size)
        elif click:
            dest_sorcerer = True
    else:
        sorcerer_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Sorcerer_Setting.png'))
        sorcerer_btn = pygame.transform.scale(sorcerer_btn,box_size)
    return sorcerer_btn, dest_sorcerer