import numpy as np
import matplotlib as plt

Features = np.array([[1.0, 6.0, 5.9],
                     [9.0, 1.5, 8.8], #DADOS PRINCIPAIS
                     [7.6, 5.5, 4.2]])

Target = np.array([[5.0, 5.6, 9.0],
                   [1.2, 5.5, 7.2], #DADO A SEREM ATINGIDOS VALOR = Y
                   [1.2, 7.0, 8.8]])

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

    def sigmoide(self):  #Função da sigmóide é de O(z) = 1/(1+e^-z)         
        self.sigmoide_function = 1/(1+np.exp(-self.Z))   #np.exp(valor) pegamos o número de euler e elevamos a um valor variável
        return  self.sigmoide_function

    def funcao_de_custo(self):
        #função de custo, Entropia Cruzada Binária. Fórmula é J = (-1/m) Somatório [Y*log(A)+(1-Y)*log(1-A)] Tal que somatório=média
        self.m = len(Target)
        self.equacao = 1/self.m * -np.mean(Target * np.log(self.sigmoide_function + self.epsilon) + (1- Target) * np.log(1-self.sigmoide_function + self.epsilon))

    def gradiente_descendente(self):
        #fórmula da derivada do gradiente descendente. dW = 1/m * X transposta * (A - Y)
        self.gradient_descendent = 1/self.m * np.transpose(self.Features_and_ones) @ (self.sigmoide_function - self.Target)
        print(self.gradient_descendent)


    def treinamento(self):
        for i in range(self.iterations):
            self.sum_ponderada()
            self.sigmoide(self.sum_ponderada())
            print(self.sigmoide_function)

    def realizar_todas_as_funcoes(self):
        self.funcao_de_custo()
        self.gradiente_descendente()
        self.treinamento()




Execute_all = Execução(Features_and_ones, Peso, Target, learning_rate, iterations)
Execute_all.realizar_todas_as_funcoes()