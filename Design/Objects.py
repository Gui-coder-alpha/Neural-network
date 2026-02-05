import pygame

class Blocks:
    def __init__(self):
        self.rain = True

    def spike(self, screen):
        pygame.draw.rect(screen, "red", (600, 450, 100, 150))

    def spike_hitbox(self):
        pega = pygame.Rect(600, 450, 100, 150)
        return pega
