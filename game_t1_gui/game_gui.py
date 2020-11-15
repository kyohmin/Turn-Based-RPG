import pygame, sys
from pygame.locals import *
from tf_functions import *
from functions import resource_path
import concurrent.futures

# Settings ====================================================
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Turn Based RPG - T1')
screen = pygame.display.set_mode((900,600))

def main_menu_page():
    # Background Image
    box_size = (358,52)
    bg = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Intro_Page.jpg'))
    bg = pygame.transform.scale(bg,(900,600))
    start_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Start_Button.png'))
    start_btn = pygame.transform.scale(start_btn,box_size)
    saved_btn = pygame.image.load(resource_path('./Game_Assets/Intro_Page/Saved_Files.png'))
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

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_start,start_btn,box_size,mx,my,change_click,click)
            t2 = executor.submit(tf_save,saved_btn,box_size,mx,my,change_click,click)
            t3 = executor.submit(tf_quit,quit_btn,box_size,mx,my,change_click,click)
            t4 = executor.submit(tf_setting,mx,my,click)
            start_btn, dest_start = t1.result()
            saved_btn, dest_saved = t2.result()
            quit_btn, dest_quit = t3.result()
            dest_setting = t4.result()

        if dest_start:
            enemy_selection_page()
        elif dest_saved:
            save_load_page()
        elif dest_quit:
            pygame.quit()
            sys.exit()
        elif dest_setting:
            setting_page()
        

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
    pvai_btn = pygame.image.load(resource_path('./Game_Assets/Player_vs_AI/Player_vs_AI.png'))
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
            t2 = executor.submit(tf_pvai,pvai_btn,box_size,mx,my,change_click,click)
            pvp_btn, dest_pvp = t1.result()
            pvai_btn, dest_pvai = t2.result()
            
        if dest_pvp:
            team_size()
        elif dest_pvai:
            main_menu_page()


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

def save_load_page():
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background.png'))
    bg = pygame.transform.scale(bg,(900,600))  
    change_click = False  
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        screen.blit(bg,(0,0))

        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                event.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu_page()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)

def setting_page():
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background.png'))
    bg = pygame.transform.scale(bg,(900,600))
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        screen.blit(bg,(0,0))


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
            print(1)
            character_selection()
        elif dest_two:
            print(2)
            character_selection()
        elif dest_three:
            print(3)
            character_selection()
        elif dest_four:
            print(4)
            character_selection()
        elif dest_five:
            print(5)
            character_selection()


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

def character_selection():
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
            print('ogre')
        elif dest_knight:
            print('knight')
        elif dest_sorcerer:
            print('sorcerer')

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

def team_setting():
    bg = pygame.image.load(resource_path('./Game_Assets/Backgrounds/menu_background.png'))
    bg = pygame.transform.scale(bg,(900,600))

    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        screen.blit(bg,(0,0))

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