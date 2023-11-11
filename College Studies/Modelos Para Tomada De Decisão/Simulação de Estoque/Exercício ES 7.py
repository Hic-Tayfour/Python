#%% Questão 1
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Função demanda pelos filtros azuis.
def fDemAzul(n):
    vDemAzul=np.round(np.random.normal(700,20,n))
    return vDemAzul

# Função demanda pelos filtros vermelhos.
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

# Simulação de 1000 lotes econômicos.

# Número de simulações.
Num=1000

# Frete.
Frete=20

# Custo unitário de estocagem.
CUE=0.50

# Vetor Lote Econômico.
LoteEco=np.zeros(Num)

# Simulações.
vDemAzul=fDemAzul(Num)
vDemVermelho=fDemVermelho(Num)

for i in range(0,Num):
    Demanda=vDemAzul[i]+vDemVermelho[i]
    LoteEco[i]=(2*Frete*Demanda/CUE)**0.5
    
print('Lote Econômico (Média) =',np.mean(LoteEco))
print('Lote Econômico (Desvio-padrão) =',np.std(LoteEco))

#%%Questão 2
# Função que calcula custos por estocagem e por frete.
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

# Cálculo do custo total mínimo (lote ótimo).
LoteInicial=200
LoteFinal=500
vLote=np.zeros(LoteFinal-LoteInicial+1)
vCustoTotal=np.zeros(LoteFinal-LoteInicial+1)
vLote=np.arange(LoteInicial,LoteFinal+1)

for q in range(LoteInicial,LoteFinal+1):
    vCustoTotal[q-LoteInicial]=fCustoTotal(q)

CustoMin=np.min(vCustoTotal)
LoteOtimo=vLote[np.argmin(vCustoTotal)]

print('Custo Mínimo = ',CustoMin)
print('Lote Ótimo = ',LoteOtimo)

plt.plot(vLote,vCustoTotal)

# Simulações do Lote Econômico.
CustoMin=np.zeros(1000+1)
LoteOtimo=np.zeros(1000+1)
for s in range(0,1000):
    for q in range(LoteInicial,LoteFinal+1):
        vCustoTotal[q-LoteInicial]=fCustoTotal(q)
    CustoMin[s]=np.min(vCustoTotal)
    LoteOtimo[s]=vLote[np.argmin(vCustoTotal)]

print('Lote Econômico (Média) =',np.mean(LoteOtimo))
print('Lote Econômico (Desvio-padrão) =',np.std(LoteOtimo))


