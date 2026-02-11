import pygame

class Blocks:
    def __init__(self):
        self.rain = True
        self.object_position = pygame.Vector2(1280, 450)

    def spike(self, screen):
        spike_form = pygame.draw.rect(screen, "red", (int(self.object_position.x), int(self.object_position.y), 100, 150))
        return  spike_form

    def spike_hitbox(self):
        self.object_position.x -= 8
        return pygame.Rect((int(self.object_position.x), int(self.object_position.y), 100, 150))

    def repeat_spike(self):
        if self.object_position == (0, 450):
            self.object_position.x = 1280

    def exclude_spike(self):
        self.object_position.x = 250