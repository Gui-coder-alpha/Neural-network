import numpy as np
import matplotlib.pyplot as plt

#Evolução/Neuroevolution
#A evolução nas redes neurais, semelhante à teoria de evolução
#de Darwin, criamos diversos indivíduos, o qual cada um vai apresentar
#um peso divergente entre si, todos aleatórios. Dependendo da sua eficácia
#selecionamos um número x de redes neurais, e passamos os seus pesos para
#uma nova geração, tal que aplicamos um mudança pequena nos pesos de forma
#aleatória. Diante disso, criamos diversas gerações com o intuito de
#selecionar o que apresenta melhores resultados.

Features = np.array([[1.0, 6.0, 5.9],
                     [9.0, 1.5, 8.8],
                     [7.6, 5.5, 4.2]])

Target = np.array([[0.3, 0.9, 1.0],
                   [0.1, 0.7, 0.4],
                   [0.7, 1.0, 0.2]])

Matrix_of_ones = np.ones((3,1))

learning_rate = 0.01
iterations = 100000


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
        self.matiz_de_um1 = np.ones((3,1))
        def soma_ponderada(self):
        Z = Features_and_ones @ self.Peso #@ é a multiplicação de matrizes, de colunas para linhas e vice-versa.
        return Z

    def sigmoide(self, valor_Z):  #Função da sigmóide é de O(z) = 1/(1+e^-z)         
        sigmoide_function = 1/(1+np.exp(-np.clip(valor_Z, -500, 500))) 
        return  sigmoide_function
    
    def originals_weights(self):
        self.W1_father = np.random.randn(4,2)
        self.W2_father = np.random.randn(3,3)
        return self.W1, self.W2
    
    def mutacao(self, father_weights, minimal_rate=0.01):
        self.W1_son = father_weights + np.random.rand(4,2) * minimal_rate
        self.W2_son = father_weights + np.random.rand(3,3) * minimal_rate


    def foward_function(self, W1, W2):
        #A fórmula do foward function é denotada por: A2 = sigmoide de (concatenar com(sigmodie de(X * W1) * W2))  
        Z1 = self.Features_and_ones @ W1
        A1 = self.sigmoide(Z1)
        A1_with_bias = np.concatenate((A1, self.matiz_de_um), axis=1)

        Z2 = A1_with_bias @ W2 
        A2 = self.sigmoide(Z2)
        return A2, A1_with_bias, A1

    def funcao_de_aptidao(self, A2):
        #função de aptidao, Entropia Cruzada Binária. Fórmula é J = (-1/m) Somatório [Y*log(A)+(1-Y)*log(1-A)] Tal que somatório=média
        #Com as hidden layers fazemos o seguinte, a fórmula que temos agora é J = (-1/m) somatório de [Y*Log(A2)+(1-Y)*Log(A2)]
        self.m = len(Target)
        self.equacao = -np.mean(Target * np.log(A2 + self.epsilon) + (1 - self.Target) * np.log(1 - A2 + self.epsilon))
        return self.equacao

    def TREINAMENTO(self):
        for i in range(self.iterations):


EXECUTAR = Execução(Features_and_ones, Target, learning_rate, iterations)
valores_de_custos_totais, valores_do_peso_novo = EXECUTAR.TREINAMENTO()
gradiente_W1, gradiente_W2 = valores_do_peso_novo

#Parte Gráfica
fig, axes = plt.subplots(1,2, figsize=(12,5), layout='constrained')
axes[0].grid(True)
axes[1].grid(True)

axes[0].set_title("Gráfico do Custo")
axes[1].set_title("Gráfico do Gradiente")

axes[0].plot(valores_de_custos_totais)
axes[0].set_ylabel('Valor do erro')
axes[0].set_xlabel('Iterações')

axes[1].plot(gradiente_W1, color='blue', label='Gradiente W1', linewidth=2)
axes[1].plot(gradiente_W2, color='green', label='Gradiente W2', linewidth=2)
axes[1].set_ylabel('Magnitude do Gradiente')
axes[1].set_xlabel('Iterações')

plt.legend()
plt.show()