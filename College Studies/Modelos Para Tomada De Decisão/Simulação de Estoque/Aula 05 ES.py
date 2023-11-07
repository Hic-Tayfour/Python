#%%Problema da Padaria do Beijamin Salamão ; Mas usando a Simulação de Monte Carlo
# Importação das bibliotecas numpy e matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# Função Geradora de Demandas

def fGeradoraDemanda():
    x=np.random.randint(0,31)
    if x<=10:
        Demanda=400
    elif x<=23:
        Demanda=600
    else:
        Demanda=750
    return Demanda
print(fGeradoraDemanda())

#Função que calcula calcula perdas com uma quantidade q de pãezinhos
def fPerda(q):
    Demanda=fGeradoraDemanda()
    if q<=Demanda:
        Perda=0.5*(Demanda-q)
    else:
        Perda=0.1*(q-Demanda)
    return Perda
print(fPerda(600))

#Função que calcula a perda dos 30 dias simulados
def fPerdaTotal(q):
    PerdaDiaria=np.zeros(30)
    for t in range(0,30):
        PerdaDiaria[t]=fPerda(q)
    PerdaTotal=np.sum(PerdaDiaria)
    return PerdaTotal

print(fPerdaTotal(600))

# Calculo de diversas perdas para valores de q

qmax=800

vQuant=np.arange(0,qmax)
vPerdaTotal=np.zeros(qmax)

for q in range(0,qmax):
    vPerdaTotal[q]=fPerdaTotal(q) 
print(vPerdaTotal)

plt.plot(vQuant,vPerdaTotal)

print("Perda Mínima de R$",np.min(vPerdaTotal))
print("Quantidade Ótima é de ", vQuant[np.argmin(vPerdaTotal)])

N=1000
vPerdaTotalSim=np.zeros(N)
vQuantOtima=np.zeros(N)

for s in range(0,N):
    for q in range(0,qmax):
        vPerdaTotal[q]=fPerdaTotal(q) 
    vPerdaTotalSim[s]=np.min(vPerdaTotal)
    vQuantOtima[s]=vQuant[np.argmin(vPerdaTotal)]

print('Perda Simulada= ',np.mean(vPerdaTotalSim),'+\-',np.std(vPerdaTotalSim))
print('Quantidade Simulada= ',np.mean(vQuantOtima),'+\-',np.std(vQuantOtima))

plt.figure()
plt.hist(vQuantOtima)
