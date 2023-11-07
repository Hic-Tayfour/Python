#%%Simulação Discreta da Demanda
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
import statistics as st

#Vetor Demanda
vDemanda=[0,1000,2000,3000,5000]

#Vetor Frequência
vFreq=[0.02,0.03,0.05,0.08,0.85]

#Vetor Frequência acumulada
vFreqAcum=np.cumsum(vFreq)

#Determinação do número de simulações
N=1000

#Alocação dos Números aletórios
vAlet=np.zeros(N)

for t in range(0,N):
    vAlet[t]=rnd.uniform(0,1)
# Simulação de Monte Carlo (discreta) das demandas.

vDem=np.zeros(N)

for t in range (0,N):
    if vAlet[t]<=vFreqAcum[0]:
        vDem[t]=vDemanda[0]
    elif vAlet[t]<=vFreqAcum[1]:
        vDem[t]=vDemanda[1]
    elif vAlet[t]<=vFreqAcum[2]:
        vDem[t]=vDemanda[2]
    elif vAlet[t]<=vFreqAcum[3]:
        vDem[t]=vDemanda[3]
    else:
        vDem[t]=vDemanda[4]

#Histograma (Gráfico da Frequências) da demanda

plt.hist(vDem,bins=[0,1000,2000,3000,5000])
plt.title("Histograma das Demandas")

#%%Simulação Contínua do Preço

#Simulação de Monte Carlo(Contínua) do preço

n=10000
media=3.65
desvio=0.20

vPreco=np.random.normal(media,desvio,N)

#Histograma (gráfico das frequências) do preço

nBins=60

plt.figure()
plt.hist(vPreco,nBins)
plt.title("Histograma dos Preços")
 
#Simualção do Lucro
vLucro=vDem*vPreco-n

#Lucro Médio
LucroMedio=np.mean(vLucro)
print("O Lucro Médio é de R$",LucroMedio)

#Desvio Padrão do Lucro
DesvPadLucro=np.std(vLucro)
print("O Desvio Padrão do Lucro é de R$",DesvPadLucro)

