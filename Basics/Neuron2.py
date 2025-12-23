import numpy as np
import matplotlib.pylab as plt
import seaborn as sns


Features = np.array([[1.0, 6.0, 5.9],
                     [9.0, 1.5, 8.8], #DADOS PRINCIPAIS
                     [7.6, 5.5, 4.2]])

Target = np.array([[0.3, 0.9, 1.0],
                   [0.1, 0.7, 0.4], #DADO A SEREM ATINGIDOS VALOR = Y
                   [0.7, 1.0, 0.2]])

Matrix_of_ones = np.ones((3,1)) #Bias, PERMITE O AJUSTE DE DADOS , LHE DANDO FLEXIBILDIADE.

learning_rate = 0.01
iterations = 100000

Peso = np.random.randn(4,3) #Sinal para ajustar na saida final do sinal, de cada neurônio, O TAMANHO DEVE SER A OPOSTA DE FEATURES CONCATENADA COM BIAS(BIAS CONCATENADA COM FEATURES TAMANHO IGUAL A 3X4), PESO DEVE SER 4X3.
Features_and_ones = np.concatenate((Features, Matrix_of_ones), axis=1) #Ao juntar Bias com Features, criamos um ajuste de dados na hora de realizar a função linear.

#Soma ponderada é Z = W * X + B, tal que B=Bias, X=Features, W=Pesos.
#Nesse caso já concatenamos X+B, agora realizar W * X para garantir a Soma ponderada.



class Execução():
    def __init__(self, Features_and_ones, Peso, Target, learning_rate, iterations):
        self.Features_and_ones = Features_and_ones
        self.Peso = Peso
        self.Target = Target
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.epsilon = 1e-10
        self.cost_history = []

    
    def soma_ponderada(self):
        self.Z = self.Features_and_ones @ self.Peso #@ é a multiplicação de matrizes, de colunas para linhas e vice-versa.
        return self.Z

    def sigmoide(self, valor_Z):  #Função da sigmóide é de O(z) = 1/(1+e^-z)         
        self.sigmoide_function = 1/(1+np.exp(-np.clip(valor_Z, -500, 500)))   #np.exp(valor) pegamos o número de euler e elevamos a um valor variável
        return  self.sigmoide_function

    def funcao_de_custo(self, sigmoide_value):
        #função de custo, Entropia Cruzada Binária. Fórmula é J = (-1/m) Somatório [Y*log(A)+(1-Y)*log(1-A)] Tal que somatório=média
        self.m = len(Target)
        self.equacao = -np.mean(Target * np.log(sigmoide_value + self.epsilon) + (1- Target) * np.log(1-sigmoide_value + self.epsilon))
        return self.equacao
    def gradiente_descendente(self, sigmoide_value):
        #fórmula da derivada do gradiente descendente. dW = 1/m * X transposta * (A - Y)
        self.gradient_descendent = 1/self.m * np.transpose(self.Features_and_ones) @ (sigmoide_value - self.Target)
        return self.gradient_descendent

    def TREINAMENTO(self):
        for i in range(self.iterations):
            valor_Z = self.soma_ponderada()
            sigmoide_value = self.sigmoide(valor_Z)
            valor_de_custo = self.funcao_de_custo(sigmoide_value)
            self.cost_history.append(valor_de_custo)
            valor_do_gradiente = self.gradiente_descendente(sigmoide_value)
            New_peso = self.Peso - learning_rate * valor_do_gradiente
            self.Peso = New_peso
        return valor_de_custo, New_peso


EXECUTAR = Execução(Features_and_ones, Peso, Target, learning_rate, iterations) 
EXECUTAR.TREINAMENTO()

valores_de_custos_totais, valores_do_peso_novo = EXECUTAR.TREINAMENTO()
print(valores_de_custos_totais)
print('//////////////')
print(valores_do_peso_novo)