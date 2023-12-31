import pygame
import os
os.chdir("C:/Users/Avkb8/Desktop/EMP Hackathon")

pygame.init()

#Create the game window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = window.get_size()

#Load background images
bgInit = pygame.image.load(os.path.join("./", "background.png"))
bg = pygame.transform.scale(bgInit, (w, h))

#Load character images
bgInit = pygame.image.load(os.path.join("./", "mainBackground.png"))
bg = pygame.transform.scale(bgInit, (w, h))

bobInit = pygame.image.load(os.path.join("./", "bobRight.png"))
bob = pygame.transform.scale(bobInit, (w * 100 // 1600, h * 200 // 900))

ladInit = pygame.image.load(os.path.join("./", "bobLeft.png"))
lad = pygame.transform.scale(ladInit, (w * 100 // 1600, h * 200 // 900))

debagInit = pygame.image.load(os.path.join("./", "bobStanding.png"))
debag = pygame.transform.scale(debagInit, (w * 100 // 1600, h * 200 // 900))


#Create character selection buttons
character_buttons = {
    "Bob": pygame.Rect(w * 200 / 1600, h * 400 / 900, w * 100 / 1600, h * 50 / 900),
    "Lad": pygame.Rect(w * 400 / 1600, h * 400 / 900, w * 100 / 1600, h * 50 / 900),
    "Debag": pygame.Rect(w * 600 / 1600, h * 400 / 900, w * 100 / 1600, h * 50 / 900),
}

#Initialize the selected character
selected_character = None
#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#Clear the screen
    window.blit(bg, (0, 0))

    # Draw character buttons
    for character, rect in character_buttons.items():
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, (0, 255, 0), rect)  # Green fill when hovered
        else:
            pygame.draw.rect(window, (0, 0, 0), rect)  # Black fill when not hovered

#White text
        text = pygame.font.Font(None, 36).render(character, True, (255, 255, 255))
        text_rect = text.get_rect(center=rect.center)
        window.blit(text, text_rect)

    # Draw selected character
    if selected_character == "Bob":
        window.blit(bob, (w * 100 / 1600, h * 200 / 900))
    elif selected_character == "Lad":
        window.blit(lad, (w * 100 / 1600, h * 200 / 900))
    elif selected_character == "Debag":
        window.blit(debag, (w * 100 / 1600, h * 200 / 900))

    pygame.display.flip()

    # Check for button clicks
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for character, rect in character_buttons.items():
        if rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                selected_character = character

#Quit pygame
pygame.quit()