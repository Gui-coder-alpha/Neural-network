import numpy as np
import matplotlib.pyplot as plt

features = np.array([1.6, 2.3, 7.8, 1.2, 5.9, 9.0, 1.2, 5.7, 8.9, 9.1])
target = np.array([0, 0, 1, 1, 1, 0, 0, 1, 0, 1]) 
features_designX = features[:,np.newaxis]  
target_designY = target[:,np.newaxis]
matrix_of_ones = np.ones((10,1))
concatenationX = np.concatenate((features_designX, matrix_of_ones), axis=1)

learning_rate = 0.01
iterations = 100

class Optmization():
    def __init__(self, target_designY, concatenationX, learning_rate,iterations):
        self.target_designY = target_designY 
        self.concatenationX = concatenationX 
        self.learning_rate = learning_rate
        self.iterations = iterations 
        self.beta_value = np.zeros((self.concatenationX.shape[1], 1))
        self.cost_history = []
        self.epsilon = 1e-10

    def function_sigmoid(self, sum_ponderada_Z):
        sigmoid = 1/(1 + np.exp(-sum_ponderada_Z))
        return sigmoid

    def Binary_cost_function(self, sigmoid_result_or_pred_y):
        self.sigmoid_result_or_pred_y = sigmoid_result_or_pred_y
        y_multply_log_of_ywithhat = self.target_designY * np.log(self.sigmoid_result_or_pred_y + self.epsilon)
        one_minus_y = 1 - self.target_designY
        log_of_1_minus_ywithhat = np.log(1 - self.sigmoid_result_or_pred_y + self.epsilon)
        cost_total = np.mean(-(y_multply_log_of_ywithhat + one_minus_y * log_of_1_minus_ywithhat))
        return cost_total
    
    def gradient_descent(self, sigmoid_result_or_pred_y):
        concatenationX_transpose = self.concatenationX.transpose()
        gradient = (1/len(self.target_designY)) * concatenationX_transpose @ (sigmoid_result_or_pred_y - self.target_designY)
        return gradient

    def trainement(self):
        for i in range(self.iterations):
            sum_ponderada_Z = self.concatenationX @ self.beta_value
            sigmoid_result_or_pred_y = self.function_sigmoid(sum_ponderada_Z)
            current_cost = self.Binary_cost_function(sigmoid_result_or_pred_y)
            self.cost_history.append(current_cost)
            new_beta_value = self.beta_value - learning_rate * self.gradient_descent(sigmoid_result_or_pred_y)
            self.beta_value = new_beta_value
        return self.beta_value, self.cost_history

model = Optmization(concatenationX=concatenationX, target_designY=target_designY, learning_rate=learning_rate, iterations=iterations)
final_beta_values, cost_history_results = model.trainement()
print(final_beta_values)
print(cost_history_results)