import pygame
import random

class Player:
    def __init__(self, screen, ML):
        colors = ["purple", "blue", "green", "pink", "white"]
        self.fix_color = random.choice(colors)

        self.player_pos = pygame.Vector2(250, 400)
        self.dt = 1.2
        self.gravity = .87
        self.player_vel_y = 0
        self.in_ground = True
        self.CONTROL = True
        self.fonte = pygame.font.SysFont("arial", 30)

        self.text_game_over = self.fonte.render("GAME OVER", True, (255,255,255))

        self.alive = True
        self.neuron = ML
    def person_form(self, screen):
        pygame.draw.rect(screen, self.fix_color, (int(self.player_pos.x), int(self.player_pos.y),100, 100))

    def person_movements(self,keys):
        if self.CONTROL == True:
            if keys[pygame.K_s]:
                self.player_pos.y += 0
            if keys[pygame.K_w] and self.in_ground:
                self.player_vel_y = -25
                self.in_ground = False
        if self.CONTROL == False:
            self.GAME_OVER_SCREEN
            self.player_pos.y = 500

        self.player_vel_y += self.gravity
        self.player_pos.y += self.player_vel_y

        if self.player_pos.y > 500:
            self.player_pos.y = 500
            self.player_vel_y = 0
            self.in_ground = True
        else:
            self.in_ground = False

    def hitbox(self):
        player_hitbox = pygame.Rect(int(self.player_pos.x), int(self.player_pos.y), 100, 100)
        return player_hitbox
    
    def GAME_OVER(self, screen):
        self.CONTROL = False
        self.GAME_OVER_SCREEN = screen.blit(self.text_game_over,(640,360))
    