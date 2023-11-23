#Função para calcular a demanda com base nos dados, usando a frequência relativa 
def fDemanda():
    aleat=np.random.uniform(0,1)
    if aleat<=0.71:
        Demanda=3
    else:
        Demanda=4
    return Demanda

#Função para calcular o custo total (estocagem + frete ) com a demanda simulada
def fCustoTotalSim(q):
    Estoque=np.zeros(365)
    Estoque[0]=q
    CustoDeFrete=Frete
    for t in range(1,365):
        Estoque[t]=Estoque[t-1]-fDemanda()
        if Estoque[t]<0:
            Estoque[t]=Estoque[t]+q
            CustoDeFrete=CustoDeFrete+Frete
    CustoDeEstocagem=np.sum(Estoque*CustoDeEstocagem)
    CustoTotal=CustoDeEstocagem+CustoDeFrete
    return CustoTotal

#Modificação para custos de estocagem progessivos 
def fCustoTotalSim(q):
    vEstoque=np.zeros(365)
    Estoque=np.zeros(365)
    CustoDeEstoque=np.zeros(365)
    Estoque[0]=q
    Contador=0
    CustoDeFrete=Frete
    for t in range(1,365):
        Contador=Contador+1
        Estoque[t]=Estoque[t-1]-fDemanda()
        if Estoque[t]<0:
            Estoque[t]=Estoque[t]+q
            CustoDeFrete=CustoDeFrete+Frete
            Contador=1
        if Contador==1:
            vEstocagem[t]=18
        else:
            vEstocagem[t]=36
        CustoDeEstoque[t]=vEstocagem[t]*Estoque[t]
    CustoDeEstocagem=np.sum(CustoDeEstoque)
    CustoTotal=CustoDeEstocagem+CustoDeFrete
    return CustoTotal
            

            
