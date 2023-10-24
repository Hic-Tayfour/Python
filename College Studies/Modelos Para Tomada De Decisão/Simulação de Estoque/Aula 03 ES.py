#%% Otimização de estoque Calculo do Lote Economico
"Testando Valores Um a Um"
import numpy as np
import matplotlib.pyplot as plt

Lote=949
EstoqueInicial=Lote
CustoDeEstocagem=0.02
Frete=600
DemandaDiária=15

Tempo=np.arange(1,366)

Estoque=np.zeros(365)

Estoque[0]=Lote

CustoDeFrete=Frete

for t in range(1,365):
    Estoque[t]=Estoque[t-1]-DemandaDiária
    if Estoque[t]<DemandaDiária:
        Estoque[t]=Estoque[t]+Lote
        CustoDeFrete=CustoDeFrete+Frete

CustoTotalDeEstocagem=np.sum(CustoDeEstocagem*Estoque)

CustoTotal=CustoTotalDeEstocagem+CustoDeFrete

print("Custo de Estocagem R$",CustoTotalDeEstocagem)
print("Custo de Frete R$",CustoDeFrete)
print("Custo Total R$",CustoTotal)

"Testando Valores Via Vetor"
import numpy as np
import matplotlib.pyplot as plt

Lote=np.arange(500,2001)
EstoqueInicial=Lote
CustoDeEstocagem=0.02
Frete=600
DemandaDiária=15

Tempo=np.arange(1,366)

Estoque=np.zeros(365)
CEst=np.zeros(2001-500)
CFrete=np.zeros(2001-500)

for q in Lote:
    Estoque[0]=q
    CustoDeFrete=Frete
    for t in range(1,365):
        Estoque[t]=Estoque[t-1]-DemandaDiária
        if Estoque[t]<DemandaDiária:
            Estoque[t]=Estoque[t]+q
            CustoDeFrete=CustoDeFrete+Frete
    CEst[q-500]=np.sum(CustoDeEstocagem*Estoque)
    CFrete[q-500]=CustoDeFrete
    
CustoTotal=CEst+CFrete

print("Custo Total R$",CustoTotal)

plt.plot(Lote,CustoTotal)

print("O menor custo total é R$",np.min(CustoTotal))
print("O lote mínimo está na posição ",np.argmin(CustoTotal)) 
"Você pode fazer também print("
print("O lote mínimo é de ",Lote[np.argmin(CustoTotal)])

"Usando uma formula geral para o custo total de estoacagem, frete e do lote economico"
"""
q=(2df/h)^(1/2)
em que 
q=é o lote 
d=demanda total deo produto
f=custo de frete
h=custo unitário
"""
q=(2*15*600/0.02)**(0.5)
print(q)

#Aproximadamente 949 , mas o nosso deu 915 , qual o certo ? O 915, mas o da formula não está errado
#Mas a formula é valida