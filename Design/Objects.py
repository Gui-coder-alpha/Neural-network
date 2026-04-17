import pygame
import random

class Blocks:
    def __init__(self):
        self.rain = True
        self.object_position = pygame.Vector2(1580, 562)
        self.points_for_score = pygame.Vector2(1580,562)
        self.orb_position = pygame.Vector2(1380, 532)

        self.cycle_of_point = 0
        self.gen_for_graph = 0
        self.fonte = pygame.font.SysFont("arial", 30)
        self.generation_number = 1
        self.Exponencial_value = 5.2
        self.sum = .4

        self.the_choice = [0, 1, 2]
        self.true_choice = 2
        self.image_spike = pygame.image.load("Design/Images/yep.png").convert_alpha()
        self.image_one_formated = pygame.transform.scale(self.image_spike, (100, 150))
        self.image_bird = pygame.image.load("Design/Images/bird.png").convert_alpha()
        self.image_two_formated = pygame.transform.scale(self.image_bird, (150, 100))
        self.spike_carpet = pygame.image.load("Design/Images/spike_carpet.png").convert_alpha()
        self.spike_carpet_formated = pygame.transform.scale(self.spike_carpet, (300, 150))

        self.orb = pygame.image.load("Design/Images/orb.png").convert_alpha()
        self.orb_formated = pygame.transform.scale(self.orb, (100, 100))




        self.simple_text = "Neuron in real time"
        self.x = 960
        self.y = 300

        self.exclude = 0



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
        if self.true_choice == 2:
            spike_carpet = screen.blit(self.spike_carpet_formated, (int(self.object_position.x), int(self.object_position.y)-50))
            orb_image_real = self.orb_image(screen)
            return spike_carpet, orb_image_real

    def spike_hitboxes(self):
        if self.true_choice == 0:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y), 100, 150))
        if self.true_choice == 1:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y)-200, 100, 150))
        if self.true_choice == 2:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y)-50, 300, 150))
        
    def spike_velocity(self):
        self.object_position.x -= self.Exponencial_value
        self.orb_position.x -= self.Exponencial_value
        return self.object_position.x, self.orb_position.x
    
    def speed_info(self):
        return self.Exponencial_value

    def repeat_spike(self):
        if self.object_position.x <= -400:
            self.object_position.x = 1580
            self.cycle_of_point += 1
            self.Exponencial_value += self.sum
            self.orb_position.x = 1380
            self.random_spike()
    
    def exclude_spike(self):
        self.object_position.x = 250
        self.orb_position.x = 250
        
    def hitbox_point(self):
        if self.true_choice == 0:
            scored = pygame.Rect((int(self.object_position.x + 300), int(self.object_position.y) - 87, 1000, 800))
            return scored
        if self.true_choice == 1:
            scored = pygame.Rect((int(self.object_position.x + 600), int(self.object_position.y)-87, 1000, 800))
            return scored
        if self.true_choice == 2:
            scored = pygame.Rect((int(self.object_position.x + 600), int(self.object_position.y) - 87, 1000, 800))
            return scored
    def pause(self):
        self.object_position.x = 1580
        self.orb_position.x = 1380

    def gen(self, screen):
        self.text_of_gen = self.fonte.render(f"Generation {self.generation_number}", True, (255,255,255))
        screen.blit(self.text_of_gen, (10,10))
        self.text_of_neuron = self.fonte.render(f"{self.simple_text}", True, (255,255,255))
        screen.blit(self.text_of_neuron, (self.x, self.y))

    def gen_plus(self):
        self.generation_number += 1

    def text_change(self):
        self.simple_text = "Loading"
        self.x = 1000
        self.y = 150


    def normal_text(self):
        self.simple_text = "Neuron in real time"
        self.x = 960
        self.y = 300

    def big_wall(self):
        return pygame.Rect((int(self.object_position.x + 300), int(self.object_position.y) - 500, 100, 400))
            
    def orb_hitbox(self):
        if self.true_choice == 2:
            return pygame.Rect((int(self.orb_position.x), int(self.orb_position.y), 100, 100))
        else:
            return pygame.Rect((int(self.orb_position.x), int(self.orb_position.y)+1000, 100, 100))
    
    def orb_image(self, screen):
        orb = screen.blit(self.orb_formated, (int(self.orb_position.x), int(self.orb_position.y), 100, 100))
        return orb