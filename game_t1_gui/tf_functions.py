import pygame,sys
from functions import resource_path
def tf_start(point,start_btn,box_size,mx,my,change_click,click):
    dest_start = False
    if 289 <= mx <= 289+355 and 261 <= my <= 261+52: # Play
        start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button_Hover.png'))
        start_btn = pygame.transform.scale(start_btn,box_size)
        point = 1
        if change_click:
            start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button_Clicked.png'))
            start_btn = pygame.transform.scale(start_btn,box_size)
        elif click:
            dest_start = True
    else:
        start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button.png'))
        start_btn = pygame.transform.scale(start_btn,box_size)
    return start_btn, dest_start

def tf_save(point,saved_btn,box_size,mx,my,change_click,click):
    dest_saved = False
    if 289 <= mx <= 289+355 and 338 <= my <= 338+52: # Save / Load
        saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_Files_Hover.png'))
        saved_btn = pygame.transform.scale(saved_btn,box_size)
        point = 2
        if change_click:
            saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_Files_Clicked.png'))
            saved_btn = pygame.transform.scale(saved_btn,box_size)
        elif click:
            dest_saved = True
    else:
        saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_Files.png'))
        saved_btn = pygame.transform.scale(saved_btn,box_size)
    return saved_btn, dest_saved
    
def tf_quit(point,quit_btn,box_size,mx,my,change_click,click):
    dest_quit = False
    if 289 <= mx <= 289+355 and 417 <= my <= 417+52: # Quit
        quit_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Exit_Button_Hover.png'))
        quit_btn = pygame.transform.scale(quit_btn,box_size)
        point = 3
        if change_click:
            quit_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Exit_Button_Clicked.png'))
            quit_btn = pygame.transform.scale(quit_btn,box_size)
        elif click:
            dest_quit = True
    else:
        quit_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Exit_Button.png'))
        quit_btn = pygame.transform.scale(quit_btn,box_size)
    return quit_btn, dest_quit

def tf_setting(point,mx,my,click):
    dest_setting = False
    if 805 <= mx <= 805+71 and 510 <= my <= 510+65: # Setting
        point = 4
        if click:
            dest_setting = True
    return dest_setting

def tf_pvp(point,pvp_btn,box_size,mx,my,change_click,click):
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

def tf_pvai(point,pvai_btn,box_size,mx,my,change_click,click):
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

def tf_one(point,one_btn,box_size,mx,my,change_click,click):
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

def tf_two(point,two_btn,box_size,mx,my,change_click,click):
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

def tf_three(point,three_btn,box_size,mx,my,change_click,click):
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

def tf_four(point,four_btn,box_size,mx,my,change_click,click):
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

def tf_five(point,five_btn,box_size,mx,my,change_click,click):
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