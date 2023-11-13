#%% Questão 1 A
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt


# Determinação de constantes.
# Preço médio do diesel (R$).

MédiaPD = 3.3
# Desvio-padrão do preço do diesel (R$).

DesvPadPD = 0.4
# Distância (km).

Dist = 90

# Vetor consumo (l/km).
vCons = np.array([2,3,4])

# Vetor frequência.
vFreq = np.array([0.2,0.3,0.5])

# Demanda mensal (kits).
Dem = 4600

# Custo unitário de estocagem (R$ por kit por mês).
CustoUnitEst = 10*30

# Cálculo do frete.
# Consumo Médio (l/km).

ConsMédio = np.sum(vCons*vFreq)
print('Consumo Médio = ',ConsMédio)

# Frete.
Frete = Dist * MédiaPD * ConsMédio
print('Frete = ',Frete)

# Cálculo do Lote Econômico.
LoteEconômico = np.sqrt(2*Frete*Dem/CustoUnitEst)
print('Lote Econômico = ',LoteEconômico)

#%% Questão 1 B
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Determinação de constantes.

# Preço médio do diesel (R$).
MédiaPD = 3.3

# Desvio-padrão do preço do diesel (R$).
DesvPadPD = 0.4

# Distância (km).
Dist = 90

# Vetor consumo (l/km).
vCons = np.array([2,3,4])

# Vetor frequência.
vFreq = np.array([0.2,0.3,0.5])

# Demanda mensal (kits).
Dem = 4600

# Custo unitário de estocagem (R$ por kit por mês).
CustoUnitEst = 10*30

# Simulações do Lote Econômico.
# Função preço simulado.
def fPreçoSim(q):
    vPreço = np.zeros(q)
    vPreço = np.random.normal(MédiaPD,DesvPadPD,q)
    return vPreço

# Função consumo simulado.
def fConsSim(q):
    vConsumo = np.zeros(q)
    for i in range(0,q):
        Aleat = np.random.uniform(0,1)
        if Aleat <= 0.2:
            vConsumo[i] = 2
        elif Aleat <= 0.5:
            vConsumo[i] = 3
        else:
            vConsumo[i] = 4
    return vConsumo

# Simulação do frete.
Num = 1000
FreteSim = Dist*fPreçoSim(Num)*fConsSim(Num)

# Simulação do Lote Econômico.
LoteSim = np.sqrt(2*FreteSim*Dem/CustoUnitEst)
print('Média do Frete = ',np.mean(FreteSim))
print('Desvio-padrão do Frete = ',np.std(FreteSim))
print('Média do Lote Econômico = ',np.mean(LoteSim))
print('Desvio-padrão do Lote Econômico = ',np.std(LoteSim))

#%% Questão 2 A
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Determinação de constantes.
# Demanda diária (kits).
Dem = np.round(4600/30)

# Custo unitário de estocagem (R$ por kit por dia).
CustoUnitEst = 10

# Frete
Frete = 1000

# Custo por venda perdida.
Falta = 20

# Custo por kit em excesso.
Excesso = 10

# Vetor dia (30 dias).
Dia = np.arange(1,31)

# Lote
Lote = 153

# Cálculo das perdas.
Estoque = np.zeros(len(Dia))
Estoque[0] = 0
VendasPerdidas = 0
CustoExcesso = 0
CustoFrete = 0

for t in range(0,len(Dia)):
    Estoque[t] = Estoque[t] + Lote
    if Estoque[t] <= Dem:
        VendasPerdidas = VendasPerdidas + Falta * (Dem - Estoque[t])
        Estoque[t] = 0
    else:
        Estoque[t] = Estoque[t] - Dem
    CustoExcesso = CustoExcesso + Excesso * Estoque[t]
    CustoFrete = CustoFrete + Frete
    
print('Custo por Vendas Perdidas = ',VendasPerdidas)
print('Custo por Estoque em Excesso = ',CustoExcesso)
print('Custo de Frete = ',CustoFrete)
print('Custo Total =',VendasPerdidas + CustoExcesso + CustoFrete)
#%% Questão 2 B
# Função de Cálculo das perdas.
def fCustoTotal(q):
    Lote = q
    Estoque = np.zeros(len(Dia))
    Estoque[0] = 0
    VendasPerdidas = 0
    CustoExcesso = 0
    CustoFrete = 0
    for t in range(0,len(Dia)):
        Dem = np.random.normal(152,12)
        Estoque[t] = Estoque[t] + Lote
        if Estoque[t] <= Dem:
            VendasPerdidas = VendasPerdidas + Falta * (Dem - Estoque[t])
            Estoque[t] = 0
        else:
            Estoque[t] = Estoque[t] - Dem
            CustoExcesso = CustoExcesso + Excesso * Estoque[t]
    CustoFrete = CustoFrete + Frete
    CustoTotal = VendasPerdidas + CustoExcesso + CustoFrete
    return CustoTotal

# Simulações com lote fixo.
Num = 1000
vCustoTotal = np.zeros(Num)

for i in range(0,Num):
    vCustoTotal[i] = fCustoTotal(152)
    
print('Média do Custo Total = ',np.mean(vCustoTotal))
print('Desvio-padrão do Custo Total = ',np.std(vCustoTotal))

#%% Questão 3 A

vCTMin = np.zeros(1000)
vLote = np.zeros(1000)
for t in range(0,1000):
    for i in range(0,len(vLote)):
        q = vLote[i]
        vCustoTotal[i] = fCustoTotal(q)
    vCTMin[t] = np.min(vCustoTotal)
    vLote[t] = vLote[np.argmin(vCustoTotal)]
    
#%% Questão 3 B
# Vetor dia (30 dias).
Dia = np.arange(1,31)

# Função de Cálculo das perdas.
def fCustoTotal(q):
   Lote = q
   Estoque = np.zeros(len(Dia))
   Estoque[0] = 0
   VendasPerdidas = 0
   CustoExcesso = 0
   CustoFrete = 0
   for t in range(0,len(Dia)):
       FreteSim = Dist*fPreçoSim(1)*fConsSim(1)
       Dem = np.random.normal(152,12)
       Estoque[t] = Estoque[t] + Lote
       if Estoque[t] <= Dem:
           VendasPerdidas = VendasPerdidas + Falta * (Dem - Estoque[t])
           Estoque[t] = 0
       else:
          Estoque[t] = Estoque[t] - Dem
   CustoExcesso = CustoExcesso + Excesso * Estoque[t]
   CustoFrete = CustoFrete + FreteSim
   CustoTotal = VendasPerdidas + CustoExcesso + CustoFrete
   return CustoTotal