#%%Criação e uso de Functions para programas
import numpy as np
import matplotlib.pyplot as plt
Frete=600
CustoDeEstoque=0.02
DemandaDiaria=15
def fCalculaCustos(Lote):
    Estoque=np.zeros(30)
    Estoque[0]=Lote
    CustoFrete=Frete
    for t in range(1,30):
        Estoque[t]=Estoque[t-1]-DemandaDiaria
        if Estoque[t]<DemandaDiaria:
            Estoque[t]=Estoque[t]+Lote
            CustoFrete=CustoFrete+Frete
    CustoDeEstocagem=np.sum(CustoDeEstoque*Estoque)
    CustoTotal=CustoDeEstocagem+CustoFrete
    return CustoTotal
print(fCalculaCustos(100)) #Testanto a Função

#Aplicando a Função 
Lote=np.arange(500,2001)
Custos=np.zeros(2000-500+1)
for q in Lote:
    Custos[q-500]=fCalculaCustos(q)
print(Custos)
plt.plot(Lote,Custos)

#%%Simulação com variáveis discretas 
import math as fm
import matplotlib.pyplot as plt
import numpy as np
"""
Padaria Beijamin Salomão
"""
#1.Criação das Classes; DemandaMédia ; Frequência

#    Classes    DemandaDiária    Frequência
"De 300 a 500       400             10"
"De 500 a 700       600             13"
"De 700 a 800       750              7"

#2.Demanda Média
Dm=(10*400+13*600+7*750)/30  
print("A demanda média de pãesxzinhos é " ,round(Dm,2))

#3.Adotando a Demanda Média é 568

#4. Quanto ela perde por pão a mais que a demanda diária ? E quanto deixa de lucrar por pãozinho abaixo da demanda do dia ?
"""
Perda por pãozinho a mais: R$0,10 (0,50-0,40)
Lucro perdido (Perda) por pãozinho a menos: R$0,50 (1-0,50)
"""

#5. Vamos tentar estimar uma perda imaginando que a demanda diária dele seja 568
Pexcesso=0.1
Pfalta=0.5
Dm=568
PC1=((Dm-400)*Pexcesso)
print(PC1)
PC2=((600-Dm)*Pfalta)
print(PC2)
PC3=((750-Dm)*Pfalta)
print(PC3)
PerdaMensalEstimada=10*PC1+13*PC2+7*PC3
print("A perda mensal estimada é de R$",PerdaMensalEstimada)

#%%Vamos simular com variáveis discretas para resolver o problema da padaria 
import math as fm
import matplotlib.pyplot as plt
import numpy as np

#Criação do Vetor Demanda
vDemanda=np.zeros(30)
vDemanda[0:10]=400
vDemanda[10:23]=600
vDemanda[23:]=750
print(vDemanda) #Conferindo os valores

vDemandaMedia=np.mean(vDemanda)
print(vDemandaMedia)

#Função Perda Mensal
def fPerdas(q):
    Perda=np.zeros(30)
    for t in range(0,len(Perda)):
        if q<=vDemanda[t]:
            Perda[t]=0.50*(vDemanda[t]-q)
        else:
            Perda[t]=0.10*(q-vDemanda[t])
    PerdaTotal=np.sum(Perda)
    return PerdaTotal
vQuant=np.arange(500,801)
print(vQuant)

vPerdas=np.zeros(len(vQuant))
for q in range(0,len(vQuant)):
    vPerdas[q]=fPerdas(vQuant[q])
print(vPerdas)

plt.plot(vQuant,vPerdas)
print(np.min(vPerdas))
print(vQuant[np.argmin(vPerdas)]) 

#%%Problema da Padaria do Beijamin Salamão ; Mas usando a Simulação de Monte Carlo
# Importação das bibliotecas numpy e matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# Vetor de frequências.

vFreq = [10,13,7]

# Vetor de frequências acumuladas.

vFreqAcum = np.cumsum(vFreq)

# Número de simulações

N=1000

# Função demandas simuladas.

vDemanda = np.zeros(30)

def fDemandaSim(q):
    for t in range(30):
        x = np.random.randint(1,31)    
        if x <= vFreqAcum[0]:
            vDemanda[t] = 400
        elif x <= vFreqAcum[1]:
            vDemanda[t] = 600
        else:
            vDemanda[t] = 750
    return vDemanda

# Função perdas.

vPerdas = np.zeros(30)

def fPerdas(q):
    for t in range(0,len(vDemanda)):
        if q <= vDemanda[t]:
            vPerdas[t] = 0.50*(vDemanda[t] - q)
        else:
            vPerdas[t] = 0.10*(q- vDemanda[t])
    PerdasTotais=np.sum(vPerdas)
    return PerdasTotais

# Simulações.

vPerdaMin=np.zeros(N)
vQMin=np.zeros(N)

vQuant=np.arange(500,801)
vPerda=np.zeros(801-500)

for n in range(0,N):
    vDemanda = fDemandaSim(n)
    for q in range(0,len(vQuant)):
        vPerda[q] = fPerdas(vQuant[q])
    vPerdaMin[n]=np.min(vPerda)
    vQMin[n] = vQuant[np.argmin(vPerda)]
    
# Histograma da quantidade ótima de pãzeinhos produzidos.
plt.figure()
plt.hist(vQMin)

# Histograma das perdas mínimas.
plt.figure()
plt.hist(vPerdaMin)

# Quantidade ótima (média +/- desvio padrão).

print('Quantidade ótima a ser produzida: q =',np.mean(vQMin),'+/-',np.std(vQMin))

# Custo mínimo (média +/- desvio padrão).

print('Custo mínimo: C =',np.mean(vPerdaMin),'+/-',np.std(vPerdaMin))
