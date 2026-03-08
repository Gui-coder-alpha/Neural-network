import pygame

def base_floor(screen):
    gray_color = (129, 130, 116)
    floor = (208, 204, 166)

    screen.fill(floor)
    pygame.draw.rect(screen, gray_color, (0, 520, 1280, 720))
    pygame.draw.rect(screen, gray_color, (0, 520, 1280, 750))
