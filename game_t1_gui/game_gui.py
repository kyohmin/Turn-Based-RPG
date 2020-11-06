import pygame, sys
from pygame.locals import *

# Settings ====================================================
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Turn Based RPG - T1')
screen = pygame.display.set_mode((900,600))

# Game Functions ==============================================
def main_menu_page(): 
    # Background Image
    bg = pygame.image.load('./Game_Assets/Backgrounds/menu_background.png')
    bg = pygame.transform.scale(bg,(900,600))
    logo = pygame.image.load('./Game_Assets/Intro_Page/Turn_based_RPG_banner.png')
    logo = pygame.transform.scale(logo,(400,220))


    # Variables
    click = False
    enter = False
    point = 0

    # While Loop
    while True:
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        print("pointer =", point)
        screen.blit(bg,(0,0))
        screen.blit(logo,(250,40))

        if 289 <= mx <= 289+355 and 261 <= my <= 261+52: pass
        if 289 <= mx <= 289+355 and 338 <= my <= 338+52: pass
        if 289 <= mx <= 289+355 and 417 <= my <= 417+52: pass
        if 805 <= mx <= 805+71 and 510 <= my <= 510+65: pass

        if 289 <= mx <= 289+355 and 261 <= my <= 261+52 or point == 1: # Play
            if click or enter:
                enemy_selection_page()
        if 289 <= mx <= 289+355 and 338 <= my <= 338+52 or point == 2: # Save / Load
            if click or enter:
                save_load_page()
        if 289 <= mx <= 289+355 and 417 <= my <= 417+52 or point == 3: # Quit
            if click or enter:
                pygame.quit()
                sys.exit()
        if 805 <= mx <= 805+71 and 510 <= my <= 510+65 or point == 4: # Setting
            if click or enter:
                setting_page()

        click = False
        enter = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if 0 <= point <= 3:
                        point += 1
                if event.key == K_UP:
                    if 2 <= point <= 4:
                        point -= 1
                if event.key == K_RETURN:
                    enter = True
                    
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def enemy_selection_page():
    bg = pygame.image.load('./Game_Assets/Backgrounds/menu_background.png')
    bg = pygame.transform.scale(bg,(900,600))    
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
                    click = True

        pygame.display.update()
        clock.tick(60)

def save_load_page():
    bg = pygame.image.load('./Game_Assets/Backgrounds/menu_background.png')
    bg = pygame.transform.scale(bg,(900,600))    
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
                    click = True

        pygame.display.update()
        clock.tick(60)

def setting_page():
    bg = pygame.image.load('./Game_Assets/Backgrounds/menu_background.png')
    bg = pygame.transform.scale(bg,(900,600))    
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
                    click = True

        pygame.display.update()
        clock.tick(60)

def main():
    main_menu_page()

# Main ========================================================
main()