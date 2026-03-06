import pygame

class Blocks:
    def __init__(self):
        self.rain = True
        self.object_position = pygame.Vector2(1280, 450)
        self.points_for_score = pygame.Vector2(1280,450)

        self.cycle_of_point = 0
        self.fonte = pygame.font.SysFont("arial", 30)
        self.generation_number = 1
        self.Exponencial_value = 8
        self.sum = 1

    def spike(self, screen):
        spike_form = pygame.draw.rect(screen, "red", (int(self.object_position.x), int(self.object_position.y), 100, 150))
        return  spike_form
    def spike_hitbox(self):
        return pygame.Rect((int(self.object_position.x), int(self.object_position.y), 100, 150))
    
    def fly_spike(self, screen):
        spike_draw = pygame.draw.rect(screen, "red", (int(self.object_position.x), int(self.object_position.y)+20, 100, 100))
        return spike_draw
    def fly_hitbox(self):
        return pygame.Rect((int(self.object_position.x), int(self.object_position.y)+20, 100, 100))


    
    def spike_velocity(self):
        self.object_position.x -= self.Exponencial_value
        return self.object_position.x
    
    def speed_info(self):
        return self.Exponencial_value

    def repeat_spike(self):
        if self.object_position.x <= -80:
            self.object_position.x = 1290
            self.cycle_of_point += 1
            self.Exponencial_value += self.sum

    def exclude_spike(self):
        self.object_position.x = 250
        
    def hitbox_point(self, screen):
        scored = pygame.Rect((int(self.object_position.x + 100), int(self.object_position.y), 300, 150))
        return scored
    
    def pause(self):
        self.object_position.x = 1280

    def gen(self, screen):
        self.text_of_gen = self.fonte.render(f"Generation {self.generation_number}", True, (255,255,255))
        screen.blit(self.text_of_gen, (10,10))

    def gen_plus(self):
        self.generation_number += 1