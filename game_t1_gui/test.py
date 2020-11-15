import pygame, sys
from pygame.locals import *
from tf_functions import *
from functions import resource_path
import concurrent.futures

# Settings ====================================================
clock = pygame.time.Clock()
pygame.init()
names_list = [] 
pygame.display.set_caption('Turn Based RPG - T1')
screen = pygame.display.set_mode((900,600))
base_font = pygame.font.Font(resource_path("./Game_Assets/gumela.ttf"), 32)                                                 

def ogre1_name():
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background.png"))
    bg = pygame.transform.scale(bg,(900,600))  
    ogre_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))
    ogre_set = pygame.transform.scale(ogre_set,(844,420))
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,(80,80))                                              

    name_input = ''
    change_click = False
    click = False
    point = 0                                                                             #should I write it or not
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(ogre_set,(22,140))
        screen.blit(next_page,(800,25))                                                  
        text_surface = base_font.render(name_input,True,(255,255,255))
        screen.blit(text_surface,(60, 440))
        

        #if not 800 <= mx <= 800+100 and not 25<= my <= 25+100: point = 0         #value 100 is a temporary 

        #with concurrent.futures.ThreadPoolExecutor() as executor:
            ##next_page, dest_next = t1.result()

        #if dest_next:
            #knight1_name()


        change_click = False
        click = False
        CAPSLOCK = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            if event.type == QUIT:
                event.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    ogre1_name = name_input
                    names_list.append(ogre1_name)                                       #made ogre1_name variable to use in the other game logic too
                    if ogre1.name in names_list:
                        event.clear                                                     #clear that already entered text or backspace      #how to make code for backspace?  #Is event.clear right one?
                    else:
                        break                                                              #should I write 'break'?
                #elif event.unicode.isbackspace():
                   # K_CLEAR
                elif len(name_input) < 20 and event.unicode.isalpha() == True:                            #if the limit is 15, len(name_input) < 15
                    name_input += event.unicode
                elif event.unicode.isalpha() == False:
                    pass                                                                  

        pygame.display.update()
        clock.tick(120)


def kngiht1_name():
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background.png"))
    bg = pygame.transform.scale(bg,(900,600))  
    knight_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))        #knight1 image
    knight_set = pygame.transform.scale(knight_set,(844,420))
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,(80,80))                                          #need to change size


    name_input = ''
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(knight_set,(22,140))
        screen.blit(next_page,(800,25))                        #need to change size
        text_surface = base_font.render(name_input,True,(255,255,255))
        screen.blit(text_surface,(60, 445))
        # Logic goes here

        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            '''if event.type == QUIT:
                event.quit()
                sys.exit()'''
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    knight1_name = name_input
                    names_list.append(knight1_name)
                    if knight1.name in names_list:
                        event.clear          #인풋된 것 다시 지우기          #백스페이스 어떻게 하지
                    else:
                        break              
                    break
                elif event.unicode.isspace():
                    pass
                #elif event.unicode.isbackspace():
                   # K_CLEAR
                elif len(name_input) < 20 and event.unicode.isalpha() == True:                            #if the limit is 15, len(name_input) < 15
                    name_input += event.unicode
                elif len(name_input) >= 20 or event.unicode.isalpha() == False:
                    K_CLEAR                                                           #리셋?
                
                                       
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)



def sorcerer1_name():
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background.png"))
    bg = pygame.transform.scale(bg,(900,600))  
    sorcerer_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))              #sorcerer1 image
    sorcerer_set = pygame.transform.scale(sorcerer_set,(844,420))
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,(80,80))                                          #need to change size


    name_input = ''
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(sorcerer_set,(22,140))
        screen.blit(next_page,(800,25))                                              #need to change size
        text_surface = base_font.render(name_input,True,(255,255,255))
        screen.blit(text_surface,(60, 445))
        

        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            '''if event.type == QUIT:
                event.quit()
                sys.exit()'''
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    sorcerer1_name = name_input
                    names_list.append(sorcerer1_name)
                    if sorcerer1.name in names_list:
                        event.clear          #인풋된 것 다시 지우기          #백스페이스 어떻게 하지
                    else:
                        break              
                    break
                elif event.unicode.isspace():
                    pass
                #elif event.unicode.isbackspace():
                   # K_CLEAR
                elif len(name_input) < 20 and event.unicode.isalpha() == True:                            #if the limit is 15, len(name_input) < 15
                    name_input += event.unicode
                elif len(name_input) >= 20 or event.unicode.isalpha() == False:
                    K_CLEAR                                                           #리셋?
                
                                       
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)


def ogre2_name():
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background.png"))
    bg = pygame.transform.scale(bg,(900,600))  
    ogre_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))            #ogre2 image
    ogre_set = pygame.transform.scale(ogre_set,(844,420))
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,(80,80))                                          #need to change size

    name_input = ''
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(ogre_set,(22,140))
        screen.blit(next_page,(800,25))                                                   #need to change location
        text_surface = base_font.render(name_input,True,(255,255,255))
        screen.blit(text_surface,(60, 445))
        
        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            '''if event.type == QUIT:
                event.quit()
                sys.exit()'''
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    ogre2_name = name_input
                    names_list.append(ogre2_name)
                    if ogre2.name in names_list:
                        event.clear                                                     #인풋된 것 다시 지우기       #백스페이스 어떻게 하지
                    else:
                        break                                                              #should I write 'break'?
                #elif event.unicode.isbackspace():
                   # K_CLEAR
                elif len(name_input) < 20 and event.unicode.isalpha() == True:                            #if the limit is 15, len(name_input) < 15
                    name_input += event.unicode
                elif len(name_input) >= 20 or event.unicode.isalpha() == False:
                    K_CLEAR                                                           #리셋?                       
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)


def kngiht2_name():
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background.png"))
    bg = pygame.transform.scale(bg,(900,600))  
    knight_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))        #knight2 image
    knight_set = pygame.transform.scale(knight_set,(844,420))
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,(80,80))                                          #need to change size


    name_input = ''
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(knight_set,(22,140))
        screen.blit(next_page,(800,25))                        #need to change size
        text_surface = base_font.render(name_input,True,(255,255,255))
        screen.blit(text_surface,(60, 445))
        # Logic goes here

        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            '''if event.type == QUIT:
                event.quit()
                sys.exit()'''
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    knight2_name = name_input
                    names_list.append(knight2_name)
                    if knight2.name in names_list:
                        event.clear          #인풋된 것 다시 지우기          #백스페이스 어떻게 하지
                    else:
                        break              
                    break
                elif event.unicode.isspace():
                    pass
                #elif event.unicode.isbackspace():
                   # K_CLEAR
                elif len(name_input) < 20 and event.unicode.isalpha() == True:                            #if the limit is 15, len(name_input) < 15
                    name_input += event.unicode
                elif len(name_input) >= 20 or event.unicode.isalpha() == False:
                    K_CLEAR                                                           #리셋?
                
                                       
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)



def sorcerer2_name():
    bg = pygame.image.load(resource_path("./Game_Assets/Backgrounds/menu_background.png"))
    bg = pygame.transform.scale(bg,(900,600))  
    sorcerer_set = pygame.image.load(resource_path("./Game_Assets/Character_Name/Ogre_Character_Overview.png"))              #sorcerer2 image
    sorcerer_set = pygame.transform.scale(sorcerer_set,(844,420))
    next_page = pygame.image.load(resource_path("./Game_Assets/Character_Name/forward_button.png"))
    next_page = pygame.transform.scale(next_page,(80,80))                                          #need to change size


    name_input = ''
    change_click = False
    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(sorcerer_set,(22,140))
        screen.blit(next_page,(800,25))                                              #need to change size
        text_surface = base_font.render(name_input,True,(255,255,255))
        screen.blit(text_surface,(60, 445))
        # Logic goes here

        change_click = False
        click = False
        # Event Collections
        for event in pygame.event.get():
            # Function to quit game
            '''if event.type == QUIT:
                event.quit()
                sys.exit()'''
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    sorcerer2_name = name_input
                    names_list.append(sorcerer2_name)
                    if sorcerer2.name in names_list:
                        event.clear          #인풋된 것 다시 지우기          #백스페이스 어떻게 하지
                    else:
                        break              
                    break
                elif event.unicode.isspace():
                    pass
                #elif event.unicode.isbackspace():
                   # K_CLEAR
                elif len(name_input) < 20 and event.unicode.isalpha() == True:                            #if the limit is 15, len(name_input) < 15
                    name_input += event.unicode
                elif len(name_input) >= 20 or event.unicode.isalpha() == False:
                    K_CLEAR                                                           #리셋?
                
                                       
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    change_click = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(120)







def main():
    ogre1_name()

# Main ========================================================
main()