#%% Parte 1
import numpy as np
import matplotlib.pyplot as plt

Lote=600
EstoqueInicial=Lote
CustoDeEstocagem=(0.02*4)
Frete=50
DemandaDiária=600/30

Tempo=np.arange(1,31)

Estoque=np.zeros(30)

Estoque[0]=Lote

CustoDeFrete=Frete

for t in range(1,30):
    Estoque[t]=Estoque[t-1]-DemandaDiária
    if Estoque[t]<=0:
        Estoque[t]=Estoque[t]+Lote
        CustoDeFrete=CustoDeFrete+Frete

CustoTotalDeEstocagem=np.sum(CustoDeEstocagem*Estoque)

CustoTotal=CustoTotalDeEstocagem+CustoDeFrete

print("Custo de Estocagem R$",CustoTotalDeEstocagem)
print("Custo de Frete R$",CustoDeFrete)
print("Custo Total R$",CustoTotal)

#%% Parte 2
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
# Definição de constantes.
DemDiaria=600/30
CustoEstoqueUnitario=(0.02*4)
CustoFreteUnitario=50
# Alocação de vetores.
Lote=np.arange(100,300)
CustoFrete = np.zeros(len(Lote))
CustoEstoque = np.zeros(len(Lote))
CustoTotal= np.zeros(len(Lote))
# Vetor dia.
Dia=np.arange(1,31) #14
# Custos do mês com relação à quantidade comprada de camisetas.
for j in range(len(Lote)):
    q = Lote[j] #8
    # Alocação do vetor de estoque
    estoque = np.zeros(30)
    # Estoque inicial
    estoque[0] = q #3
    # Contador de fretes
    frete = 1
    # Cálculos estoques diários
    for t in range(1,30):
        estoque[t] = estoque[t-1] - DemDiaria #2
        if estoque[t] <= 0:
            estoque[t] = estoque[t] + q #17
            # Contabilizar frete
            frete = frete + 1 #7
    # Cálculo dos custos
    CustoEstoque[j] = sum(CustoEstoqueUnitario*estoque) #27
    CustoFrete[j] = frete*CustoFreteUnitario #22
    CustoTotal[j] = CustoEstoque[j] + CustoFrete[j] #10
print(f'Mínimo custo: {round(min(CustoTotal),2)}')
print(f'Lote Ecônomico: {Lote[np.argmin(CustoTotal)]}')
print(f'Número de fretes: {frete}')
# Gráfico do total de perdas com estocagem (azul) e com frete (vermelho) em função do lote.
plt.plot(Lote,CustoEstoque,color='blue')
plt.plot(Lote,CustoFrete,color='red')
plt.plot(Lote,CustoTotal,color='green')
# O valor mínimo da soma das perdas com frete e estocagem é dado por 
round(min(CustoTotal),2)
# O lote que resulta nesse valor mínimo é dado por
Lote[np.argmin(CustoTotal)]
print(int(np.mean(CustoTotal)))
print(int(np.std(CustoTotal)))
