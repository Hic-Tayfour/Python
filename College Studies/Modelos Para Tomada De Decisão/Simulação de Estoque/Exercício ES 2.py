#%%Questão 1
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
# Definição de constantes.
DemDiaria=int(250/30)
CustoEstoqueUnitario=np.round(0.30/30,2)
CustoFreteUnitario=20
# Alocação de vetores.
Lote=np.arange(10,500)
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