import pygame
import os
import random
os.chdir("C:/Users/Suraj/Downloads/How-expensive-is-your-lifestyle-main/How-expensive-is-your-lifestyle-main")

pygame.init()

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

bbgInit = pygame.image.load(os.path.join("./", "blurredBackground.png"))
bbg = pygame.transform.scale(bbgInit, (w, h))

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

questions = [
    'How often do you eat animal-based products?',
    'What material is your house constructed with?',
    'How many people live in your household?',
    'How energy efficient is your home?',
    'Approximately how much water do you use a day?'
]

answers = [
    'Never/barely',
    'Occasionally - Once or twice a week',
    'Often',
    'Traditional materials - brick and concrete.',
    'A combination of both traditional and eco-friendly materials.',
    'Sustainable and eco-friendly materials such as reclaimed wood, recycled steel, and bamboo.',
    '1-3',
    '4-6',
    '7+',
    'Below Average - poor insulation, non-LED lights, heating/cooling systems used often',
    'Average - Modern appliances, climate controls',
    'Above average - well insulated, efficient lighting and appliances, careful use',
    'Below Average - <80 gallons of water per day',
    'Average - 80-140 gallons per day',
    'Above Average - 140+ gallons per day'
]

reviewLines = [

    'It is best to either have a balanced diet when it comes to meat and vegetables, or reduce it as much as possible.',
    'Most houses are made of wood, which is much better than bricks and concrete.',
    'The average number of persons per household is 2.55 people.',
    'The average amount of electricity used per month is 1,037 kWh per person.',
    'The average amount of water used per person per day is around 120 gallons per day.'

]

neededReviewLines = []

smallFont = pygame.font.Font('freesansbold.ttf', int(w * 25/1600))
font = pygame.font.Font('freesansbold.ttf', int(w * 50/1600))
midFont = pygame.font.Font('freesansbold.ttf', int(w * 75/1600))
bigFont = pygame.font.Font('freesansbold.ttf', int(w * 100/1600))
##-------------
doorText = bigFont.render('Choose a path:', True, (255,255,255), None)
doorText2 = bigFont.render('(go to door and press space)', True, (255,255,255), None)

qI = random.randint(0, len(questions) - 1)

currAnswers = []
for i in range(3):
    currAnswers.append(answers[qI * 3 + i])

button1Rect = pygame.Rect(w * 0/1600, h * 250/900, w * 1600/1600, h * 80/900)
button2Rect = pygame.Rect(w * 0/1600, h * 400/900, w * 1600/1600, h * 80/900)
button3Rect = pygame.Rect(w * 0/1600, h * 550/900, w * 1600/1600, h * 80/900)
answerButtons = [button1Rect, button2Rect, button3Rect]

playerX = w * 40/1600
moveRight = False
moveLeft = False

play = True

susScore = 0

screen = 0


pygame.mixer.init()
pygame.mixer.music.load('begMusic.mp3')
pygame.mixer.music.play()

while play:

    x, y = pygame.mouse.get_pos()
    
    if screen == 0:

        if (not pygame.mixer.get_busy()):
            pygame.mixer.music.queue('begMusic.mp3')

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
        
        if (not pygame.mixer.get_busy()):
            pygame.mixer.music.queue('midMusic.mp3')

        window.blit(mainbg, (0, 0))

        window.blit(doorText, (w * 450/1600, h * 100/900))
        window.blit(doorText2, (w * 100/1600, h * 200/900))

        if ((playerX > w * 190/1600) and (playerX < w * 430/1600)):
            window.blit(doorOpen, (w * 290/1600, h * 450/900))
        else:
            window.blit(doorClosed, (w * 290/1600, h * 450/900))

        if ((playerX > w * 630/1600) and (playerX < w * 870/1600)):
            window.blit(doorOpen, (w * 730/1600, h * 450/900))
        else:
            window.blit(doorClosed, (w * 730/1600, h * 450/900))
        
        if ((playerX > w * 1070/1600) and (playerX < 1310)):
            window.blit(doorOpen, (w * 1170/1600, h * 450/900))
        else:
            window.blit(doorClosed, (w * 1170/1600, h * 450/900))
    
        if ((moveRight and not moveLeft) and (playerX <= w * 1530/1600)):
            playerX += w * 20/1600
            window.blit(bobRight, (playerX, h * 525/900))
        elif ((moveLeft) and (playerX >= w * 20/1600)):
            playerX -= w * 20/1600
            window.blit(bobLeft, (playerX, h * 525/900))           
        else:
            window.blit(bobStanding, (playerX, h * 525/900))

    elif (screen == 2):

        if (not pygame.mixer.get_busy()):
            pygame.mixer.music.queue('midMusic.mp3')

        window.blit(mainbg, (0, 0))

        question = font.render('Question: ' + questions[qI], True, (0,0,0), None)
        window.blit(question,(w * 50/1600, h * 50/900))
        
        if button1Rect.collidepoint(x, y):
            pygame.draw.rect(window, (0, 255, 0), button1Rect)
        else:
            pygame.draw.rect(window, (0, 0, 0), button1Rect)
        if button2Rect.collidepoint(x, y):
            pygame.draw.rect(window, (0, 255, 0), button2Rect)
        else:
            pygame.draw.rect(window, (0, 0, 0), button2Rect)
        if button3Rect.collidepoint(x, y):
            pygame.draw.rect(window, (0, 255, 0), button3Rect)
        else:
            pygame.draw.rect(window, (0, 0, 0), button3Rect)

        button1Text = font.render(currAnswers[0], True, (255, 255, 255), None)
        button2Text = font.render(currAnswers[1], True, (255, 255, 255), None)
        button3Text = font.render(currAnswers[2], True, (255, 255, 255), None)
        
        # Draw buttons and text
        pygame.draw.rect(window, (0, 0, 0), button1Rect, 2)  # Draw button border
        window.blit(button1Text, (w * 5/1600, h * 250/900 + 10))

        pygame.draw.rect(window, (0, 0, 0), button2Rect, 2)  # Draw button border
        window.blit(button2Text, (w * 5/1600, h * 400/900 + 10))

        pygame.draw.rect(window, (0, 0, 0), button3Rect, 2)  # Draw button border
        window.blit(button3Text, (w * 5/1600, h * 550/900 + 10))

    elif screen == 3:

        if (not pygame.mixer.get_busy()):
            pygame.mixer.music.queue('endMusic.mp3')

        index = 0
        
        window.blit(bbg, (0, 0))
        
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900):
            window.blit(quitHov, (w * 500/1600, h * 750/900))
        else:
            window.blit(quit, (w * 500/1600, h * 750/900))
            
        if susScore >= 7:
            title = font.render('You do not have a sustainable lifestyle!', True, (0,0,0), None)
            window.blit(title, (w * 200/1600, h * 100/900))
            title = font.render('But that is ok.', True, (0,0,0), None)
            window.blit(title, (w * 500/1600, h * 150/900))
        else:
            title = font.render('You have a sustainable lifestyle!', True, (0,0,0), None)
            window.blit(title, (w * 400/1600, h * 50/900))
            
        if len(neededReviewLines) > 0:              
            title = font.render('Compared to others in Washington:', True, (0,0,0), None)
            window.blit(title, (w * 60/1600, h * 300/900))
                
            for i in neededReviewLines:
                line = smallFont.render(i, True, (0,0,0), None)
                window.blit(line, (w * 60/1600, (h * 400/900 + 50 * index)))
                index += 1
            
    elif screen == 4:

        if (not pygame.mixer.get_busy()):
            pygame.mixer.music.queue('begMusic.mp3')

        window.blit(instructbg, (0, 0))
        if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900):
            window.blit(backHov, (w * 500/1600, h * 750/900))
        else:
            window.blit(back, (w * 500/1600, h * 750/900))
            
    elif screen == 5:

        if (not pygame.mixer.get_busy()):
            pygame.mixer.music.queue('begMusic.mp3')

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
                pygame.mixer.music.load('midMusic.mp3')
                pygame.mixer.music.play()
            elif (x > w * 900/1600  and x < w * 1500/1600 and y > h * 640/900 and y < h * 760/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False
            elif (x > w * 900/1600  and x < w * 1500/1600 and y > h * 320/900 and y < h * 440/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 4
            elif (x > w * 900/1600  and x < w * 1500/1600 and y > h * 480/900 and y < h * 600/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 5
                
        elif screen == 3:
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900 and event.type == pygame.MOUSEBUTTONDOWN):
                play = False
        
        elif screen == 1:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    if ((playerX > w * 190/1600) and (playerX < w * 430/1600)):
                        screen = 2
                    if ((playerX > w * 630/1600) and (playerX < w * 870/1600)):
                        screen = 2
                    if ((playerX > w * 1070/1600) and (playerX < w * 1310/1600)):
                        screen = 2
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
            
            if (button1Rect.collidepoint(x, y)) and (event.type == pygame.MOUSEBUTTONDOWN):
                screen = 1

                length = len(currAnswers)
                for i in range(length):
                    answers.remove(currAnswers.pop(length - i - 1))
                questions.pop(qI)

                if (len(questions) > 1):
                    qI = random.randint(0, len(questions) - 1)
                elif len(questions) == 1:
                    qI = 0
                    
                if (len(answers) > 0):
                    for i in range(length):
                        currAnswers.append(answers[qI * length + i])
                
            elif (button2Rect.collidepoint(x, y)) and (event.type == pygame.MOUSEBUTTONDOWN):
                susScore += 1
                screen = 1

                length = len(currAnswers)
                for i in range(length):
                    answers.remove(currAnswers.pop(length - i - 1))
                questions.pop(qI)

                if (len(questions) > 1):
                    qI = random.randint(0, len(questions) - 1)
                elif len(questions) == 1:
                    qI = 0

                if (len(answers) > 0):
                    for i in range(length):
                        currAnswers.append(answers[qI * length + i])

            elif (button3Rect.collidepoint(x, y)) and (event.type == pygame.MOUSEBUTTONDOWN):

                neededReviewLines.append(reviewLines[qI])
                reviewLines.pop(qI)
                susScore += 2
                screen = 1

                length = len(currAnswers)
                for i in range(length):
                    answers.remove(currAnswers.pop(length - i - 1))
                questions.pop(qI)

                if (len(questions) > 1):
                    qI = random.randint(0, len(questions) - 1)
                elif len(questions) == 1:
                    qI = 0

                if (len(answers) > 0):
                    for i in range(length):
                        currAnswers.append(answers[qI * length + i])
            
            if (len(questions) == 0):
                screen = 3
                pygame.mixer.music.load('endMusic.mp3')
                pygame.mixer.music.play()
                
        elif screen == 3 or 4:
            if (x > w * 500/1600  and x < w * 1100/1600 and y > h * 750/900 and y < h * 870/900 and event.type == pygame.MOUSEBUTTONDOWN):
                screen = 0
                

    pygame.display.update()