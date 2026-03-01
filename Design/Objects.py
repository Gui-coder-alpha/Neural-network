import pygame

class Blocks:
    def __init__(self):
        self.rain = True
        self.object_position = pygame.Vector2(1280, 450)
        self.points_for_score = pygame.Vector2(1280,450)

        self.cycle_of_point = 0

    def spike(self, screen):
        spike_form = pygame.draw.rect(screen, "red", (int(self.object_position.x), int(self.object_position.y), 100, 150))
        return  spike_form

    def spike_hitbox(self):
        return pygame.Rect((int(self.object_position.x), int(self.object_position.y), 100, 150))
    
    def spike_velocity(self):
        self.object_position.x -= 8

    def repeat_spike(self):
        if self.object_position == (0, 450):
            self.object_position.x = 1280
            self.cycle_of_point += 1

    def exclude_spike(self):
        self.object_position.x = 250
        
    def hitbox_point(self, screen):
        scored = pygame.Rect((int(self.object_position.x + 100), int(self.object_position.y), 300, 150))
        return scored
    
    def pause(self):
        self.object_position.x = 1280