import pygame
import Ambient
import Player_fundamentals
import Objects
import MachineLearning

pygame.init()
screen = pygame.display.set_mode((1280, 720), display= 1)
clock = pygame.time.Clock()
running = True

Player_one = Player_fundamentals.Player(screen)

Obstacle = Objects.Blocks()

Study = MachineLearning.Neuro()

while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    
#-------> Ambient/Background <-------
    Ambient.base_floor(screen)
#--------------> End <---------------
#///////////////////////////////////////////////////////////
#--------------> Obstacle/Objects <---------------
    Obstacle.spike(screen)
    losing = Obstacle.spike_hitbox()
    Obstacle.spike_velocity()

#--------------------> End <----------------------
#///////////////////////////////////////////////////////////
# ----------> Player controls/visual <----------
    Player_one.person_form(screen)

    keys = pygame.key.get_pressed()
    Player_one.person_movements(keys)
    touching = Player_one.hitbox()

#----------------> End Player <-----------------
#///////////////////////////////////////////////////////
#--------------->Lose game<-----------------------
    if touching.colliderect(losing):
        Player_one.GAME_OVER(screen)
        Obstacle.exclude_spike()

    Obstacle.repeat_spike()
#-------------->end of lose game<-------------------------



    Study.Features(Player_one, Obstacle)

    pygame.display.flip()
    clock.tick(144)

pygame.quit()