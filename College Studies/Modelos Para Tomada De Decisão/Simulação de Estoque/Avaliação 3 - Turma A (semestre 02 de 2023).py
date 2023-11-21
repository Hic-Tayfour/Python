"Questão 1"
import numpy as np
import matplotlib.pyplot as plt

Demanda = 4
Estocagem = 20
Frete = 300

LoteEconômico = (2 * Frete * Demanda / Estocagem) ** 0.5

print('Custo Unitário de Estocagem = ',Estocagem)
print('Lote Econômico = ',LoteEconômico)

"Questão 2"
# Vetor tempo.

Dia = np.arange(1,366)

# Tamanho do lote.

Lote = 20

# Definições iniciais.

Estoque = np.zeros(365)
Estoque[0] = Lote
CustoDeFrete = Frete
# Cálculo dos custos.

for t in range(1,365):
    Estoque[t] = Estoque[t-1] - Demanda
    if Estoque[t] < 0:
        Estoque[t] = Estoque[t] + Lote
        CustoDeFrete = CustoDeFrete + Frete
CustoDeEstocagem = np.sum(Estocagem * Estoque)

print('Custo de Frete = ',CustoDeFrete)
print('Custo de Estocagem = ',CustoDeEstocagem)
print('Custo Total = ',CustoDeFrete + CustoDeEstocagem)

# Cálculo dos custos.

def fCustoTotal(q):
    Estoque = np.zeros(365)
    Estoque[0] = q
    CustoDeFrete = Frete
    for t in range(1,365):
        Estoque[t] = Estoque[t-1] - Demanda
        if Estoque[t] < 0:
            Estoque[t] = Estoque[t] + q
            CustoDeFrete = CustoDeFrete + Frete
    CustoDeEstocagem = np.sum(Estocagem * Estoque)
    CustoTotal = CustoDeEstocagem + CustoDeFrete
    return CustoTotal


# Cálculo do lote econômico.

vLote = np.arange(4,50)

CustoTotal = np.zeros(len(vLote))

for q in range(0,len(vLote)):
    CustoTotal[q] = fCustoTotal(vLote[q])

plt.plot(vLote,CustoTotal)

print('Custo Total Mínimo =',np.min(CustoTotal))
print('Lote Econômico =',vLote[np.argmin(CustoTotal)])

"Questão 3"
# Demanda simulada.

def fDemanda():
    aleat = np.random.uniform(0,1)
    if aleat <= 0.71:
        Demanda = 3
    else:
        Demanda = 5
    return Demanda

# Função que calcula o custo total simulado.

def fCustoTotalSim(q):
    Estoque = np.zeros(365)
    Estoque[0] = q
    CustoDeFrete = Frete
    for t in range(1,365):
        Estoque[t] = Estoque[t-1] - fDemanda()
        if Estoque[t] < 0:
            Estoque[t] = Estoque[t] + q
            CustoDeFrete = CustoDeFrete + Frete
    CustoDeEstocagem = np.sum(Estocagem * Estoque)
    CustoTotal = CustoDeEstocagem + CustoDeFrete
    return CustoTotal
# Cem simulações.

N = 100

LoteEconomico = np.zeros(N)

for s in range(1,N):
    CustoTotal = np.zeros(len(vLote))
    for q in range(0,len(vLote)):
        CustoTotal[q] = fCustoTotalSim(vLote[q])
    LoteEconomico[s] = vLote[np.argmin(CustoTotal)]

print(np.mean(LoteEconomico))
print(np.std(LoteEconomico))
