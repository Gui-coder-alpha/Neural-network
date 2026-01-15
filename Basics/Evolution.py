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
    def __init__(self, Target, W1=None, W2=None):
        self.Target = Target
        self.matiz_de_um1 = np.ones((3,1))

        if W1 is not None and W2 is not None:
            self.W1 = W1
            self.W2 = W2
        else:
            self.W1 = np.random.randn(4, 2)
            self.W2 = np.random.randn(3, 3) 
    
    def soma_ponderada(self):
        Z = Features_and_ones @ self.Peso #@ é a multiplicação de matrizes, de colunas para linhas e vice-versa.
        return Z

    def sigmoide(self, valor_Z):  #Função da sigmóide é de O(z) = 1/(1+e^-z)         
        sigmoide_function = 1/(1+np.exp(-np.clip(valor_Z, -500, 500))) 
        return  sigmoide_function
    
    def mutacao(self, minimal_rate=0.01): #Filhos
        self.W1 += np.random.rand(4,2) * minimal_rate
        self.W2 += np.random.rand(3,3) * minimal_rate
        return self.W1, self.W2


    def foward_function(self, matrix):
        #A fórmula do foward function é denotada por: A2 = sigmoide de (concatenar com(sigmodie de(X * W1) * W2))  
        Z1 = matrix @ self.W1
        A1 = self.sigmoide(Z1)
        A1_with_bias = np.concatenate((A1, self.matiz_de_um1), axis=1)

        Z2 = A1_with_bias @ self.W2 
        A2 = self.sigmoide(Z2)
        return A2
    

    def funcao_de_aptidao(self, saida):
        #função de aptidao, ou de custo, Mean Squared Error(MSE), vai ser utilizado
        #Dado a fórmula: 1/n somatório de (Target - Saída)² ou 1/n somatório de (Y - A2)
        #Aqui o cálculo de custo se torna cálculo de aptidão, o qual selecionamos o melhor
        self.equacao = np.mean(np.square(self.Target - saida)) #saida = A2
        return self.equacao
    

#Não temos a função de treinamento, vamos ter um loop por parte de fora para realizar toda a operação
#Tal que, ao colocar tudo dentro da classe vamos gerenciar inúmeros dados de uma vez só, sendo não só 1
#mas 99 ou mais ao lado, ou seja iriámos ter diversas redes na mesma classe, se tornando um código
#espaguete.


Populacao = [Execução(Target) for _ in range(100)] #Realizamos a função em 100 vezes, o qual são os nossos indivíduos
#Vale ressaltar que, a _ é uma variável descartável

Erro_da_geração = [] #Armazenamaos todas as redes aqui, o qual apenas a melhor se qualifica, demonstrando a evolução da rede neural
geracao = 1000 #Vamos até a geração 1000, ou seja 1000 repetições


for rede in range(geracao): #Aqui chamamos a classe, realizando as operações num loop, ao invés de dentro da própria classe
    custos = [] 
    for individuo in Populacao: #Basicamente o cálculo de custo/aptidão do tipo MSE
        saida = individuo.foward_function(Features_and_ones)
        erro = individuo.funcao_de_aptidao(saida) #saida = A2
        custos.append(erro)
    
    Resultados_filtrados = np.argmin(custos) #Usamos o np.argmin, para selecionar a rede que apresenta o resultado com valores baixos.
    Melhor_individuo = Populacao[Resultados_filtrados] #Pegamos o melhor indivíduo
    Erro_da_geração.append(custos[Resultados_filtrados]) #Colocamos no erro da geração
    
    nova_geracao = [] #Nova geração deve aparecer

    vencedor =Execução(Target, np.copy(Melhor_individuo.W1), np.copy(Melhor_individuo.W2)) 
    nova_geracao.append(vencedor)

    for _ in range(100 - 1):
        clone = Execução(Target, np.copy(Melhor_individuo.W1), np.copy(Melhor_individuo.W2)) #Os pesos são passados adiante, sendo herdado da melhor rede
        clone.mutacao(0.01) #Mutação na nova geração para melhorar os resultados
        nova_geracao.append(clone)

    if rede % 5 == 0: #Imprime a cada 100 gerações
        plt.clf() # Limpa o gráfico anterior
        plt.plot(Erro_da_geração)
        plt.pause(0.01) # Pausa curta para o gráfico atualizar
    
    Populacao = nova_geracao

#Parte Gráfica
fig, axes = plt.subplots(1,2, figsize=(12,5), layout='constrained')
axes[0].grid(True)
axes[0].set_title("Gráfico do Custo")
axes[0].plot(Erro_da_geração)
axes[0].set_ylabel('Valor do erro')
axes[0].set_xlabel('Iterações')

plt.legend()
plt.show()
