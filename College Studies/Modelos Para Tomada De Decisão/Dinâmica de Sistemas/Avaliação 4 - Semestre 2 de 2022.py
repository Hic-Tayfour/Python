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
"Questão 1 Parte A"
#Classifique cada um dos loops (ciclos) descritos a seguir como sendo de reforço (escreva R) ou de balanceamento (escreva B).
#1. População na cidade -> Fluxo de população evacuada -> População na cidade: [L1]
#2. População na zona de descontaminação -> Fluxo de militares e profissionais de saúde -> População na zona de descontaminação: [L2]
#3. População na zona de descontaminação -> Fluxo de população descontaminada -> População na zonade descontaminação: [L3]

#Resposta: L1 = Balanceamento, L2 = Balanaceamento, L3 = Balanceamento

"Questão 1 Parte B"

#Bibliotecas Necesárias
from scipy.integrate import odeint
import numpy as np

#Variáveis
a=-0.4
b=0.2
c=0.4
d=0.47

# Definindo as equações diferenciais
def model(Y, t):
    P, Z = Y
    dPdt = a*P + b*Z
    dZdt = c*P - d*Z
    return [dPdt, dZdt]

#Condições iniciais
P0 = 728000
Z0 = 508
y0 = [P0, Z0]

#Vetor Tempo
t = np.arange(0,20,1e-4)

# Resolvendo o sistema de EDOs
Y=odeint(model, y0, t)

#Respsotas
PC = int(Y[-1, 0])
PM = int(np.max(Y[:, 1]))
DM = round(t[np.argmax(Y[:, 1])], 2)
DE = round(t[np.argmax(Y[:, 0] <= P0/2)], 2)

print(f"Pessoas na cidade: {PC}")
print(f"Pessoas na máxima zona de descontaminação: {PM}")
print(f"Tempo ocorre essa população máxima na zona de descontaminação: {DM}")
print(f"Tempo metade da população da cidade terá sido: {DE}")

"Questão 2"
#Bibliotecas Necesárias
import numpy as np
from scipy.integrate import odeint

#Variáveis
alfa=0.12
beta=0.05
gama=0.01
sigma=0.01

# Definindo as equações diferenciais
def model(Y, t):
    D, I = Y
    dDdt = -alfa*D + gama*D*I
    dIdt = beta*I - sigma*D*I
    return [dDdt, dIdt]

# Condições iniciais
D0 = 4
I0 = 12
y0 = [D0, I0]

# Vetor Tempo
t = np.arange(0, 200, 1e-4)

# Resolvendo o sistema de EDOs
Y = odeint(model, y0, t)

# Respostas
MaxD = round(np.max(Y[:, 0]), 2)
MinI = round(np.min(Y[:, 1]), 2)
MaxDI = round(Y[np.argmax(Y[:, 0]), 1], 2)
MinID = round(Y[np.argmin(Y[:, 1]), 0], 2)
MaxMin = round(t[np.argmin(Y[:, 1])] - t[np.argmax(Y[:, 0])], 2)

print(f"Valor máximo do dólar: {MaxD}")
print(f"Valor mínimo do Ibovespa: {MinI}")
print(f"Valor do Ibovespa quando o dólar atinge o seu valor máximo: {MaxDI}")
print(f"Valor do dólar quando o Ibovespa atinge o seu valor mínimo: {MinID}")
print(f"Intervalo de tempo entre um máximo do dólar e um mínimo do Ibovespa: {MaxMin}")