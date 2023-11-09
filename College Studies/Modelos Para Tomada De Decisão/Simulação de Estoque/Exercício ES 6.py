#%%Questão 1 
#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Cálculo dos vetores de frequência
sim = 30

# Simulação da disponibilidade de produtos
produtos = np.array([10, 14, 18, 22, 26])
vfreq = np.array([0.15, 0.20,0.30,0.20,0.15])
vfreqacum = np.zeros(len(vfreq))
vfreqacum[0] = vfreq[0]

for t in range(1,len(vfreq)):
        vfreqacum[t] = vfreqacum[t-1] + vfreq[t]
produtosim = np.zeros(sim)
# Simulação da quantidade de produtos fabricados

for t in range(0,sim):
    aleat = np.random.random()
    if aleat <= vfreqacum[0]:
        produtosim[t] = produtos[0]
    elif aleat <= vfreqacum[1]:
        produtosim[t] = produtos[1]
    elif aleat <= vfreqacum[2]:
        produtosim[t] = produtos[2]
    elif aleat <= vfreqacum[3]:
        produtosim[t] = produtos[3]    
    else:
        produtosim[t] = produtos[4]

# Simulação do número de clientes
clientes = np.random.poisson(24,sim)
demanda = np.zeros(sim)
for t in range(0,sim):
    demanda[t] = int(0.7*clientes[t])
# Cálculo do prejuízo e do lucro diários
prejuizo = np.zeros(sim)
lucro = np.zeros(sim)
for t in range(0,sim):
    if demanda[t] <= produtosim[t]:
        lucro[t] = demanda[t]*100
    else:
        lucro[t] = produtosim[t]*100
        prejuizo[t] = (demanda[t]-produtosim[t])*40
lucrodiario = lucro-prejuizo
lucromedio = np.mean(lucrodiario)

#%%Questão 2
# Importação das bibliotecas.

import numpy as np
import matplotlib.pyplot as plt

# Definição de constantes.
NumSim=1000
MediaDolar=5.17
DesvpadDolar=0.15
PerdaPorExcesso=29
PerdaPorFalta=35
QuantInicial=300
QuantFinal=600

# Dados da demanda.
vDemanda=np.array([400,450,500,550])
vFreq=np.array([0.15,0.23,0.45,0.17])

# Cálculo da frequência acumulada.
vFreqAcum=np.cumsum(vFreq)

# Função demanda simulada.
def fDemSim(aleat):
    if aleat<=vFreqAcum[0]:
        demanda=vDemanda[0]
    elif aleat<=vFreqAcum[1]:
        demanda=vDemanda[1]
    elif aleat<=vFreqAcum[2]:
        demanda=vDemanda[2]
    else:
        demanda=vDemanda[3]
    return demanda

# Função perda.
def fSimPerda(q):
    if q<=demanda:
        perda=PerdaPorFalta*(demanda-q)
    else:
        perda=PerdaPorExcesso*(q-demanda)
    return perda

# Simulações
Quant=np.zeros(QuantFinal-QuantInicial)
PerdaReais=np.zeros(QuantFinal-QuantInicial)
PerdaMinima=np.zeros(NumSim)
QuantPerdaMinima=np.zeros(NumSim)
for s in range(0,NumSim):
    # Geração do aleatório para a demanda.
    aleat=np.random.rand()
    # Cálculo da demanda simulada.
    demanda=fDemSim(aleat)
    # Geração da cotação simulada do dólar.
    CotDolar=np.random.normal(MediaDolar,DesvpadDolar)
    # Cálculo da quantidade simulada de perda mínima.
    for q in range(QuantInicial,QuantFinal):
        Quant[q-QuantInicial]=q
        PerdaDolar=fSimPerda(q)
        PerdaReais[q-QuantInicial]=PerdaDolar*CotDolar
    PerdaMinima[s]=np.min(PerdaReais)
    QuantPerdaMinima[s]=Quant[np.argmin(PerdaReais)]

# Histograma da quantidade de perda mínima.
plt.hist(QuantPerdaMinima)

# Média da quantidade de perda mínima.
print(np.mean(QuantPerdaMinima))

# Desvio padrão da quantidade de perda mínima.
print(np.std(QuantPerdaMinima))