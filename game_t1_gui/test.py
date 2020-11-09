import pygame, sys
from pygame.locals import *
from functions import *
import concurrent.futures

# Settings ====================================================
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Turn Based RPG - T1')
screen = pygame.display.set_mode((900,600))

def main_menu_page():
    # Background Image
    box_size = (358,52)
    bg = pygame.image.load('./Game_Assets/Intro_Page/Intro_Page.jpg')
    bg = pygame.transform.scale(bg,(900,600))
    start_btn = pygame.image.load('./Game_Assets/Intro_Page/Start_Button.png')
    start_btn = pygame.transform.scale(start_btn,box_size)
    saved_btn = pygame.image.load('./Game_Assets/Intro_Page/Saved_Files.png')
    saved_btn = pygame.transform.scale(saved_btn,box_size)
    quit_btn = pygame.image.load('./Game_Assets/Intro_Page/Exit_Button.png')
    quit_btn = pygame.transform.scale(quit_btn,box_size)

    change_click = False
    click = False
    point = 0
    # While Loop
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(start_btn,(287,260))
        screen.blit(saved_btn,(287,338))
        screen.blit(quit_btn,(287,415))

        if not 289 <= mx <= 289+355 and not 261 <= my <= 261+52: point = 0
        elif not 289 <= mx <= 289+355 and not 338 <= my <= 338+52: point = 0
        elif not 289 <= mx <= 289+355 and not 417 <= my <= 417+52: point = 0
        elif not 805 <= mx <= 805+71 and not 510 <= my <= 510+65: point = 0

        with concurrent.futures.ThreadPoolExecutor() as executor:
            t1 = executor.submit(tf_start,point,start_btn,box_size,mx,my,change_click,click)
            t2 = executor.submit(tf_save,point,saved_btn,box_size,mx,my,change_click,click)
            t3 = executor.submit(tf_quit,point,quit_btn,box_size,mx,my,change_click,click)
            t4 = executor.submit(tf_setting,point,mx,my,click)
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
        clock.tick(60)

def enemy_selection_page():
    bg = pygame.image.load('./Game_Assets/Backgrounds/menu_background.png')
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
                event.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu_page()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def save_load_page():
    bg = pygame.image.load('./Game_Assets/Backgrounds/menu_background.png')
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
        clock.tick(60)

def setting_page():
    bg = pygame.image.load('./Game_Assets/Backgrounds/menu_background.png')
    bg = pygame.transform.scale(bg,(900,600))
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        screen.blit(bg,(0,0))


        click = False
        change_click = False
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
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def main():
    main_menu_page()

# Main ========================================================
main()