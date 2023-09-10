import pygame
import os
import random

pygame.init()

#makes window and sets main menu background
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = window.get_size()

mainbgInit = pygame.image.load(os.path.join("./", "mainBackground.png"))
mainbg = pygame.transform.scale(mainbgInit, (w, h))

bobStandingInit = pygame.image.load(os.path.join("./", "bobStanding.png"))
bobStanding = pygame.transform.scale(bobStandingInit, (w * 98/1600, h * 245/900))

bobRightInit = pygame.image.load(os.path.join("./", "bobRight.png"))
bobRight = pygame.transform.scale(bobRightInit, (w * 98/1600, h * 245/900))

bobLeftInit = pygame.image.load(os.path.join("./", "bobLeft.png"))
bobLeft = pygame.transform.scale(bobLeftInit, (w * 98/1600, h * 245/900))

playerX = w * 40/1600
moveRight = False
moveLeft = False

play = True

while play:

    x, y = pygame.mouse.get_pos()

    window.blit(mainbg, (0, 0))
    
    if ((moveRight and not moveLeft) and (playerX <= w * 1530/1600)):
        playerX += w * 20/1600
        window.blit(bobRight, (playerX, h * 525/900))
    elif ((moveLeft) and (playerX >= w * 20/1600)):
        playerX -= w * 20/1600
        window.blit(bobLeft, (playerX, h * 525/900))           
    else:
        window.blit(bobStanding, (playerX, h * 525/900))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            play = False

        if event.type == pygame.KEYDOWN: #Escape button quits the game
            if (event.key == pygame.K_ESCAPE):
                play = False
        
        if event.type == pygame.KEYDOWN:
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

    pygame.display.update()