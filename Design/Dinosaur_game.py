import pygame
import Ambient
import Player_fundamentals
import Objects
import MachineLearning

pygame.init()
screen = pygame.display.set_mode((1280, 720), display=1)
clock = pygame.time.Clock()
running = True

#---------FUNCTIONS-----------------
Obstacle = Objects.Blocks()

Iterations = 10

Population = []
for _ in range(Iterations):
    ML = MachineLearning.Neuro()
    Players = Player_fundamentals.Player(screen, ML)
    Players.neuron = ML
    Population.append(Players)

Errors = []
Losers = 0
timeout = False
runs = True

while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    
#-------> Ambient/Background <-------
    Ambient.base_floor(screen)
#--------------> End <---------------
#///////////////////////////////////////////////////////////
#--------------> Obstacle/Objects <---------------
    points = Obstacle.hitbox_point(screen)
    Obstacle.spike(screen)
    losing = Obstacle.spike_hitbox()
    Obstacle.spike_velocity()

#--------------------> End <----------------------
#///////////////////////////////////////////////////////////
# ----------> Player controls/visual <----------
    #Player_one.person_form(screen)

    #keys = pygame.key.get_pressed()
    #Player_one.person_movements(keys)
    #touching = Player_one.hitbox()

#----------------> End Player <-----------------
#///////////////////////////////////////////////////////
#--------------->Lose game<-----------------------
    #if touching.colliderect(losing):
     #   Player_one.GAME_OVER(screen)
      #  Obstacle.exclude_spike()

    Obstacle.repeat_spike()
#-------------->end of lose game<-------------------------


#/////////////////////////////////////////////////////////////////////////
#------------------------>Machine Learning part<----------------------------
    if runs == True:
        for Players in Population:
            if Players.alive == True:
                decision = Players.neuron.Foward_function(Players, Obstacle)
                Players.person_movements()
                Players.person_form(screen)
                if decision[0][0] > 0.5 and Players.in_ground:
                    Players.Jump()
                ML_hitbox = Players.hitbox()
                if ML_hitbox.colliderect(points):
                    if Players.last_score != Obstacle.cycle_of_point:
                        Players.Unique_points()
                        Players.last_score = Obstacle.cycle_of_point
                if ML_hitbox.colliderect(losing):
                    Players.player_vel_y -= 1000
                    Players.in_ground = True
                    if Players.in_ground == True:
                        Players.alive = False
                        Losers += 1
                        print(f"LOSER ML")
                    if Losers == Iterations:
                        print("MORREU TODO MUNDO GERAL")
                        timeout = True
                        death_time = pygame.time.get_ticks()
                        
    if timeout == True:
        timer_actual = pygame.time.get_ticks()
        if timer_actual - death_time >= 5000:
            print("recomeçando////////")
            timeout = False
            Losers = 0
            runs = False
    if runs == False:
        runs = True
        Players.alive = True
        Losers = 0
        Obstacle.delete()





    pygame.display.flip()
    clock.tick(144)

pygame.quit()