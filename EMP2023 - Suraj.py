import pygame
import os
import random

pygame.init()

#makes window and sets main menu background
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = window.get_size()

bgInit = pygame.image.load(os.path.join("./", "background.png"))
bg = pygame.transform.scale(bgInit, (w, h))

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
    
    for event in pygame.event.get():
        
        #remove later
        if event.type == pygame.KEYDOWN: #Escape button quits the game
            if (event.key == pygame.K_ESCAPE):
                play = False
        
        if event.type == pygame.QUIT:
            play = False
        
        if screen == 0:
            if (x > w * 900/1600  and x < w * 1500/1600 and y > h * 640/900 and y < h * 760/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False
