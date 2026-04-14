import pygame
import Ambient
import Player_fundamentals
import Objects
import MachineLearning
import numpy as np
import Graphic

pygame.init()
screen = pygame.display.set_mode((1280, 720), display=1)
clock = pygame.time.Clock()
running = True

#---------FUNCTIONS-----------------
Obstacle = Objects.Blocks()
Graph = Graphic

Iterations = 200

Population = []
for _ in range(Iterations):
    ML = MachineLearning.Neuro()
    Players = Player_fundamentals.Player(screen, ML)
    Players.neuron = ML
    Population.append(Players)

Losers = 0
timeout = False
runs = True

Final_points = []
Gen_count = 0
Gen_list = []
update = False

while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False

    
#-------> Ambient/Background <-------
    Ambient.base_floor(screen)
#--------------> End <---------------
#///////////////////////////////////////////////////////////
#--------------> Obstacle/Objects <---------------
    points = Obstacle.hitbox_point()
    Obstacle.spikes(screen)
    losing = Obstacle.spike_hitboxes()
    Obstacle.spike_velocity()
    Obstacle.repeat_spike()
    hitbox_jump = Obstacle.orb_jump()
    wall = Obstacle.big_wall()

    keys = pygame.key.get_pressed()
    Obstacle.gen(screen)

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

#-------------->end of lose game<-------------------------
    best_player = None
    best_score = -1

#/////////////////////////////////////////////////////////////////////////
#------------------------>Machine Learning part<----------------------------
    for Players in Population:
        if Players.alive == True:
            if Players.score > best_score:
                best_score = Players.score
                best_player = Players
            decision, test = Players.neuron.Foward_function(Players, Obstacle)
            Players.person_movements()
            Players.person_form(screen)
            if decision[0][0] > 0.5 and Players.in_ground:
                Players.Jump()
            ML_hitbox = Players.hitbox()
            if ML_hitbox.colliderect(hitbox_jump) and Obstacle.orb_activate:
                Players.gravity = 0.45
            if Players.in_ground:
                Players.gravity = 0.98
            if ML_hitbox.colliderect(wall):
                Players.gravity = 0.98
            if ML_hitbox.colliderect(points):
                if Players.last_score != Obstacle.cycle_of_point:
                    Players.Unique_points()
                    Players.last_score = Obstacle.cycle_of_point
            

            if ML_hitbox.colliderect(losing):
                Players.player_vel_y -= 1000
                Losers += 1
                Players.alive = False
                if Losers == Iterations:
                    all_points = np.array([Players.score for Players in Population])
                    Best_index = np.argmax(all_points)
                    Father_player = Population[Best_index]
                    
                    best_bias_hidden = np.copy(Father_player.neuron.bias_hidden)
                    best_weights_hidden = np.copy(Father_player.neuron.weights_input_hidden)
                    best_bias_output = np.copy(Father_player.neuron.bias_output)
                    best_weights_output = np.copy(Father_player.neuron.weights_hidden_output)

                    Objects.Exponencial_value = 7.2
                    
                    death_time = pygame.time.get_ticks()
                    timeout = True

    if best_player != None:
        Ambient.Neural_Hud(screen, best_player, Obstacle)

    if timeout == True:
        Obstacle.text_change()
        timer_actual = pygame.time.get_ticks()
        Obstacle.pause()

        if not update:
            Gen_count += 1
            best_unique_points = Father_player.score
            Final_points.append(best_unique_points)
            Gen_list.append(Gen_count)
            Graph.plot_the_graph(Final_points, Gen_list)
            update = True

        if timer_actual - death_time >= 3000:
            Obstacle.normal_text()
            update = False
            timeout = False
            Obstacle.gen_plus()
            Losers = 0
            for i, p in enumerate(Population):
                p.neuron.weights_input_hidden = np.copy(best_weights_hidden)    
                p.neuron.weights_hidden_output = np.copy(best_weights_output)
                p.neuron.bias_hidden = np.copy(best_bias_hidden)
                p.neuron.bias_output = np.copy(best_bias_output)

                p.alive = True
                p.score = 0
                p.last_score = -1
                p.player_pos = pygame.Vector2(250, 400)
                p.player_vel_y = 0
                if i > 0:
                    p.neuron.Mutation()

    if Obstacle.Exponencial_value >= 24:
        Obstacle.sum = 0

    

    pygame.display.flip()
    clock.tick(144)

pygame.quit()