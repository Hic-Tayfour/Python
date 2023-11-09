#%%Questão 1
import numpy as np
def fDemMagaMa(q):
    vDemMagaMAa=np.random.randint(500,801,q) #12
    return vDemMagaMAa
def fDemLojasLu(q):
    vDemLojasLu=np.zeros(q)
    vDemLojasLu=np.random.normal(700,50,q) #4
    vDemLojasLu=np.round(vDemLojasLu,0)
    return vDemLojasLu
def fDemHavana(q):
    vDemHavana=np.zeros(q)
    for t in range(0,q):
        x=np.random.uniform(0,1)
        if x<=0.3:
            vDemHavana[t]=600 #15
        elif x<=0.7: #14
            vDemHavana[t]=700 #3x
        elif x<=0.9: #14
            vDemHavana[t]=800 #10
        else:
            vDemHavana[t]=900 #17
    return vDemHavana

#%%Questão 2
DemandaTotal=fDemMagaMa(30)+fDemLojasLu(30)+fDemHavana(30)

MediaDaDemanda=np.mean(DemandaTotal) #5

DesvPadDaDemanda=np.std(DemandaTotal) #3

N=int(10000)

Valor=np.zeros(N)

for q in range(0,N):
    DemandaTotal=fDemMagaMa(30)+fDemLojasLu(30)+fDemHavana(30)
    MediaDaDemanda=np.mean(DemandaTotal)
    Valor[q]=MediaDaDemanda
    
MediaDemanda=np.mean(Valor)
DesvPadDemanda=np.std(DemandaTotal)
