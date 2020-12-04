import pygame, sys
from pygame.locals import *
from tf_func import *
from functions import *
import concurrent.futures
from  class_file import *

# Settings ====================================================
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Turn Based RPG - T1')
screen = pygame.display.set_mode((900,600))
base_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 32)

def main_menu_page():
    # Background Image
    box_size = (358,52)
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background.png'))
    bg = pygame.transform.scale(bg,(900,600))
    logo = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Turn_based_RPG_banner.png'))
    logo = pygame.transform.scale(logo,(567,269))
    start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button.png'))
    start_btn = pygame.transform.scale(start_btn,box_size)
    saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_ComingSoon.png'))
    saved_btn = pygame.transform.scale(saved_btn,box_size)
    quit_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Exit_Button.png'))
    quit_btn = pygame.transform.scale(quit_btn,box_size)

    change_click = False
    click = False
    # While Loop
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(start_btn,(287,260))
        screen.blit(saved_btn,(287,338))
        screen.blit(quit_btn,(287,415))
        screen.blit(logo,(172,4))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_start,start_btn,box_size,mx,my,change_click,click)
            t3 = executor.submit(tf_quit,quit_btn,box_size,mx,my,change_click,click)

            start_btn, dest_start = t1.result()
            quit_btn, dest_quit = t3.result()

        if dest_start:
            enemy_selection_page()
        elif dest_quit:
            pygame.quit()
            sys.exit()
        

        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)

def enemy_selection_page():
    box_size = (400,400)
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background.png'))
    bg = pygame.transform.scale(bg,(900,600))
    logo = pygame.image.load(resource_path('./Game_Assets/Character_Selection/Enemy_Choice.png'))
    logo = pygame.transform.scale(logo,(543,108))
    pvp_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_Player.png'))
    pvp_btn = pygame.transform.scale(pvp_btn,box_size)
    pvai_btn = pygame.image.load(resource_path('./Game_Assets/Character_Selection/coming_soon.png'))
    pvai_btn = pygame.transform.scale(pvai_btn,box_size)

    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(logo,(195,4))
        screen.blit(pvp_btn,(40,140))
        screen.blit(pvai_btn,(460,140))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_pvp,pvp_btn,box_size,mx,my,change_click,click)
            # t2 = executor.submit(tf_pvai,pvai_btn,box_size,mx,my,change_click,click)
            pvp_btn, dest_pvp = t1.result()
            # pvai_btn, dest_pvai = t2.result()
            
        if dest_pvp:
            team_size()
        # elif dest_pvai:
        #     main_menu_page()


        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)

def team_size():
    index_count = 0
    box1_size = (252,210)
    box2_size = (329,240)
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background.png'))
    bg = pygame.transform.scale(bg,(900,600))
    logo = pygame.image.load(resource_path('./Game_Assets/Team_Size/Team_Size.png'))
    logo = pygame.transform.scale(logo,(543,108))
    one_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/1v1.png'))
    one_btn = pygame.transform.scale(one_btn,box1_size)
    two_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/2v2.png'))
    two_btn = pygame.transform.scale(two_btn,box1_size)
    three_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/3v3.png'))
    three_btn = pygame.transform.scale(three_btn,box1_size)
    four_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/4v4.png'))
    four_btn = pygame.transform.scale(four_btn,box2_size)
    five_btn = pygame.image.load(resource_path('./Game_Assets/Team_Size/5v5.png'))
    five_btn = pygame.transform.scale(five_btn,box2_size)



    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(logo,(195,4))
        screen.blit(one_btn,(61,130))
        screen.blit(two_btn,(325,130))
        screen.blit(three_btn,(589,130))
        screen.blit(four_btn,(107,346))
        screen.blit(five_btn,(470,346))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_one,one_btn,box1_size,mx,my,change_click,click)
            t2 = executor.submit(tf_two,two_btn,box1_size,mx,my,change_click,click)
            t3 = executor.submit(tf_three,three_btn,box1_size,mx,my,change_click,click)
            t4 = executor.submit(tf_four,four_btn,box2_size,mx,my,change_click,click)
            t5 = executor.submit(tf_five,five_btn,box2_size,mx,my,change_click,click)
            
            one_btn, dest_one = t1.result()
            two_btn, dest_two = t2.result()
            three_btn, dest_three = t3.result()
            four_btn, dest_four = t4.result()
            five_btn, dest_five = t5.result()
            
        if dest_one:
            ally_obj_list, enemy_obj_list = list_maker(1)
            character_selection(ally_obj_list,enemy_obj_list, index_count)
        elif dest_two:
            ally_obj_list, enemy_obj_list = list_maker(2)
            character_selection(ally_obj_list,enemy_obj_list,index_count)
        elif dest_three:
            ally_obj_list, enemy_obj_list = list_maker(3)
            character_selection(ally_obj_list,enemy_obj_list,index_count)
        elif dest_four:
            ally_obj_list, enemy_obj_list = list_maker(4)
            character_selection(ally_obj_list,enemy_obj_list,index_count)
        elif dest_five:
            ally_obj_list, enemy_obj_list = list_maker(5)
            character_selection(ally_obj_list,enemy_obj_list,index_count)


        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)

def character_selection(ally_obj_list,enemy_obj_list, index_count):
    if index_count == len(ally_obj_list):
        index_count = 0
        enemy_character_selection(ally_obj_list,enemy_obj_list,index_count)

    box1_size = (272,363)
    box2_size = (264,350)
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background_blurred.png'))
    bg = pygame.transform.scale(bg,(900,600))
    logo = pygame.image.load(resource_path('./Game_Assets/Character_Type/TeamSetting_Header.png'))
    logo = pygame.transform.scale(logo,(523,88))
    ogre_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Ogre_Setting.png'))
    ogre_btn = pygame.transform.scale(ogre_btn,box1_size)
    knight_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Knight_Setting.png'))
    knight_btn = pygame.transform.scale(knight_btn,box2_size)
    sorcerer_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Sorcerer_Setting.png'))
    sorcerer_btn = pygame.transform.scale(sorcerer_btn,box1_size)


    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(logo,(209,21))
        screen.blit(ogre_btn,(18,147))
        screen.blit(knight_btn,(317,153))
        screen.blit(sorcerer_btn,(610,147))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_ogre_select,ogre_btn,box1_size,mx,my,change_click,click)
            t2 = executor.submit(tf_knight_select,knight_btn,box2_size,mx,my,change_click,click)
            t3 = executor.submit(tf_sorcerer_select,sorcerer_btn,box1_size,mx,my,change_click,click)
            
            ogre_btn, dest_ogre = t1.result()
            knight_btn, dest_knight = t2.result()
            sorcerer_btn, dest_sorcerer = t3.result()

        if dest_ogre:
            team_setting('Ogre', index_count, ally_obj_list, enemy_obj_list)
        elif dest_knight:
            team_setting('Knight', index_count, ally_obj_list, enemy_obj_list)
        elif dest_sorcerer:
            team_setting('Sorcerer', index_count, ally_obj_list, enemy_obj_list)

        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)

def team_setting(race, index_count, ally_obj_list, enemy_obj_list):
    box1_size = (60,60)
    box2_size = (844,450)
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background_blurred.png"))
    bg = pygame.transform.scale(bg,(900,600))
    if race == 'Ogre':
        character_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))
    elif race == 'Knight':
        character_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Knight_Character_Overview.png"))
    elif race == 'Sorcerer':
        character_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Sorcerer_Character_Overview.png"))

    character_set = pygame.transform.scale(character_set,box2_size)
    if index_count == 0:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Ally1.png"))
    elif index_count == 1:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Ally2.png"))
    elif index_count == 2:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Ally3.png"))
    elif index_count == 3:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Ally4.png"))
    elif index_count == 4:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Ally5.png"))

    back_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/back_button.png"))
    logo = pygame.transform.scale(logo,(460,120))
    back_page = pygame.transform.scale(back_page,box1_size)
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,box1_size)                                              

    name_input = []
    name_str = ''
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(logo,(220,25))
        screen.blit(character_set,(22,150))
        if race == 'Ogre':
            ogre_stat(screen)
        elif race == 'Knight':
            knight_stat(screen)
        elif race == 'Sorcerer':
            sorcerer_stat(screen)
        screen.blit(next_page,(820,35))    
        screen.blit(back_page,(20,35))
        text_surface = base_font.render(name_str,True,(255,255,255))
        screen.blit(text_surface,(60, 468))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_ts_back,back_page,box1_size,mx,my,change_click,click)
            t2 = executor.submit(tf_ts_next,next_page,box1_size,mx,my,change_click,click,name_str)
            
            back_page, dest_back = t1.result()
            next_page, dest_next = t2.result()

        if dest_back:
            character_selection(ally_obj_list,enemy_obj_list, index_count)
        elif dest_next:
            if race == 'Ogre':
                ally_obj_list[index_count] = Ogre()
                ally_obj_list[index_count].set_NT(name_str,"ALLY")
                index_count += 1
                Unit.ally_counter += 1
                character_selection(ally_obj_list,enemy_obj_list, index_count)
            elif race == 'Knight':
                ally_obj_list[index_count] = Knight()
                ally_obj_list[index_count].set_NT(name_str,"ALLY")
                index_count += 1
                Unit.ally_counter += 1
                character_selection(ally_obj_list,enemy_obj_list,index_count)
            elif race == 'Sorcerer':
                ally_obj_list[index_count] = Sorcerer()
                ally_obj_list[index_count].set_NT(name_str,"ALLY")
                index_count += 1
                Unit.ally_counter += 1
                character_selection(ally_obj_list,enemy_obj_list,index_count)


        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                event.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(name_input) > 0:
                        name_input.pop()
                elif len(name_input) <= 10 and event.unicode.isalpha() == True:
                    name_input += event.unicode
                if event.key == K_RETURN:
                    pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        name_str = ''.join(map(str, name_input))

        pygame.display.update()
        clock.tick(120)

def enemy_character_selection(ally_obj_list,enemy_obj_list, index_count):
    if index_count == len(ally_obj_list):
        battle_ground(ally_obj_list, enemy_obj_list)

    box1_size = (272,363)
    box2_size = (264,350)
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background_blurred.png'))
    bg = pygame.transform.scale(bg,(900,600))
    logo = pygame.image.load(resource_path('./Game_Assets/Character_Type/TeamSetting_Header.png'))
    logo = pygame.transform.scale(logo,(523,88))
    ogre_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Ogre_Setting.png'))
    ogre_btn = pygame.transform.scale(ogre_btn,box1_size)
    knight_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Knight_Setting.png'))
    knight_btn = pygame.transform.scale(knight_btn,box2_size)
    sorcerer_btn = pygame.image.load(resource_path('./Game_Assets/Character_Type/Sorcerer_Setting.png'))
    sorcerer_btn = pygame.transform.scale(sorcerer_btn,box1_size)

    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(logo,(209,21))
        screen.blit(ogre_btn,(18,147))
        screen.blit(knight_btn,(317,153))
        screen.blit(sorcerer_btn,(610,147))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_ogre_select,ogre_btn,box1_size,mx,my,change_click,click)
            t2 = executor.submit(tf_knight_select,knight_btn,box2_size,mx,my,change_click,click)
            t3 = executor.submit(tf_sorcerer_select,sorcerer_btn,box1_size,mx,my,change_click,click)
            
            ogre_btn, dest_ogre = t1.result()
            knight_btn, dest_knight = t2.result()
            sorcerer_btn, dest_sorcerer = t3.result()

        if dest_ogre:
            enemy_team_setting('Ogre', index_count, ally_obj_list, enemy_obj_list)
        elif dest_knight:
            enemy_team_setting('Knight', index_count, ally_obj_list, enemy_obj_list)
        elif dest_sorcerer:
            enemy_team_setting('Sorcerer', index_count, ally_obj_list, enemy_obj_list)

        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)

def enemy_team_setting(race, index_count, ally_obj_list, enemy_obj_list):
    box1_size = (60,60)
    box2_size = (844,450)
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background_blurred.png"))
    bg = pygame.transform.scale(bg,(900,600))
    if race == 'Ogre':
        character_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))
    elif race == 'Knight':
        character_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Knight_Character_Overview.png"))
    elif race == 'Sorcerer':
        character_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Sorcerer_Character_Overview.png"))

    if index_count == 0:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Enemy1.png"))
    elif index_count == 1:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Enemy2.png"))
    elif index_count == 2:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Enemy3.png"))
    elif index_count == 3:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Enemy4.png"))
    elif index_count == 4:
        logo = pygame.image.load(resource_path("./Game_Assets/Character_Name/Character_Name_Enemy5.png"))
        
    logo = pygame.transform.scale(logo,(460,120))
    character_set = pygame.transform.scale(character_set,box2_size)
    back_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/back_button.png"))
    back_page = pygame.transform.scale(back_page,box1_size)
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,box1_size)

    name_input = []
    name_str = ''
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(logo,(220,25))
        screen.blit(character_set,(22,150))
        if race == 'Ogre':
            ogre_stat(screen)
        elif race == 'Knight':
            knight_stat(screen)
        elif race == 'Sorcerer':
            sorcerer_stat(screen)
        screen.blit(next_page,(820,35))    
        screen.blit(back_page,(20,35))
        text_surface = base_font.render(name_str,True,(255,255,255))
        screen.blit(text_surface,(60, 468))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_ts_back,back_page,box1_size,mx,my,change_click,click)
            t2 = executor.submit(tf_ts_next,next_page,box1_size,mx,my,change_click,click,name_str)
            
            back_page, dest_back = t1.result()
            next_page, dest_next = t2.result()

        if dest_back:
            character_selection(ally_obj_list,enemy_obj_list, index_count)
        elif dest_next:
            if race == 'Ogre':
                enemy_obj_list[index_count] = Ogre()
                enemy_obj_list[index_count].set_NT(name_str,"ENEMY")
                Unit.enemy_counter += 1
                index_count += 1
                enemy_character_selection(ally_obj_list,enemy_obj_list, index_count)
            elif race == 'Knight':
                enemy_obj_list[index_count] = Knight()
                enemy_obj_list[index_count].set_NT(name_str,"ENEMY")
                index_count += 1
                Unit.enemy_counter += 1
                enemy_character_selection(ally_obj_list,enemy_obj_list,index_count)
            elif race == 'Sorcerer':
                enemy_obj_list[index_count] = Sorcerer()
                enemy_obj_list[index_count].set_NT(name_str,"ENEMY")
                index_count += 1
                Unit.enemy_counter += 1
                enemy_character_selection(ally_obj_list,enemy_obj_list,index_count)


        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                event.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    if len(name_input) > 0:
                        name_input.pop()
                elif len(name_input) <= 10 and event.unicode.isalpha() == True:
                    name_input += event.unicode
                if event.key == K_RETURN:
                    pass
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        name_str = ''.join(map(str, name_input))

        pygame.display.update()
        clock.tick(120)

def battle_ground(ally_obj_list, enemy_obj_list):
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/battle_background.png'))
    bg = pygame.transform.scale(bg,(900,600))
    turn_num = pygame.image.load(resource_path('./Game_Assets/Battleground/Turn_Box.png'))
    turn_num = pygame.transform.scale(turn_num,(385,65))
    msg_box = pygame.image.load(resource_path('./Game_Assets/Battleground/message_bar.png'))
    msg_box = pygame.transform.scale(msg_box,(855,60))
    turn_box_ally = pygame.image.load(resource_path('./Game_Assets/Battleground/ally_turn.png'))
    turn_box_ally = pygame.transform.scale(turn_box_ally,(155,36))
    turn_box_enemy = pygame.image.load(resource_path('./Game_Assets/Battleground/enemy_turn.png'))
    turn_box_enemy = pygame.transform.scale(turn_box_enemy,(155,36))
    ally_btn_list,enemy_btn_list,ally_stat_list,enemy_stat_list,ally_health_stat_list,enemy_health_stat_list = [], [], [], [], [], []
    base_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 40)
    msg_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 30)
    character_size = (78,93)

    # Empty list maker
    for _ in range(len(ally_obj_list)):
        ally_btn_list.append(0)
        enemy_btn_list.append(0)
        ally_stat_list.append(0)
        enemy_stat_list.append(0)
        ally_health_stat_list.append(0)
        enemy_health_stat_list.append(0)

    name_str = 'TURN - '
    msg = ''
    turn = 1
    click = False
    selected_unit = 0
    selected_target = 0
    player_turn = 0
    atk_sor = False
    heal_sor = False
    selected_team = 0
    selection = False
    missed = False
    total_damage = 0
    msg_surface = msg_font.render(msg,True,(0,0,0))
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(turn_num,(237,22))
        screen.blit(msg_box,(20,500))
        text_surface = base_font.render(name_str + str(turn),True,(0,0,0))
        screen.blit(text_surface,(353,32))
        if player_turn == 0:
            screen.blit(turn_box_ally,(342,80))
        else:
            screen.blit(turn_box_enemy,(342,80))

        # Player 1 vs 1
        if len(ally_obj_list) == 1:
            screen_size = (120,68)
            character_size = (130,155)
            ally_1_loc = (269,238)
            enemy_1_loc = (528,238)

            if player_turn == 0:
                if heal_sor == False:
                    selected_unit = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)

                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                elif heal_sor == True:
                    _ = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    temp = 0
                    if click == True and ally_1_loc[0] <= mx <= ally_1_loc[0] + character_size[0] and ally_1_loc[1] <= my <= ally_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                else:
                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                        
                    else:
                        pass

                if selected_unit != 0 and (selected_target != 0 or selected_team != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                msg = ''
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                msg = ''
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))

                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

            # Enemy's Turn ===============================================================================
            elif player_turn == 1:
                if heal_sor == False:
                    selected_unit = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)

                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 

                elif heal_sor == True:
                    _ = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    temp = 0
                    if click == True and enemy_1_loc[0] <= mx <= enemy_1_loc[0] + character_size[0] and enemy_1_loc[1] <= my <= enemy_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                else:
                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                    else:
                        pass

                if selected_unit != 0 and (selected_team != 0 or selected_target != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            msg = ''
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        msg = ''
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))
                            
                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 0
                    turn += 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)
                    

        # Player 2 vs 2 =============================================================================================================
        elif len(ally_obj_list) == 2:
            screen_size = (120,68)
            character_size = (104,124)
            ally_1_loc = (279,180)
            ally_2_loc = (279,316)
            enemy_1_loc = (498,180)
            enemy_2_loc = (498,316)

            if player_turn == 0:
                if heal_sor == False:
                    selected_unit = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    selected_unit = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 

                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                elif heal_sor == True:
                    _ = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    _ = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    temp = 0
                    if click == True and ally_1_loc[0] <= mx <= ally_1_loc[0] + character_size[0] and ally_1_loc[1] <= my <= ally_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_2_loc[0] <= mx <= ally_2_loc[0] + character_size[0] and ally_2_loc[1] <= my <= ally_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                else:
                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                        
                    else:
                        pass

                if selected_unit != 0 and (selected_target != 0 or selected_team != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                msg = ''
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                msg = ''
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))

                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

            # Enemy's Turn ===============================================================================
            elif player_turn == 1:
                if heal_sor == False:
                    selected_unit = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)

                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 

                elif heal_sor == True:
                    _ = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    temp = 0
                    if click == True and enemy_1_loc[0] <= mx <= enemy_1_loc[0] + character_size[0] and enemy_1_loc[1] <= my <= enemy_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_2_loc[0] <= mx <= enemy_2_loc[0] + character_size[0] and enemy_2_loc[1] <= my <= enemy_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                else:
                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                    else:
                        pass

                if selected_unit != 0 and (selected_team != 0 or selected_target != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            msg = ''
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        msg = ''
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))
                            
                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 0
                    turn += 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)
                    

        # Player 3 vs 3
        elif len(ally_obj_list) == 3:
            screen_size = (120,68)
            character_size = (104,124)
            ally_1_loc = (226,108)
            ally_2_loc = (306,228)
            ally_3_loc = (226,341)
            enemy_1_loc = (563,108)
            enemy_2_loc = (480,228)
            enemy_3_loc = (563,341)

            if player_turn == 0:
                if heal_sor == False:
                    selected_unit = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    selected_unit = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    selected_unit = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 

                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                elif heal_sor == True:
                    _ = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    _ = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    _ = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    temp = 0
                    if click == True and ally_1_loc[0] <= mx <= ally_1_loc[0] + character_size[0] and ally_1_loc[1] <= my <= ally_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_2_loc[0] <= mx <= ally_2_loc[0] + character_size[0] and ally_2_loc[1] <= my <= ally_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_3_loc[0] <= mx <= ally_3_loc[0] + character_size[0] and ally_3_loc[1] <= my <= ally_3_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                else:
                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                        
                    else:
                        pass

                if selected_unit != 0 and (selected_target != 0 or selected_team != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                msg = ''
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                msg = ''
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))

                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

            # Enemy's Turn ===============================================================================
            elif player_turn == 1:
                if heal_sor == False:
                    selected_unit = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)

                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 


                elif heal_sor == True:
                    _ = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    temp = 0
                    if click == True and enemy_1_loc[0] <= mx <= enemy_1_loc[0] + character_size[0] and enemy_1_loc[1] <= my <= enemy_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_2_loc[0] <= mx <= enemy_2_loc[0] + character_size[0] and enemy_2_loc[1] <= my <= enemy_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_3_loc[0] <= mx <= enemy_3_loc[0] + character_size[0] and enemy_3_loc[1] <= my <= enemy_3_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                else:
                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                    else:
                        pass

                if selected_unit != 0 and (selected_team != 0 or selected_target != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            msg = ''
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        msg = ''
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))
                            
                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 0
                    turn += 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

        elif len(ally_obj_list) == 4:
            screen_size = (120,68)
            character_size = (104,124)
            ally_1_loc = (346,185)
            ally_2_loc = (346,321)
            ally_3_loc = (126,93)
            ally_4_loc = (126,356)
            enemy_1_loc = (455,185)
            enemy_2_loc = (455,321)
            enemy_3_loc = (674,93)
            enemy_4_loc = (674,356)

            if player_turn == 0:
                if heal_sor == False:
                    selected_unit = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    selected_unit = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    selected_unit = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    selected_unit = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 

                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                elif heal_sor == True:
                    _ = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    _ = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    _ = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    _ = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    temp = 0
                    if click == True and ally_1_loc[0] <= mx <= ally_1_loc[0] + character_size[0] and ally_1_loc[1] <= my <= ally_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_2_loc[0] <= mx <= ally_2_loc[0] + character_size[0] and ally_2_loc[1] <= my <= ally_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_3_loc[0] <= mx <= ally_3_loc[0] + character_size[0] and ally_3_loc[1] <= my <= ally_3_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_4_loc[0] <= mx <= ally_4_loc[0] + character_size[0] and ally_4_loc[1] <= my <= ally_4_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                else:
                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                        
                    else:
                        pass

                if selected_unit != 0 and (selected_target != 0 or selected_team != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                msg = ''
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                msg = ''
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))

                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

            # Enemy's Turn ===============================================================================
            elif player_turn == 1:
                if heal_sor == False:
                    selected_unit = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)

                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 


                elif heal_sor == True:
                    _ = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    temp = 0
                    if click == True and enemy_1_loc[0] <= mx <= enemy_1_loc[0] + character_size[0] and enemy_1_loc[1] <= my <= enemy_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_2_loc[0] <= mx <= enemy_2_loc[0] + character_size[0] and enemy_2_loc[1] <= my <= enemy_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_3_loc[0] <= mx <= enemy_3_loc[0] + character_size[0] and enemy_3_loc[1] <= my <= enemy_3_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_4_loc[0] <= mx <= enemy_4_loc[0] + character_size[0] and enemy_4_loc[1] <= my <= enemy_4_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                else:
                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                    else:
                        pass

                if selected_unit != 0 and (selected_team != 0 or selected_target != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            msg = ''
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        msg = ''
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))
                            
                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 0
                    turn += 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

        elif len(ally_obj_list) == 5:
            screen_size = (120,68)
            character_size = (104,124)
            ally_1_loc = (346,185)
            ally_2_loc = (346,321)
            ally_3_loc = (126,93)
            ally_4_loc = (126,228)
            ally_5_loc = (126,356)
            enemy_1_loc = (455,185)
            enemy_2_loc = (455,321)
            enemy_3_loc = (674,93)
            enemy_4_loc = (674,228)
            enemy_5_loc = (674,356)

            if player_turn == 0:
                if heal_sor == False:
                    selected_unit = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    selected_unit = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    selected_unit = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    selected_unit = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    selected_unit = selected_character_ally(ally_5_loc,character_size,ally_obj_list[4],ally_btn_list[4],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 

                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_5_loc,character_size,enemy_obj_list[4],enemy_btn_list[4],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                elif heal_sor == True:
                    _ = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target)
                    _ = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    _ = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    _ = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    _ = selected_character_ally(ally_5_loc,character_size,ally_obj_list[4],ally_btn_list[4],click,screen,mx,my,screen_size,selected_unit,selection,player_turn,selected_target) 
                    temp = 0
                    if click == True and ally_1_loc[0] <= mx <= ally_1_loc[0] + character_size[0] and ally_1_loc[1] <= my <= ally_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_2_loc[0] <= mx <= ally_2_loc[0] + character_size[0] and ally_2_loc[1] <= my <= ally_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_3_loc[0] <= mx <= ally_3_loc[0] + character_size[0] and ally_3_loc[1] <= my <= ally_3_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_4_loc[0] <= mx <= ally_4_loc[0] + character_size[0] and ally_4_loc[1] <= my <= ally_4_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                    elif click == True and ally_5_loc[0] <= mx <= ally_5_loc[0] + character_size[0] and ally_5_loc[1] <= my <= ally_5_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_5_loc,character_size,ally_obj_list[4],ally_btn_list[4],click,screen,mx,my,screen_size,temp,selection,player_turn,0)
                else:
                    selected_target = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)
                    selected_target = selected_character_enemy(enemy_5_loc,character_size,enemy_obj_list[4],enemy_btn_list[4],click,screen,mx,my,screen_size,selection,selected_target,player_turn,selected_unit)

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                        
                    else:
                        pass

                if selected_unit != 0 and (selected_target != 0 or selected_team != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                msg = ''
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                msg = ''
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))

                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

            # Enemy's Turn ===============================================================================
            elif player_turn == 1:
                if heal_sor == False:
                    selected_unit = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    selected_unit = selected_character_enemy(enemy_5_loc,character_size,enemy_obj_list[4],enemy_btn_list[4],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)

                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_5_loc,character_size,ally_obj_list[4],ally_btn_list[4],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 


                elif heal_sor == True:
                    _ = selected_character_enemy(enemy_1_loc,character_size,enemy_obj_list[0],enemy_btn_list[0],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_2_loc,character_size,enemy_obj_list[1],enemy_btn_list[1],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_3_loc,character_size,enemy_obj_list[2],enemy_btn_list[2],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_4_loc,character_size,enemy_obj_list[3],enemy_btn_list[3],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    _ = selected_character_enemy(enemy_5_loc,character_size,enemy_obj_list[4],enemy_btn_list[4],click,screen,mx,my,screen_size,selection,selected_unit,player_turn,selected_target)
                    temp = 0
                    if click == True and enemy_1_loc[0] <= mx <= enemy_1_loc[0] + character_size[0] and enemy_1_loc[1] <= my <= enemy_1_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_2_loc[0] <= mx <= enemy_2_loc[0] + character_size[0] and enemy_2_loc[1] <= my <= enemy_2_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_3_loc[0] <= mx <= enemy_3_loc[0] + character_size[0] and enemy_3_loc[1] <= my <= enemy_3_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_4_loc[0] <= mx <= enemy_4_loc[0] + character_size[0] and enemy_4_loc[1] <= my <= enemy_4_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                    elif click == True and enemy_5_loc[0] <= mx <= enemy_5_loc[0] + character_size[0] and enemy_5_loc[1] <= my <= enemy_5_loc[1] + character_size[1]:
                        temp = selected_unit
                        selected_team = selected_character_ally(ally_5_loc,character_size,ally_obj_list[4],ally_btn_list[4],click,screen,mx,my,screen_size,temp,selection,player_turn,0) 
                else:
                    selected_target = selected_character_ally(ally_1_loc,character_size,ally_obj_list[0],ally_btn_list[0],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_2_loc,character_size,ally_obj_list[1],ally_btn_list[1],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_3_loc,character_size,ally_obj_list[2],ally_btn_list[2],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_4_loc,character_size,ally_obj_list[3],ally_btn_list[3],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 
                    selected_target = selected_character_ally(ally_5_loc,character_size,ally_obj_list[4],ally_btn_list[4],click,screen,mx,my,screen_size,selected_target,selection,player_turn,selected_unit) 

                if selected_unit != 0:
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        if click == True and 509 <= mx <= 509 +108 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            atk_sor = True
                        if click == True and 509+108+10 <= mx <= 509+108*2+10 and 514 <= my <= 514+33:
                            click = False
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            screen.blit(msg_surface,(46,508))
                            heal_sor = True
                    else:
                        pass

                if selected_unit != 0 and (selected_team != 0 or selected_target != 0):
                    if selected_unit.show_stats()[1] == 'Sorcerer':
                        if atk_sor == True:
                            msg = ''
                            missed, total_damage = attack(selected_unit,selected_target)
                            msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                            msg_surface = msg_font.render(msg,True,(0,0,0))
                            atk_sor = False
                        else:
                            if heal_sor == False:
                                missed, total_damage = attack(selected_unit,selected_target)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                            elif heal_sor == True:
                                heal(selected_unit,selected_team)
                                msg_surface = msg_font.render(msg,True,(0,0,0))
                                selected_unit = 0
                                selected_team = 0
                                selected_target = 0
                                heal_sor = False
                    elif selected_target != 0:
                        msg = ''
                        missed, total_damage = attack(selected_unit,selected_target)
                        msg = message(selected_unit,selected_target,missed,total_damage,msg,player_turn,screen,atk_sor,heal_sor)
                        msg_surface = msg_font.render(msg,True,(0,0,0))
                            
                    if heal_sor == False:
                        selected_unit = 0
                        selected_team = 0
                        selected_target = 0
                        heal_sor == False
                    player_turn = 0
                    turn += 1

                try:
                    if selected_unit.show_stats()[1] != 'Sorcerer': screen.blit(msg_surface,(46,508))
                except:
                    screen.blit(msg_surface,(46,508))

                if Unit.ally_counter == 0 or Unit.enemy_counter == 0:
                    winner_page(ally_obj_list,enemy_obj_list)

        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = False

        pygame.display.update()
        clock.tick(480)


def winner_page(ally_obj_list,enemy_obj_list):
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background_blurred.png'))
    bg = pygame.transform.scale(bg,(900,600))
    ally_win_finder, enemy_win_finder = [], []
    for i in ally_obj_list:
        ally_win_finder.append(i.show_stats()[9])
    for i in enemy_obj_list:
        enemy_win_finder.append(i.show_stats()[9])

    if True in ally_win_finder:
        winner_logo = pygame.image.load(resource_path('./Game_Assets/Game_Result/Result_Ally.png'))
    elif True in enemy_win_finder:
        winner_logo = pygame.image.load(resource_path('./Game_Assets/Game_Result/Result_Enemy.png'))
    winner_logo = pygame.transform.scale(winner_logo,(776,148))
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(winner_logo,(67,70))


        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                change_click = False
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)


def main():
    main_menu_page()

# Main ========================================================
main()