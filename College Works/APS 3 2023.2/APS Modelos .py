#Sobre este Trabalho
"""
Este trabalho se trata do APS de Modelos para Tomada de Decisão, em que simularemos o estoque 
de massas do restaurante Piazza Sicilia , mas usaremos do Python para realizar a Simulação de
Monte Carlo para avaliar descobrir qual a melhor forma de estocagem dos ingredientes de massas.
"""

#Integrantes
"""
Beatriz Emi Ueda (beatrizeu@al.insper.edu.br),  
Beatriz Fernandes da Silva (beatrizfs1@al.insper.edu.br),  
Gabriela Abib (gabrielaa6@al.insper.edu.br),  
Hicham Munir Tayfour (hichamt@al.insper.edu.br),  
Júlia de Aquino Rocha (juliaar1@al.insper.edu.br),  
Raynnara Silva de Freitas Gurgel (raynnarasf@al.insper.edu.br).  
"""
#Bibliotecas a serem usadas para a resolução desse problema
import numpy as np
import matplotlib.pyplot as plt

#Contexto geral
"""
O restaurante Piazza Sciilia, localizado na cidade de Natal, Rio Grande do Norte, é um restaurante
italiano que preza pela qualidade e excelência de suas massas, por isso suas massas são feitas na hora.
Para isso é necessário Semolinas, leite e farinha, sendo o Semolinas e o leite perecíveis, e a farinha não perecível.
O restaurante quer avaliar a demanda por Semolinass, leite e farinha por 30 dias e com isso achar o lote econômico
para os ingredientes.
"""

#Funções Demandas de Semolinas, Leite e Farinha
def fDemSemolinas(q):
    vDemSemolinas=np.random.normal(1000,250,q)
    return vDemSemolinas
def fDemLeite(q):
    vDemLeite=np.random.normal(2000,250,q)
    return vDemLeite
def fDemFarinha(q):
    vDemFarinha=np.random.uniform(2000,5000,q)
    return vDemFarinha

#Calculo da Demanda Mensal dos Ingredientes
"Dias Simulados (como simularemos para o mês, será q=30)"
q=30

DemandaMensalTotal=fDemSemolinas(q)+fDemLeite(q)+fDemFarinha(q)

MediaMensal=np.mean(DemandaMensalTotal)

DesvioPadraoMensal=np.std(DemandaMensalTotal)

#Calculo do Lote Econômico

"Para o cálculo do lote econômico, utilizaremos a fórmula do lote econômico de Wilson, que é:"
#LoteEconômico=(2*DemandaMédia*CustoDeFrete/CustoDeEstocagem)^(1/2)
"Onde:"
CustoDeEstoqueDoSemolinas=int(5)
CustoDeEstoqueDoLeite=int(6)
CustoDeEstoqueDaFarinha=int(2)

CustoDeEstocagem=np.mean([CustoDeEstoqueDoSemolinas,CustoDeEstoqueDoLeite,CustoDeEstoqueDaFarinha])

CustoDeFrete=int(100)

LoteEconômico=(2*MediaMensal*CustoDeFrete/CustoDeEstocagem)**(1/2)
LoteEconômicoSegurança=(2*(MediaMensal+DesvioPadraoMensal)*CustoDeFrete/CustoDeEstocagem)**(1/2)

#Simulação Para o Estoque dos Ingredientes

N=int(10000)
Dias=30

Valores=np.zeros(N)

for q in range(0,N):
    DemandaSim=fDemSemolinas(Dias)+fDemLeite(Dias)+fDemFarinha(Dias)
    MediaSim=np.mean(DemandaSim)
    Valores[q]=MediaMensal

MediaSim=np.mean(Valores)
DesvioPadraoSim=np.std(DemandaSim)

#Valores Finais
print("A média mensal de demanda é de", round(MediaMensal, 0), "ingredientes.")
print("O desvio padrão mensal de demanda é de", round(DesvioPadraoMensal, 0), "ingredientes.")
print("O custo de estocagem é de", round(CustoDeEstocagem, 0), "reais.")
print("O custo de frete é de", round(CustoDeFrete, 0), "reais.")
print("O lote econômico é de", round(LoteEconômico, 0), "ingredientes.")
print("O lote econômico de seguranaça é de", round(LoteEconômicoSegurança, 0), "ingredientes.")
print("A média da simulação é de", round(MediaSim, 0), "ingredientes.")
print("O desvio padrão da simulação é de", round(DesvioPadraoSim, 0), "ingredientes.")

"""
Após descobrirmos os lotês econômicos e lote de segurança, o restuarante Piazza Sicilia solicitou a construção de uma modelo
para estimação de clientes por dia. Para isso utilizaremos equações diferenciais oridnárias, que são equações que envolvem
derivadas de uma ou mais variáveis dependentes em relação a uma variável independente. Para isso, faremos o uso da função odeint
presente na variável scipy.integrate, que é uma função que resolve equações diferenciais ordinárias e seguinda a lógica do modelo de Bass."""

#Bibliotecas a serem usadas para a resolução desse problema
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Definição das constantes
N=751300 #População de Natal
C0=10000 #Clientes iniciais
P0=N-C0 #Adotantes em potencial iniciais
A0=C0 #Adotantes iniciais
a=0.001 #Coeficiente de inovação
i=0.02 #Coeficiente de imitação
c=10 #Coeficiente de saturação

#Definição do sistema de equações diferenciais
def SisEqDif(Y,t):
    P=Y[0]
    A=Y[1] 
    dPdt = -a*P-(i*c/N)*P*A #Equação diferencial dos adotantes em potencial
    dAdt = a*P+(i*c/N)*P*A #Equação diferencial dos adotantes
    return [dPdt,dAdt]

#Definição do intervalo de tempo
T = np.arange(0,30,0.0001)

#Definição das condições iniciais
Y0=[P0,A0]

#Rodando o OdeInt
Y=odeint(SisEqDif,Y0,T)

#Plotando o gráfico
plt.plot(T,Y[:,0],'g',label='Adotantes em Potencial (P)')
plt.plot(T,Y[:,1],'r',label='Adotantes (A)')
plt.axis([0, max(T), 0, max(max(Y[:,0]), max(Y[:,1]))])
plt.ylabel('População')
plt.xlabel('Tempo (dias)')
plt.title('Modelo de Bass para Clientes do Pizza Sicilia')
plt.legend()
plt.show()

# Definição do intervalo de tempo
T = np.arange(0, 30, 7)  # A cada uma semana

# Definição das condições iniciais
Y0 = [P0, A0]

# Rodando o OdeInt
Y = odeint(SisEqDif, Y0, T)

# Plotando o gráfico
plt.plot(T, Y[:, 1], 'r', label='Adotantes (A)')
plt.ylabel('População')
plt.xlabel('Tempo (semanas)')
plt.title('Adotantes a cada uma semana')
plt.legend()
plt.show()

# Imprimindo os valores dos adotantes a cada semana
for i, adotante in enumerate(Y[:, 1]):
    print(f"Semana {i+1}: {round(adotante)}")