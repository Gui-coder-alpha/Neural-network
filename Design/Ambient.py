import pygame

def base_floor(screen):
    screen.fill('black')
    pygame.draw.rect(screen, "gray", (0, 520, 1280, 720))
    pygame.draw.rect(screen, "gray", (0, 520, 1280, 750))
