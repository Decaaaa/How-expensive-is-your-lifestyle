import pygame
import os
import random
from pygame import mixer

pygame.init()
mixer.init()

#makes window and sets main menu background
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = window.get_size()

mainbgInit = pygame.image.load(os.path.join("./", "mainBackground.png"))
mainbg = pygame.transform.scale(mainbgInit, (w, h))

bgInit = pygame.image.load(os.path.join("./", "background.png"))
bg = pygame.transform.scale(bgInit, (w, h))

instructbgInit = pygame.image.load(os.path.join("./", "InstructionsBackground.png"))
instructbg = pygame.transform.scale(instructbgInit, (w, h))

tcBGInit = pygame.image.load(os.path.join("./", "tcBackground.png"))
tcBG = pygame.transform.scale(tcBGInit, (w, h))

#quit button all initialized and scaled here
#-------------
quitInit = pygame.image.load(os.path.join("./", "quit.png"))
quit = pygame.transform.scale(quitInit, (w * 600/1600, h * 120/900))
quitHovInit = pygame.image.load(os.path.join("./", "quitHov.png"))
quitHov = pygame.transform.scale(quitHovInit, (w * 600/1600, h * 120/900))

#quit button all initialized and scaled here
backInit = pygame.image.load(os.path.join("./", "back.png"))
back = pygame.transform.scale(backInit, (w * 600/1600, h * 120/900))
backHovInit = pygame.image.load(os.path.join("./", "backHov.png"))
backHov = pygame.transform.scale(backHovInit, (w * 600/1600, h * 120/900))

#Start button, instruction button, and the cause button all initialized and scaled here
startButInit = pygame.image.load(os.path.join("./", "startBut.png"))
startBut = pygame.transform.scale(startButInit, (w * 600/1600, h * 120/900))
startButHovInit = pygame.image.load(os.path.join("./", "startButHov.png"))
startButHov = pygame.transform.scale(startButHovInit, (w * 600/1600, h * 120/900))

instructionButInit = pygame.image.load(os.path.join("./", "instructionsBut.png"))
instructionBut = pygame.transform.scale(instructionButInit, (w * 600/1600, h * 120/900))
instructionButHovInit = pygame.image.load(os.path.join("./", "instructionsButHov.png"))
instructionButHov = pygame.transform.scale(instructionButHovInit, (w * 600/1600, h * 120/900))

tcButInit = pygame.image.load(os.path.join("./", "causeBut.png"))
tcBut = pygame.transform.scale(tcButInit, (w * 600/1600, h * 120/900))
tcButHovInit = pygame.image.load(os.path.join("./", "causeButHov.png"))
tcButHov = pygame.transform.scale(tcButHovInit, (w * 600/1600, h * 120/900))

bobStandingInit = pygame.image.load(os.path.join("./", "bobStanding.png"))
bobStanding = pygame.transform.scale(bobStandingInit, (w * 98/1600, h * 245/900))

bobRightInit = pygame.image.load(os.path.join("./", "bobRight.png"))
bobRight = pygame.transform.scale(bobRightInit, (w * 98/1600, h * 245/900))

bobLeftInit = pygame.image.load(os.path.join("./", "bobLeft.png"))
bobLeft = pygame.transform.scale(bobLeftInit, (w * 98/1600, h * 245/900))

doorOpenInit = pygame.image.load(os.path.join("./", "doorOpen.png"))
doorOpen = pygame.transform.scale(doorOpenInit, (w * 140/1600, h * 290/900))

doorClosedInit = pygame.image.load(os.path.join("./", "doorClosed.png"))
doorClosed = pygame.transform.scale(doorClosedInit, (w * 140/1600, h * 290/900))

playerX = w * 40/1600
moveRight = False
moveLeft = False

play = True

screen = 0

while play:
    x, y = pygame.mouse.get_pos()
    
    if screen == 0:

        window.blit(bg, (0, 0))
        
        #quit button
        if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 640/900 and y < h * 760/900):
                window.blit(quitHov, (w * 900/1600, h * 640/900))
        else:
            window.blit(quit, (w * 900/1600, h * 640/900))
        #start button
        if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 160/900  and y < h * 280/900):
            window.blit(startButHov, (w * 900/1600, h * 160/900))
        else:
            window.blit(startBut, (w * 900/1600, h * 160/900))
        #instructions button
        if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 320/900 and y < h * 440/900):
            window.blit(instructionButHov, (w * 900/1600, h * 320/900))
        else:
            window.blit(instructionBut, (w * 900/1600, h * 320/900))
        #the cause button
        if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 480/900 and y < h * 600/900):
            window.blit(tcButHov, (w * 900/1600, h * 480/900))
        else:
            window.blit(tcBut, (w * 900/1600, h * 480/900))
            
        pygame.display.update()

    elif screen == 1:

        window.blit(mainbg, (0, 0))

        if ((playerX > 190) and (playerX < 430)):
            window.blit(doorOpen, (290, 450))
        else:
            window.blit(doorClosed, (290, 450))

        if ((playerX > 630) and (playerX < 870)):
            window.blit(doorOpen, (730, 450))
        else:
            window.blit(doorClosed, (730, 450))
        
        if ((playerX > 1070) and (playerX < 1310)):
            window.blit(doorOpen, (1170, 450))
        else:
            window.blit(doorClosed, (1170, 450))
    
        if ((moveRight and not moveLeft) and (playerX <= w * 1530/1600)):
            playerX += w * 20/1600
            window.blit(bobRight, (playerX, h * 525/900))
        elif ((moveLeft) and (playerX >= w * 20/1600)):
            playerX -= w * 20/1600
            window.blit(bobLeft, (playerX, h * 525/900))           
        else:
            window.blit(bobStanding, (playerX, h * 525/900))
    
    elif screen == 2:
        
        window.blit(instructbg, (0, 0))
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900):
            window.blit(backHov, (w * 500/1600, h * 750/900))
        else:
            window.blit(back, (w * 500/1600, h * 750/900))
            
    elif screen == 3:
        window.blit(tcBG, (0, 0))
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900):
            window.blit(backHov, (w * 500/1600, h * 750/900))
        else:
            window.blit(back, (w * 500/1600, h * 750/900))      

    for event in pygame.event.get():
        
        #remove later
        if event.type == pygame.KEYDOWN: #Escape button quits the game
            if (event.key == pygame.K_ESCAPE):
                play = False
        
        if event.type == pygame.QUIT:
            play = False
        
        if screen == 0:
            if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 160/900 and y < h * 280/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 1
            elif (x > w * 900/1600  and x < w * 1500/1600 and y > h * 320/900 and y < h * 440/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 2
            elif (x > w * 900/1600  and x < w * 1500/1600 and y > h * 640/900 and y < h * 760/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False
            elif (x > w * 900/1600  and x < w * 1500/1600 and y > h * 480/900 and y < h * 600/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 3
        
        elif screen == 1:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    if ((playerX > 190) and (playerX < 430)):
                        screen = 3
                    if ((playerX > 630) and (playerX < 870)):
                        screen = 4
                    if ((playerX > 1070) and (playerX < 1310)):
                        sceen = 5
                if ((event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (not (event.key == pygame.K_a or event.key == pygame.K_LEFT))):
                    moveLeft = False
                    moveRight = True
                elif ((event.key == pygame.K_a or event.key == pygame.K_LEFT)):
                    moveLeft = True
                    moveRight = False
            elif (event.type == pygame.KEYUP):
                if ((event.key == pygame.K_d or event.key == pygame.K_RIGHT) and (not (event.key == pygame.K_a or event.key == pygame.K_LEFT))):
                    moveLeft = False
                    moveRight = False
                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT):
                    moveRight = False
                    moveLeft = False
                    
        elif screen == 2:
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 0
                
        elif screen == 3:
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 0
                
    pygame.display.update()