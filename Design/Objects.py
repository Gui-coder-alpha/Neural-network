import pygame
import random

class Blocks:
    def __init__(self):
        self.rain = True
        self.object_position = pygame.Vector2(1280, 562)
        self.points_for_score = pygame.Vector2(1280,562)

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
        self.y = 260
        self.orb_activate = False


    def random_spike(self):
        self.true_choice = random.choice(self.the_choice)
        self.orb_activate = True
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
            def orb_form(screen):
                orb_form = screen.blit(self.orb_formated, (int(self.object_position.x) - 170, int(self.object_position.y)-30))
                return orb_form
            return spike_carpet, orb_form(screen)
            
    def orb_jump(self):
        if self.orb_activate == True:
            self.orb_x_position = 170
            self.orb_y_position = 30
            orb_hitbox = pygame.Rect((int(self.object_position.x) - self.orb_x_position, int(self.object_position.y)-self.orb_y_position, 100, 100))
            return orb_hitbox
        else:
            return pygame.Rect(-1000, -1000, 0, 0)

    def spike_hitboxes(self):
        if self.true_choice == 0:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y), 100, 150))
        if self.true_choice == 1:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y)-200, 100, 150))
        if self.true_choice == 2:
            return pygame.Rect((int(self.object_position.x), int(self.object_position.y)-50, 300, 150))
    
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
        self.orb_y_position = 1280
        self.object_position.x = 250
        
    def hitbox_point(self):
        if self.true_choice == 0:
            scored = pygame.Rect((int(self.object_position.x + 100), int(self.object_position.y), 300, 150))
            return scored
        if self.true_choice == 1:
            scored = pygame.Rect((int(self.object_position.x + 100), int(self.object_position.y)+87, 300, 100))
            return scored
        if self.true_choice == 2:
            scored = pygame.Rect((int(self.object_position.x + 300), int(self.object_position.y)+87, 700, 800))
            return scored
    def pause(self):
        self.object_position.x = 1280

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
        self.y = 260

    def big_wall(self):
        return pygame.Rect((int(self.object_position.x + 300), int(self.object_position.y), 3000, 3000))