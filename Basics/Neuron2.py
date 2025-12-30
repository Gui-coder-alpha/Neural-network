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
iterations = 100

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
        self.matiz_de_um = np.ones((3,1))

        self.W1 = np.random.randn(4,2) #Novos pesos W1 e W2
        self.W2 = np.random.randn(3,3)

    
    def soma_ponderada(self):
        self.Z = self.Features_and_ones @ self.Peso #@ é a multiplicação de matrizes, de colunas para linhas e vice-versa.
        return self.Z

    def sigmoide(self, valor_Z):  #Função da sigmóide é de O(z) = 1/(1+e^-z)         
        self.sigmoide_function = 1/(1+np.exp(-np.clip(valor_Z, -500, 500)))   #np.exp(valor) pegamos o número de euler e elevamos a um valor variável
        return  self.sigmoide_function

    def foward_function(self):
        self.Z1 = self.Features_and_ones @ self.W1 #Multiplicamos a entrada dos dados já com o bias embutido com o W1 Nota Z1 = soma ponderada número 1
        self.A1 = self.sigmoide(self.Z1) #A1 = ativação número 1 com base no valor de Z1 que obtemos, colocando Z1 na sigmoide
        self.A1_with_bias = np.concatenate((self.A1, self.matiz_de_um), axis=1) #concatenando com os bias intermediário junto com A1, agora temos a ativação com bias

        self.Z2 = self.A1_with_bias @ self.W2 #Multiplicamos os valores de ativação número 1 com o W2, criando assim uma nova entrada de dados denominada de Z2
        self.A2 = self.sigmoide(self.Z2) #A2 = ativação número 2
        print(self.A2)



    def funcao_de_custo(self, sigmoide_value):
        #função de custo, Entropia Cruzada Binária. Fórmula é J = (-1/m) Somatório [Y*log(A)+(1-Y)*log(1-A)] Tal que somatório=média
        self.m = len(Target)
        self.equacao = -np.mean(Target * np.log(sigmoide_value + self.epsilon) + (1- Target) * np.log(1-sigmoide_value + self.epsilon))
        return self.equacao
    

    def gradiente_descendente(self, sigmoide_value):
        #fórmula da derivada do gradiente descendente. dW = 1/m * X transposta * (A - Y)
        self.gradient_descendent = 1/self.m * np.transpose(self.Features_and_ones) @ (sigmoide_value - self.Target)
        return self.gradient_descendent

    def ativar_funcao(self):
        self.foward_function()
        self.funcao_de_custo(self.sigmoide_function)
        self.gradiente_descendente(self.sigmoide_function)


    #def TREINAMENTO(self):
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
EXECUTAR.ativar_funcao()

valores_de_custos_totais, valores_do_peso_novo = EXECUTAR.TREINAMENTO()
print("///////////////////////////////////")


#W1 e W2. W1 é um conjunto de pesos que são misturados com os dados de entradas, modificando-os e transformando em 2 neurônios ocultos
#extraindo os mais diversos padrôes. W2 é a resposta da camada oculta, que é levada para os nosso neurônios de saída
#tal que obtemos uma saída dependente de W1.