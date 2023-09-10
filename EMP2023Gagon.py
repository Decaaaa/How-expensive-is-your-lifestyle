import pygame
import os

pygame.init()

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)
w, h = window.get_size()

bgInit = pygame.image.load(os.path.join("Desktop/EMP Hackathon/", "mainBackground.png"))
bg = pygame.transform.scale(bgInit, (w, h))

bobInit = pygame.image.load(os.path.join("Desktop/EMP Hackathon/", "bobRight.png"))
bob = pygame.transform.scale(bobInit, (w * 100 // 1600, h * 200 // 900))

ladInit = pygame.image.load(os.path.join("Desktop/EMP Hackathon/", "bobLeft.png"))
lad = pygame.transform.scale(ladInit, (w * 100 // 1600, h * 200 // 900))

debagInit = pygame.image.load(os.path.join("Desktop/EMP Hackathon/", "bobStanding.png"))
debag = pygame.transform.scale(debagInit, (w * 100 // 1600, h * 200 // 900))

character_buttons = {
    "Bob": pygame.Rect(w * 200 // 1600, h * 400 // 900, w * 100 // 1600, h * 50 // 900),
    "Lad": pygame.Rect(w * 400 // 1600, h * 400 // 900, w * 100 // 1600, h * 50 // 900),
    "Debag": pygame.Rect(w * 600 // 1600, h * 400 // 900, w * 100 // 1600, h * 50 // 900),
}

selected_character = None

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 100, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    window.blit(bg, (0, 0))

    # Draw character buttons
    for character, rect in character_buttons.items():
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(window, DARK_GREEN, rect)  # Green fill when hovered
            pygame.draw.rect(window, BLACK, rect, 3)  # Black outline for buttons when hovered
        else:
            pygame.draw.rect(window, GREEN, rect)  # Green fill
            pygame.draw.rect(window, BLACK, rect, 3)  # Black outline for buttons
        text = pygame.font.Font(None, 48).render(character, True, WHITE)
        text_rect = text.get_rect(center=(rect.centerx, h * 100 // 900))  # Position text at the top of the button
        window.blit(text, text_rect)

    # Draw selected character
    if selected_character == "Bob":
        window.blit(bob, (w * 100 // 1600, h * 200 // 900))
    elif selected_character == "Lad":
        window.blit(lad, (w * 100 // 1600, h * 200 // 900))
    elif selected_character == "Debag":
        window.blit(debag, (w * 100 // 1600, h * 200 // 900))

    pygame.display.flip()

    # Check for button clicks
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for character, rect in character_buttons.items():
        if rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                selected_character = character

pygame.quit()