import numpy as np
import pygame
import Objects
class Neuro:
    def __init__(self,input_size=5, hidden_size=6, output_size=1):
        self.weights_input_hidden = np.random.uniform(-1, 1, (input_size, hidden_size)) #W = weights
        self.weights_hidden_output = np.random.uniform(-1, 1, (hidden_size, output_size)) #W = Weights

        self.bias_hidden = np.random.uniform(-1, 1, (1, hidden_size)) #B = Bias
        self.bias_output = np.random.uniform(-1, 1, (1, output_size)) #B = Bias
        self.matrix_of_ones = np.ones((1,1))

    def Features(self, Player, Obstacle):
        hitbox_player = Player.hitbox() #serve para distância alémd e hitbox.
        hitbox_obstacle = Obstacle.spike_hitbox() #vai servir para distância?

        distanceX_ML = (hitbox_obstacle.x - hitbox_player.x) / 1280 ################
        positionY_ML = hitbox_player.y / 720
        distanceY_ML_object = (hitbox_obstacle.y - hitbox_player.y) / 720

        player_height = hitbox_player.height / 100
        objectvelocity = -8 /20

        features = np.array([distanceX_ML, positionY_ML, player_height, objectvelocity, distanceY_ML_object]).reshape(1,5) #X = features
        features_tranformed = np.concatenate((features, self.matrix_of_ones), axis=1)
        print(features_tranformed)


