#%%Exercício 1 Modulo ES

import numpy as np
import matplotlib.pyplot as plt
Dia=np.arange(1,31) #21
Estoque=np.zeros(30) #29
Estoque[0]=240 #8
for t in range(1,30):
    Estoque[t]=Estoque[t-1]-240/30 #18
Estocagem=0.30/30*Estoque #9
plt.plot(Dia,Estocagem) #27
plt.bar(Dia,Estocagem) #5
PerdaTotal=np.sum(Estocagem) #16
print(PerdaTotal)

#%%Exercício 2 Modulo ES
import numpy as np
mhp=int(100)
dhp=int(40)

mhg=int(30*0.5+50*0.4+70*0.1)
estoquehp=np.zeros(7)
estoquehg=np.zeros(7)
estoquehp[0]=1700
estoquehg[0]=720

for t in range(1,7):
    estoquehp[t]=estoquehp[t-1]-100
    estoquehg[t]=estoquehg[t-1]-42
custoestoquehp=0.05*estoquehp
custoestoquehg=0.05*estoquehg

custototal=np.sum(custoestoquehp)+np.sum(custoestoquehg)
print(custototal)

estoquehg2=np.zeros(30)
estoquehp2=np.zeros(30)
estoquehp2[0]=1700
estoquehg2[0]=720
for t in range(1,30):
    estoquehp2[t]=estoquehp2[t-1]-100
    estoquehg2[t]=estoquehg2[t-1]-42
    if estoquehp2[t]==0:
        print(t+1)
    if estoquehg2[t]==0:
        print(t+1)    



    


