#Revisão dos Loop's presentes no modelo de Bass
"""Loop de Balanceamento do diagrama de Bass

Um loop de balanceamento, também conhecido como loop de feedback negativo,
é um conceito fundamental na modelagem de sistemas dinâmicos. Ele descreve uma 
situação em que uma mudança em uma variável do sistema leva a uma resposta que tende a restaurar 
o sistema ao seu estado original.

Em termos mais técnicos, um loop de balanceamento é uma sequência fechada de relações causais 
(ou seja, A afeta B, B afeta C, e assim por diante) que eventualmente retorna à variável original 
de uma maneira que se opõe à mudança inicial. Isso significa que se a variável original aumentar,
o efeito do loop será uma diminuição dessa variável, e vice-versa.

Os loops de balanceamento são uma parte essencial de muitos sistemas naturais e artificiais, 
ajudando a manter a estabilidade em face de perturbações. Eles são um dos principais mecanismos p
elos quais os sistemas se auto-regulam.

Os loops de balanceamento são resposáveis por auto regular o sistema. No caso do modelo de Bass,
os loops de balanceamento são responsáveis por regular a quantidade de clientes que entram e saem
do restaurante. Por exemplo 
"""


"""Loop de Reforço do diagrama de Bass

Um loop de reforço, também conhecido como loop de feedback positivo, é um conceito chave na modelagem 
de sistemas dinâmicos. Ele descreve uma situação em que uma mudança em uma variável do sistema leva a 
uma resposta que amplifica a mudança original.

Em termos mais técnicos, um loop de reforço é uma sequência fechada de relações causais
(ou seja, A afeta B, B afeta C, e assim por diante) que eventualmente retorna à variável original 
de uma maneira que reforça a mudança inicial. Isso significa que se a variável original aumentar, 
o efeito do loop será um aumento adicional dessa variável, e vice-versa.

Os loops de reforço são uma parte essencial de muitos sistemas naturais e artificiais, impulsionando o crescimento, 
a mudança e a evolução. Eles são um dos principais mecanismos pelos quais os sistemas se desenvolvem e se transformam 
ao longo do tempo. No entanto, eles também podem levar a instabilidades se não forem equilibrados por loops de balanceamento adequados.

Os loops de reforço são responsáveis por regular o crescimento do sistema. No caso do modelo de Bass,
os loops de reforço são responsáveis por regular a quantidade de clientes que entram e saem
do restaurante. Por exemplo, se o restaurante está muito cheio, os clientes que estão no restaurante
começam a sair, diminuindo a quantidade de clientes no restaurante. Isso faz com que o restaurante
fique mais vazio, fazendo com que mais clientes entrem no restaurante, aumentando a quantidade de clientes
no restaurante. Por exemplo

"""

"Questão 1"
"""
A seguir, associe R para loop de reforço e B para loop de balanceamento associado aos loops mostrados como letras 
vermelhas no diagrama causal do modelo.

A: [A] -> R
B: [B] -> B
C: [C] -> R 
D: [D] -> B 

Associe uma polaridade positiva (usando o a letra p) ou uma polaridade negativa (usando a letra n) à relação 
mostrada na figura como letra E. Essa é a relação da População Sapiens com a Taxa de Mortes Neandertal.

E: [E] -> p
 
Há outros loops ocultos na figura. Um deles é o que vai da População Sapiens para o Fluxo de Mortes Neandertais, 
daí para a População Neandertal, para o Fluxo de Mortes Sapiens e retorna à População Sapiens. Indique se esse é 
um loop de reforço (R) ou de balanceamento (B).

F: [F] -> R
"""
"Questão 2"
#A questão foi uma questão toda teórica e com imagens , não vale a pena a tentativa de inserir o resultados aqui
#Em suma, tinha que se ter o conhecimnento dos conceitos de loops de reforço e balanceamento para responder a questão

"Questão 3"

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Determinação das constantes
A0 = 76800000
TA = 851000000
tc = 15
fp = 0.0063 + 0.065
P0 = 214000000
k = 0.007

# Definição do sistema de equações diferenciais
def SisEqDif(Y,t):
 A = Y[0]
 P = Y[1]
 dAdt = (TA - A) / tc - fp * A
 dPdt = k * P
 return[dAdt,dPdt]

# Definição do intervalo de tempo
T=np.arange(0,100,1e-4)

# Definindo as condições iniciais
Y0=[A0,P0]

# Rodando o odeint
Y=odeint(SisEqDif,Y0,T)

# Fazendo o gráfico das soluções
plt.plot(T,Y[:,0],'g',label='Área Cultivada (A)')
plt.plot(T,Y[:,1],'r',label='População (P)')
plt.axis([0, max(T), 0, max(Y[0])])
plt.ylabel('População')
plt.xlabel('Tempo (anos)')
plt.title(r'Modelo de Segurança Alimentar')
plt.legend(labelspacing=0.8)
plt.show()

# População prevista para daqui a 100 anos (em milhões)
populacao = round(Y[-1,1] / 1000000)
print(populacao)

# Alimento disponível daqui a 100 anos (em milhões de toneladas)
ADisp=3.8*Y[-1,0]/1000000
alimento_disponivel = round(ADisp)
print(alimento_disponivel)

# Consumo per capita em toneladas por pessoa por ano
consumo_per_capita = 0.8

# Alimento necessário daqui a 100 anos (em milhões de toneladas)
ANesc=0.8*Y[-1,1]/1000000
alimento_necessario = round(ANesc)
print(alimento_necessario)

# Índice de segurança alimentar
indice_seguranca_alimentar = round(alimento_disponivel / alimento_necessario, 2)
print(indice_seguranca_alimentar)

# Quantidade máxima de pessoas que o Brasil poderá alimentar (em milhões)
max_populacao_alimentada = round((ADisp/ANesc)*Y[-1,1]/(0.8*1000000)
)
print(max_populacao_alimentada)
