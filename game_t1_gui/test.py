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

def save_load_page():
    bg = pygame.image.load(resource_path('Game_Assets/Backgrounds/menu_background.png'))
    bg = pygame.transform.scale(bg,(900,600))  
    ogre_set = pygame.image.load(resource_path('Game_Assets/Character_Name/Ogre_Character_Overview.png'))
    ogre_set = pygame.transform.scale(ogre_set,(844,420))

    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(ogre_set,(22,140))
        # Logic goes here

        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                event.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    print(name_input)   # When pressed enter, it prints name in the terminal
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)

def main():
    save_load_page()

# Main ========================================================
main()