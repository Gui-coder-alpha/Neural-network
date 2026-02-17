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
        hitbox_obstacle = Obstacle.spike_hitbox() #vai servir para distância? Sim serviu

        distanceX_ML = (hitbox_obstacle.x - hitbox_player.x) / 1280 
        positionY_ML = hitbox_player.y / 720
        distanceY_ML_object = (hitbox_obstacle.y - hitbox_player.y) / 720

        player_height = hitbox_player.height / 100
        objectvelocity = -8 /20

        features = np.array([distanceX_ML, positionY_ML, player_height, objectvelocity, distanceY_ML_object]).reshape(1,5) #X = features
        features_tranformed = np.concatenate((features, self.matrix_of_ones), axis=1) #Dados principais
        print(features_tranformed)
        return features_tranformed

    def sum_Z(self, features_transformed, Pesos, bias):
        Z_value = (features_transformed @ Pesos) + bias
        return Z_value

    def Sigmoid_result(self, Z_value):
        sigmoid_function = 1/(1 - np.exp(- np.clip(Z_value, -500, 500)))
        return sigmoid_function
    
    def Foward_function(self):
        Hidden_Layer_Z = self.sum_Z(self.Features(), self.weights_input_hidden, self.bias_hidden)
        Hidden_Layer_results = self.Sigmoid_result(Hidden_Layer_Z)

        Output_layer_Z = self.sum_Z(Hidden_Layer_results, self.weights_hidden_output, self.bias_output)
        Output_layer_results = self.Sigmoid_result(Output_layer_Z)
        return Output_layer_results

    def Mutation(self):
        self.weights_hidden_output += * 0,01