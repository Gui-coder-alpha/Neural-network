import pygame
import Ambient
import Player_fundamentals
import Objects
import MachineLearning

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

Player_one = Player_fundamentals.Player(screen)

Obstacle = Objects.Blocks()

#MACHINELEARNING = MachineLearning.NEUROEVOLUTION()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
#-------> Ambient/Background <-------
    Ambient.base_floor(screen)
#--------------> End <---------------

#--------------> Obstacle/Objects <---------------
    ENEMY_OF_ML = Obstacle.spike(screen)
    losing = Obstacle.spike_hitbox()

#--------------------> End <----------------------


# ----------> Player controls/visual <----------
    ML_PLAYER = Player_one.person_form(screen)

    keys = pygame.key.get_pressed()
    Player_one.person_movements(keys)
    touching = Player_one.hitbox()

#----------------> End Player <-----------------


    if touching.colliderect(losing):
        Player_one.GAME_OVER(screen)
        Obstacle.exclude_spike()

    Obstacle.repeat_spike()





    #MACHINELEARNING.NEUROEVOLUTION(screen)

    pygame.display.flip()
    clock.tick(144)

pygame.quit()