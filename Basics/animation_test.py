import numpy as np
import matplotlib.pylab as plt

# Ativa o modo interativo para permitir animação
plt.ion()

Features = np.array([[1.0, 6.0, 5.9],
                     [9.0, 1.5, 8.8],
                     [7.6, 5.5, 4.2]])

Target = np.array([[0.3, 0.9, 1.0],
                   [0.1, 0.7, 0.4],
                   [0.7, 1.0, 0.2]])

Matrix_of_ones = np.ones((3,1))
learning_rate = 0.01
iterations = 100000 # Diminuí para teste rápido, pode voltar para 1.000.000
Features_and_ones = np.concatenate((Features, Matrix_of_ones), axis=1)

class Execução():
    def __init__(self, Features_and_ones, Target, learning_rate, iterations):
        self.Features_and_ones = Features_and_ones
        self.Target = Target
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.epsilon = 1e-10
        self.cost_history = []
        self.gradient_W1_history = []
        self.gradient_W2_history = []
        self.matiz_de_um = np.ones((3,1))
        self.W1 = np.random.randn(4,2)
        self.W2 = np.random.randn(3,3)
        self.m = len(Target)

    def sigmoide(self, valor_Z):         
        return 1/(1+np.exp(-np.clip(valor_Z, -500, 500)))

    def foward_function(self, W1, W2):
        Z1 = self.Features_and_ones @ W1
        A1 = self.sigmoide(Z1)
        A1_with_bias = np.concatenate((A1, self.matiz_de_um), axis=1)
        Z2 = A1_with_bias @ W2
        A2 = self.sigmoide(Z2)
        return A2, A1_with_bias, A1

    def backward_function(self, A2, A1):
        delta_saida2 = (A2 - self.Target) * (A2 * (1 - A2))
        delta_saida1 = delta_saida2 @ self.W2[:-1,:].T * (A1 * (1 - A1))
        return delta_saida1, delta_saida2

    def funcao_de_custo(self, A2):
        return -np.mean(self.Target * np.log(A2 + self.epsilon) + (1 - self.Target) * np.log(1 - A2 + self.epsilon))

    def gradiente_descendente(self, delta_saida1, delta_saida2, A1_with_bias):
        gW2 = 1/self.m * np.transpose(A1_with_bias) @ (delta_saida2)
        gW1 = 1/self.m * np.transpose(self.Features_and_ones) @ (delta_saida1)
        return gW1, gW2

    def new_weights(self, v1, v2):
        self.W1 -= self.learning_rate * v1
        self.W2 -= self.learning_rate * v2

    def TREINAMENTO(self):
        # --- PREPARAÇÃO DO GRÁFICO (ANTES DO LOOP) ---
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        line_cost, = axes[0].plot([], [], color='red')
        line_w1, = axes[1].plot([], [], color='blue', label='Gradiente W1')
        line_w2, = axes[1].plot([], [], color='green', label='Gradiente W2')
        
        axes[0].set_title("Custo em Tempo Real")
        axes[1].set_title("Gradientes em Tempo Real")
        axes[1].legend()
        axes[0].grid(True)
        axes[1].grid(True)

        # --- LOOP DE TREINAMENTO ---
        for i in range(self.iterations):
            A2, a1_with_bias, A1 = self.foward_function(self.W1, self.W2)
            valor_de_custo = self.funcao_de_custo(A2)
            self.cost_history.append(valor_de_custo)
            
            b1, b2 = self.backward_function(A2, A1)
            g1, g2 = self.gradiente_descendente(b1, b2, a1_with_bias)
            
            self.gradient_W1_history.append(np.mean(np.abs(g1)))
            self.gradient_W2_history.append(np.mean(np.abs(g2)))
            
            self.new_weights(g1, g2)

            # --- ATUALIZAÇÃO DO GRÁFICO (DENTRO DO LOOP) ---
            if i % 500 == 0: # Atualiza a cada 200 iterações
                line_cost.set_data(range(len(self.cost_history)), self.cost_history)
                line_w1.set_data(range(len(self.gradient_W1_history)), self.gradient_W1_history)
                line_w2.set_data(range(len(self.gradient_W2_history)), self.gradient_W2_history)
                
                for ax in axes:
                    ax.relim()        
                    ax.autoscale_view()
                
                plt.pause(0.001) # Força o desenho na tela

        plt.ioff() # Desativa modo interativo
        plt.show() # Mantém a janela aberta ao fim
        return self.cost_history, (self.gradient_W1_history, self.gradient_W2_history)

# Execução
EXECUTAR = Execução(Features_and_ones, Target, learning_rate, iterations)
valores_de_custos_totais, valores_do_peso_novo = EXECUTAR.TREINAMENTO()