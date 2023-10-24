#%%Exercício 1 Passada 
import numpy as np
import matplotlib.pyplot as plt

EstoqueInicial=2500
DemandaDiaria=15
CustoDeEstocagem=0.02

Estoque=np.zeros(365)
print(len(Estoque))

Estoque[0]= EstoqueInicial
Tempo=np.arange(1,366)

for t in range(1,365):
    Estoque[t]=Estoque[t-1]-DemandaDiaria
    if Estoque[t]<=DemandaDiaria:
        Estoque[t]=Estoque[t]+EstoqueInicial
print(Estoque)

plt.plot(Tempo,Estoque)
plt.bar(Tempo, Estoque)

custodoestoque=0.02*Estoque
print(np.sum(custodoestoque))

#%%Continuação do probleminha 
import numpy as np
import matplotlib.pyplot as plt

Lote=365*15/2
EstoqueInicial=Lote
DemandaDiaria=15
CustoDeEstocagem=0.02
Frete=600
CustodeFrete=Frete

Estoque=np.zeros(365)
Tempo=np.arange(1,366)

Estoque[0]= EstoqueInicial

for t in range(1,365):
    Estoque[t]=Estoque[t-1]-DemandaDiaria
    if Estoque[t]<DemandaDiaria:
        Estoque[t]=Estoque[t]+Lote
        CustodeFrete=CustodeFrete+Frete
print(Estoque)

plt.plot(Tempo,Estoque)
plt.bar(Tempo, Estoque)

custodoestoque=0.02*Estoque
print('Custo de Estocagem do produto R$',np.sum(custodoestoque))
print('Custo Total R$',np.sum(custodoestoque)+CustodeFrete)

#%%Simulando para 1000 unidades de ssd
import numpy as np
import matplotlib.pyplot as plt

Lote=1000
EstoqueInicial=Lote
DemandaDiaria=15
CustoDeEstocagem=0.02
Frete=600
CustodeFrete=Frete

Estoque=np.zeros(365)
Tempo=np.arange(1,366)

Estoque[0]= EstoqueInicial

for t in range(1,365):
    Estoque[t]=Estoque[t-1]-DemandaDiaria
    if Estoque[t]<DemandaDiaria:
        Estoque[t]=Estoque[t]+Lote
        CustodeFrete=CustodeFrete+Frete
print(Estoque)

plt.plot(Tempo,Estoque)
plt.bar(Tempo, Estoque)

custodoestoque=0.02*Estoque
print('Custo de Estocagem do produto R$',np.sum(custodoestoque))
print('Custo Total R$',np.sum(custodoestoque)+CustodeFrete)

