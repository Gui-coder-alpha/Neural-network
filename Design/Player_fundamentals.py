import pygame
import random

class Player:
    def __init__(self, screen, ML):
        colors = [["Design/Dinosaur_Images/Black_Dinosaur(1).png", "Design/Dinosaur_Images/Black_Dinosaur(2).png"],
        ["Design/Dinosaur_Images/Purple_Dinosaur(1).png", "Design/Dinosaur_Images/Purple_Dinosaur(2).png"],
        ["Design/Dinosaur_Images/Red_Dinosaur(1).png", "Design/Dinosaur_Images/Red_Dinosaur(2).png"],
        ["Design/Dinosaur_Images/Green_Dinosaur(1).png", "Design/Dinosaur_Images/Green_Dinosaur(2).png"],
        ["Design/Dinosaur_Images/Pink_Dinosaur(1).png", "Design/Dinosaur_Images/Pink_Dinosaur(2).png"],
        ["Design/Dinosaur_Images/Cian_Dinosaur(1).png", "Design/Dinosaur_Images/Cian_Dinosaur(2).png"],
        ["Design/Dinosaur_Images/Blue_Dinosaur(1).png", "Design/Dinosaur_Images/Blue_Dinosaur(2).png"],
        ["Design/Dinosaur_Images/Yellow_Dinosaur(1).png", "Design/Dinosaur_Images/Yellow_Dinosaur(2).png"]]

        self.fix_color = random.choice(colors)
        self.image_player1 = pygame.image.load(self.fix_color[0]).convert_alpha()
        self.image_player2 = pygame.image.load(self.fix_color[1]).convert_alpha()

        self.formated_image1 = pygame.transform.scale(self.image_player1, (100, 100))
        self.formated_image2 = pygame.transform.scale(self.image_player2, (100, 100))

        self.sprites_animated = [self.formated_image1, self.formated_image2]

        self.player_pos = pygame.Vector2(250, 600)
        self.dt = 1.2
        self.gravity = .98
        self.player_vel_y = 0
        self.in_ground = True
        self.CONTROL = True
        self.fonte = pygame.font.SysFont("arial", 30)

        self.text_game_over = self.fonte.render("GAME OVER", True, (255,255,255))

        self.neuron = ML
        
        self.alive = True
        self.score = 0

        self.last_score = -1

        self.count_frames = 0
        self.current_frames = 0

    def animate(self):
        self.count_frames += 1
        if self.count_frames >= 19:
            self.count_frames = 0
            self.current_frames = (self.current_frames + 1) % len(self.sprites_animated)
    def person_form(self, screen):
        self.animate()
        dinosaur_runs = screen.blit(self.sprites_animated[self.current_frames], (int(self.player_pos.x), int(self.player_pos.y-40)))
        return dinosaur_runs

    def person_movements(self):
        self.player_vel_y += self.gravity
        self.player_pos.y += self.player_vel_y

        if self.player_pos.y > 600: #y += 100
            self.player_pos.y = 600
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
    
