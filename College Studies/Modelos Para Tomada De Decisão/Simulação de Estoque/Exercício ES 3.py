#%% Questão 1
DemDiaria=250/30
CustoEstoqueUnitario=0.30/30
CustoFreteUnitario=20
#Função para o Cálculo de perdas 
def fCustosTotais(q):
	#Alocação o vetor de estoque
    estoque=np.zeros(30)
	#Estoque inicial 
    estoque[0]=q
	#Contador de fretes
    frete=1
	#Calculos estoques diários
    for t in range(1,30):
        estoque[t]=estoque[t-1]-DemDiaria #2
        if estoque[t]<=0:
            estoque[t]=estoque[t]+q #17
            frete=frete+1 #7
	#Cálculo dos Custos
    CustoEstoque=np.sum(CustoEstoqueUnitario*estoque) #27
    CustoFrete=frete*CustoFreteUnitario #22
    CustoTotal=CustoEstoque+CustoFrete #18
    return CustoTotal
#Alocação dos Vetores
import numpy as np
Lote=np.arange(10,500)
CustoTotal=np.zeros(len(Lote))

#Custo do mês com relação à quantidade comprada de camisetas
for j in range(len(Lote)):
	q=Lote[j]
	CustoTotal[j]=fCustosTotais(q) #13
print('Mínimo Custo R$', round(min(CustoTotal),2))
print('Lote Econômico : ', Lote[np.argmin(CustoTotal)])	

#%%Questão 2
import math as fm
import numpy as np
CustoFrete=50
CustoEstoqueUnitario=0.3
DemandaSemanal=np.array([15,13,10,12,17,9,14,12,15,19,14,13,8,12,16,12,11,15,10,16])
DemandaSemanalMedia=np.mean(DemandaSemanal)
LoteEconomico=fm.sqrt(2*CustoFrete*DemandaSemanalMedia/CustoEstoqueUnitario)
print("O lote economico é :", LoteEconomico)
DesvioPadraoDemandaSemanal=np.std(DemandaSemanal)
LoteEconomico_c=fm.sqrt(2*CustoFrete*(DemandaSemanalMedia+DesvioPadraoDemandaSemanal)/CustoEstoqueUnitario)
print("O lote econônico considerando a soma entre a demanda média semanal e o desvio da demanda média semnal é ", LoteEconomico_c)
LoteEconomico_d=fm.sqrt(2*CustoFrete*(DemandaSemanalMedia-DesvioPadraoDemandaSemanal)/CustoEstoqueUnitario)
print("O lote econônico considerando a diferença entre a demanda média semanal e o desvio da demanda média semnal é ", LoteEconomico_d)
LotesEconomicos=np.array([LoteEconomico,LoteEconomico_c,LoteEconomico_d])
MediaLotesEconomicos=np.mean(LotesEconomicos)
print("A média dos lotes econômicos é ",MediaLotesEconomicos)
DesvioLotesEconomicos=np.std(LotesEconomicos)
print("A média dos lotes econômicos é ",DesvioLotesEconomicos)
