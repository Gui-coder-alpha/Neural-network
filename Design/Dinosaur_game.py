import pygame
import Ambient
import Player_fundamentals
import Objects


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True



Player_one = Player_fundamentals.Player(screen)


Obstacle = Objects.Blocks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
#-------> Ambient/Background <-------
    Ambient.base_floor(screen)
#--------------> End <---------------

#--------------> Obstacle/Objects <---------------
    Obstacle.spike(screen)
    losing = Obstacle.spike_hitbox()

#--------------------> End <----------------------


# ----------> Player controls/visual <----------
    Player_one.person_form(screen)

    keys = pygame.key.get_pressed()
    Player_one.person_movements(keys)

    touching = Player_one.hitbox()
#----------------> End Player <-----------------


    if touching.colliderect(losing):
        Player_one.GAME_OVER()


    pygame.display.flip()
    clock.tick(144)

pygame.quit()