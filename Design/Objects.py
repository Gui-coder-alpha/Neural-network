import pygame
import random

class Blocks:
    def __init__(self):
        self.rain = True
        self.object_position = pygame.Vector2(1280, 450)
        self.points_for_score = pygame.Vector2(1280,450)

        self.cycle_of_point = 0
        self.fonte = pygame.font.SysFont("arial", 30)
        self.generation_number = 1
        self.Exponencial_value = 5
        self.sum = .4

        self.the_choice = [0, 1]
        self.true_choice = 0
        self.image_spike = pygame.image.load("Design/Images/yep.png").convert_alpha()
        self.image_one_formated = pygame.transform.scale(self.image_spike, (150, 200))
        self.image_bird = pygame.image.load("Design/Images/bird.png").convert_alpha()
        self.image_two_formated = pygame.transform.scale(self.image_bird, (200, 150))

    def random_spike(self):
        self.true_choice = random.choice(self.the_choice)
        return self.true_choice


    def spikes(self, screen):
        if self.true_choice == 0:
            spike_form = screen.blit(self.image_one_formated, (int(self.object_position.x), int(self.object_position.y)-50))
            return  spike_form
        if self.true_choice == 1:
            spike_draw = screen.blit(self.image_two_formated, (int(self.object_position.x), int(self.object_position.y)-200))
            return spike_draw
    def spike_hitboxes(self):
        if self.true_choice == 0:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y), 100, 150))
        if self.true_choice == 1:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y)-200, 100, 150))


    
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
            self.random_spike()
    def exclude_spike(self):
        self.object_position.x = 250
        
    def hitbox_point(self, screen):
        if self.true_choice == 0:
            scored = pygame.Rect((int(self.object_position.x + 100), int(self.object_position.y), 300, 150))
            return scored
        if self.true_choice == 1:
            scored = pygame.Rect((int(self.object_position.x + 100), int(self.object_position.y)+87, 300, 100))
            return scored

    def pause(self):
        self.object_position.x = 1280

    def gen(self, screen):
        self.text_of_gen = self.fonte.render(f"Generation {self.generation_number}", True, (255,255,255))
        screen.blit(self.text_of_gen, (10,10))

    def gen_plus(self):
        self.generation_number += 1