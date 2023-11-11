#%% Quest�o 1
# Importa��o das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Fun��o demanda pelos filtros azuis.
def fDemAzul(n):
    vDemAzul=np.round(np.random.normal(700,20,n))
    return vDemAzul

# Fun��o demanda pelos filtros vermelhos.
def fDemVermelho(n):
    vDemVermelho=np.zeros(n)
    for i in range(0,n):
        Aleat=np.random.uniform(0,1)
        if Aleat<=0.1:
            vDemVermelho[i]=200
        elif Aleat<=0.4:
            vDemVermelho[i]=300
        elif Aleat<=0.9:
            vDemVermelho[i]=400
        else:
            vDemVermelho[i]=500
    return vDemVermelho

# Simula��o de 1000 lotes econ�micos.

# N�mero de simula��es.
Num=1000

# Frete.
Frete=20

# Custo unit�rio de estocagem.
CUE=0.50

# Vetor Lote Econ�mico.
LoteEco=np.zeros(Num)

# Simula��es.
vDemAzul=fDemAzul(Num)
vDemVermelho=fDemVermelho(Num)

for i in range(0,Num):
    Demanda=vDemAzul[i]+vDemVermelho[i]
    LoteEco[i]=(2*Frete*Demanda/CUE)**0.5
    
print('Lote Econ�mico (M�dia) =',np.mean(LoteEco))
print('Lote Econ�mico (Desvio-padr�o) =',np.std(LoteEco))

#%%Quest�o 2
# Fun��o que calcula custos por estocagem e por frete.
Estocagem=0.50/7

def fCustoTotal(q):
    Lote=q
    vEstoque=np.zeros(20)
    vEstoque[0]=Lote
    vFrete=np.zeros(20)  
    for t in range(1,20):
        DemAzul=np.round(fDemAzul(1)/7)
        DemVermelho=np.round(fDemVermelho(1)/7)
        Dem=DemAzul+DemVermelho
        vEstoque[t]=vEstoque[t-1]-Dem
        if vEstoque[t]<0:
            vEstoque[t]=vEstoque[t]+Lote
            vFrete[t]=Frete
    FreteTotal=np.sum(vFrete)
    EstocagemTotal=np.sum(vEstoque*Estocagem)
    CustoTotal=FreteTotal+EstocagemTotal
    return CustoTotal

# C�lculo do custo total m�nimo (lote �timo).
LoteInicial=200
LoteFinal=500
vLote=np.zeros(LoteFinal-LoteInicial+1)
vCustoTotal=np.zeros(LoteFinal-LoteInicial+1)
vLote=np.arange(LoteInicial,LoteFinal+1)

for q in range(LoteInicial,LoteFinal+1):
    vCustoTotal[q-LoteInicial]=fCustoTotal(q)

CustoMin=np.min(vCustoTotal)
LoteOtimo=vLote[np.argmin(vCustoTotal)]

print('Custo M�nimo = ',CustoMin)
print('Lote �timo = ',LoteOtimo)

plt.plot(vLote,vCustoTotal)

# Simula��es do Lote Econ�mico.
CustoMin=np.zeros(1000+1)
LoteOtimo=np.zeros(1000+1)
for s in range(0,1000):
    for q in range(LoteInicial,LoteFinal+1):
        vCustoTotal[q-LoteInicial]=fCustoTotal(q)
    CustoMin[s]=np.min(vCustoTotal)
    LoteOtimo[s]=vLote[np.argmin(vCustoTotal)]

print('Lote Econ�mico (M�dia) =',np.mean(LoteOtimo))
print('Lote Econ�mico (Desvio-padr�o) =',np.std(LoteOtimo))


