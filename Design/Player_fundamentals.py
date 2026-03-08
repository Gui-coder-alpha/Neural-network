import pygame
import random


class Player:
    def __init__(self, screen, ML):
        colors = ["Design/Images/dino_1.png", "Design/Images/dino2.png", "Design/Images/dino3.png",
                  "Design/Images/dino4.png","Design/Images/dino5.png","Design/Images/dino6.png",
                  "Design/Images/dino7.png","Design/Images/dino8.png"]
        self.fix_color = random.choice(colors)
        self.image_player1 = pygame.image.load(self.fix_color).convert_alpha()
        #self.image_player2 = pygame.image.load("Design/Images/dino_2.png").convert_alpha()

        self.formated_image1 = pygame.transform.scale(self.image_player1, (140, 140))
        #self.formated_image2 = pygame.transform.scale(self.image_player2, (140, 140))

        #self.sprites_animated = [self.formated_image1, self.formated_image2]

        self.player_pos = pygame.Vector2(250, 400)
        self.dt = 1.2
        self.gravity = .87
        self.player_vel_y = 0
        self.in_ground = True
        self.CONTROL = True
        self.fonte = pygame.font.SysFont("arial", 30)

        self.text_game_over = self.fonte.render("GAME OVER", True, (255,255,255))

        self.neuron = ML
        
        self.alive = True
        self.neuron = ML

        self.score = 0

        self.last_score = -1

        #self.count_frames = 0
        #self.current_frames = 0

    #def animate(self):
     #   self.count_frames += 1
      #  if self.count_frames >= 10:
       #     self.count_frames = 0
        #    self.current_frames = (self.current_frames + 1) % len(self.sprites_animated)
    def person_form(self, screen):
        #self.animate()
        screen.blit(self.formated_image1, (int(self.player_pos.x), int(self.player_pos.y)-40))

    def person_movements(self):
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

    def Jump(self):
        self.player_vel_y -= 25
        self.in_ground = False

    def Loser(self):
        self.player_vel_y = 700
    
    def Unique_points(self):
        self.score += 1
        print(self.score)
    
