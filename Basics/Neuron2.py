import numpy as np
import matplotlib.pylab as plt

Features = np.array([[1.0, 6.0, 5.9],
                     [9.0, 1.5, 8.8], #DADOS PRINCIPAIS
                     [7.6, 5.5, 4.2]])

Target = np.array([[0.3, 0.9, 1.0],
                   [0.1, 0.7, 0.4], #DADO A SEREM ATINGIDOS VALOR = Y
                   [0.7, 1.0, 0.2]])

Matrix_of_ones = np.ones((3,1)) #Bias, PERMITE O AJUSTE DE DADOS , LHE DANDO FLEXIBILDIADE.

learning_rate = 0.01
iterations = 100000

# Peso = np.random.randn(4,3) #Sinal para ajustar na saida final do sinal, de cada neurônio, O TAMANHO DEVE SER A OPOSTA DE FEATURES CONCATENADA COM BIAS(BIAS CONCATENADA COM FEATURES TAMANHO IGUAL A 3X4), PESO DEVE SER 4X3.
Features_and_ones = np.concatenate((Features, Matrix_of_ones), axis=1) #Ao juntar Bias com Features, criamos um ajuste de dados na hora de realizar a função linear.

#Soma ponderada é Z = W * X + B, tal que B=Bias, X=Features, W=Pesos.
#Nesse caso já concatenamos X+B, agora realizar W * X para garantir a Soma ponderada.



class Execução():
    def __init__(self, Features_and_ones, Target, learning_rate, iterations):
        self.Features_and_ones = Features_and_ones
        self.Target = Target
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.epsilon = 1e-10
        self.cost_history = []
        self.matiz_de_um = np.ones((3,1))

        self.W1 = np.random.randn(4,2) #Novos pesos W1 e W2
        self.W2 = np.random.randn(3,3)

    
    #def soma_ponderada(self):
       # Z = Features_and_ones @ self.Peso #@ é a multiplicação de matrizes, de colunas para linhas e vice-versa.
        #return Z

    def sigmoide(self, valor_Z):  #Função da sigmóide é de O(z) = 1/(1+e^-z)         
        sigmoide_function = 1/(1+np.exp(-np.clip(valor_Z, -500, 500)))   #np.exp(valor) pegamos o número de euler e elevamos a um valor variável
        return  sigmoide_function

    def foward_function(self, W1, W2):
        #A fórmula do foward function é denotada por: A2 = sigmoide de (concatenar com(sigmodie de(X * W1) * W2))  
        Z1 = self.Features_and_ones @ W1 #Multiplicamos a entrada dos dados já com o bias embutido com o W1 Nota Z1 = soma ponderada número 1
        A1 = self.sigmoide(Z1) #A1 = ativação número 1 com base no valor de Z1 que obtemos, colocando Z1 na sigmoide
        A1_with_bias = np.concatenate((A1, self.matiz_de_um), axis=1) #concatenando com os bias intermediário junto com A1, agora temos a ativação com bias

        Z2 = A1_with_bias @ W2 #Multiplicamos os valores de ativação número 1 com o W2, criando assim uma nova entrada de dados denominada de Z2
        A2 = self.sigmoide(Z2) #A2 = ativação número 2. *Nota, não é necessário o bias*
        return A2, A1_with_bias, A1

    def backward_function(self, A2, A1):
        #Cálculo do delta de saída é dado pela fórmula: S= sigma  S2 = (A2 - Y) * (A2 * (1 - A2))
        delta_saida2 = (A2 - self.Target) * (A2 * (1 - A2))

        delta_saida1 = delta_saida2 @ self.W2[:-1,:].T * (A1 * (1 - A1))
        return delta_saida1, delta_saida2

    def funcao_de_custo(self, A2):
        #função de custo, Entropia Cruzada Binária. Fórmula é J = (-1/m) Somatório [Y*log(A)+(1-Y)*log(1-A)] Tal que somatório=média
        #Com as hidden layers fazemos o seguinte, a fórmula que temos agora é J = (-1/m) somatório de [Y*Log(A2)+(1-Y)*Log(A2)]
        self.m = len(Target)
        self.equacao = -np.mean(Target * np.log(A2 + self.epsilon) + (1 - self.Target) * np.log(1 - A2 + self.epsilon))
        return self.equacao


    def gradiente_descendente(self, delta_saida1, delta_saida2, A1_with_bias):
        #fórmula da derivada do gradiente descendente. dW = 1/m * X transposta * (A - Y)
        #Para as hidden layers alteramos um aspecto, no lugar de X e (A - Y) usamos os novos valores de A1 com bias embutido no lugar de X e a saida de delta no lugar de (A-Y)
        gradient_descendent_W2 = 1/self.m * np.transpose(A1_with_bias) @ (delta_saida2) #Gradiente para pponte final de W2
        gradient_descendent_W1 = 1/self.m * np.transpose(self.Features_and_ones) @ (delta_saida1)# Gradiente para a primeira ponte de W1
        return gradient_descendent_W1, gradient_descendent_W2


    def new_weights(self, valor_do_gradiente1, valor_do_gradiente2):
        self.W1 -= learning_rate * valor_do_gradiente1
        self.W2 -= learning_rate * valor_do_gradiente2


    def TREINAMENTO(self):
        for i in range(self.iterations):
            A2, a1_with_bias, A1 = self.foward_function(self.W1, self.W2)
            valor_de_custo = self.funcao_de_custo(A2)
            self.cost_history.append(valor_de_custo)
            backward_result1, backward_result2 = self.backward_function(A2, A1)
            valor_do_gradiente1, valor_do_gradiente2 = self.gradiente_descendente(backward_result1, backward_result2, a1_with_bias)
            new_weights = self.new_weights(valor_do_gradiente1, valor_do_gradiente2)
            New_peso = valor_do_gradiente1, valor_do_gradiente2
        return self.cost_history, New_peso


EXECUTAR = Execução(Features_and_ones, Target, learning_rate, iterations)
valores_de_custos_totais, valores_do_peso_novo = EXECUTAR.TREINAMENTO()
gradiente_W1, gradiente_W2 = valores_do_peso_novo
New_target = Target.flatten()
print(gradiente_W1.flatten())


#W1 e W2. W1 é um conjunto de pesos que são misturados com os dados de entradas, modificando-os e transformando em 2 neurônios ocultos
#extraindo os mais diversos padrôes. W2 é a resposta da camada oculta, que é levada para os nosso neurônios de saída
#tal que obtemos uma saída dependente de W1.

#Parte Gráfica
fig, axes = plt.subplots(1,2, figsize=(12,5), layout='constrained')
plt.grid(True)
axes[0].set_title("Gráfico do Custo")
axes[1].set_title("Gráfico do Gradiente")

axes[0].plot(valores_de_custos_totais)


axes[1].scatter(range(len(New_target)),New_target, color='red', alpha=0.7, label='Dados Originais')

plt.show()