import pygame

class Player:
    def __init__(self, screen):
        self.player_pos = pygame.Vector2(screen.get_width() / 4, 400)
        self.dt = 1.2
        self.gravity = .87
        self.player_vel_y = 0
        self.in_ground = True
        self.CONTROL = True
    def person_form(self, screen):
        pygame.draw.rect(screen, "blue", (int(self.player_pos.x), int(self.player_pos.y),100, 100))

    def person_movements(self,keys):
        if self.CONTROL == True:
            if keys[pygame.K_s]:
                self.player_pos.y += 0
            if keys[pygame.K_w] and self.in_ground:
                self.player_vel_y = -25
                self.in_ground = False
            if keys[pygame.K_a]:
                self.player_pos.x -= 5 * self.dt
            if keys[pygame.K_d]:
                self.player_pos.x += 5 * self.dt
        if self.CONTROL == False:
            print('over')



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
    
    def GAME_OVER(self):
        self.CONTROL = False
    