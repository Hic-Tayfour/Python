#%% Questão 1 A

# Importação de bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Vetor demanda. Em cestas básicas por semana.
Demanda = np.array([20,25,22,45])

# Frete.Em R$ (preço do combustível da caminhonete).
Frete = 45

# Custo unitário de estocagem. Em R$ por semana.
CustoUniEst = 0.5

# Lote econômico.
q=np.sqrt(2*Frete*np.mean(Demanda)/CustoUniEst)
print('Lote Econômico =',q)

# Quantidade de compras a serem feitas por ano.
d = np.mean(Demanda)*52
n = d/q
print('Número de Viagens por Ano =',n)
     
#%% Questão 1 B

# Função que calcula as demandas simuladas.
def fDemanda(q):
    vDemanda = np.zeros(q)
    for t in range(0,q):
        Aleat = np.random.uniform(0,1)
        if Aleat <= 0.75:
            vDemanda[t] = 24
        else:
            vDemanda[t] = 45
    return vDemanda

# Função que calcula os fretes simulados.
def fFrete(q):
    vFrete = np.random.normal(45,5,q)
    return vFrete

# Cálculo do Lote Econômico.
# Número de Simulações.
Num = 1000
vLoteEconomico = np.sqrt(2*fFrete(Num)*fDemanda(Num)/CustoUniEst)
print('Média do Lote Econômico = ',np.mean(vLoteEconomico))
print('Desvio-padrão do Lote Econômico = ',np.std(vLoteEconomico))

#%% Questão 2 A

# Importação de bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Vetor demanda. Em cestas básicas por semana.
Demanda = np.array([20,25,22,45])

# Frete.Em R$ (preço do combustível da caminhonete).
Frete = 30

# Custo unitário de estocagem. Em R$ por semana.
CustoUniEst = 0.5

# Definição do vetor Semana.
Semana = np.arange(1,53)

# Cálculo da Demanda Média.
DemandaMédia = np.round(np.mean(Demanda))

# Lote. Quantidade de cestas básicas.
Lote = 112

# "Venda Perdida" por cesta básica não entregue.
VP = 60

# Simulação do estoque por semana e cálculo dos custos.
Estoque = np.zeros(len(Semana))
Estoque[0] = Lote
CFrete = Frete
VendasPerdidas = 0
CEstoque = Lote * CustoUniEst
for t in range(1,len(Semana)):
    Estoque[t] = Estoque[t-1] - DemandaMédia
    if t%4 == 0:
        Estoque[t] = Estoque[t] + Lote
        CFrete = CFrete + Frete
        if Estoque[t] >= 0:
            CEstoque = CEstoque + Estoque[t] * CustoUniEst
        else:
            Estoque[t] = 0
        if Estoque[t] < DemandaMédia:
            VendasPerdidas = VendasPerdidas + VP * (DemandaMédia - Estoque[t])
CTotal = CEstoque + CFrete + VendasPerdidas
    
print('Custo de Estoque = ',CEstoque)
print('Custo de Frete = ',CFrete)
print('Vendas Perdidas = ',VendasPerdidas)
print('Custo Total = ',CTotal)
plt.bar(Semana,Estoque,color='green')

#%% Questão 2 B

# Importação de bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Vetor demanda. Em cestas básicas por semana.
Demanda = np.array([20,25,22,45])

# Frete.Em R$ (preço do combustível da caminhonete).
Frete = 30

# Custo unitário de estocagem. Em R$ por semana.
CustoUniEst = 0.5

# Simulação de perdas com estocagem frete e vendas perdidas em demandas semanais.
Lote = 111

# "Venda Perdida" por cesta básica não entregue.
VP = 60

# Simulação do estoque por semana e cálculo dos custos.
Estoque = np.zeros(len(Semana))
Estoque[0] = Lote
CFrete = Frete
VendasPerdidas = 0
CEstoque = Lote * CustoUniEst
DemandaDaSemana = 0
for t in range(1,len(Semana)):
    if t%4 == 1:
        DemandaDaSemana = Demanda[0]
    elif t%4 == 2:
        DemandaDaSemana = Demanda[1]
    elif t%4 == 3:
        DemandaDaSemana = Demanda[2]
    elif t%4 == 0:
        DemandaDaSemana = Demanda[3]
    Estoque[t] = Estoque[t-1] - DemandaDaSemana
    if t%4 == 0:
        Estoque[t] = Estoque[t] + Lote
        CFrete = CFrete + Frete
    if Estoque[t] >= 0:
        CEstoque = CEstoque + Estoque[t] * CustoUniEst
    else:
        Estoque[t] = 0
    if Estoque[t] < DemandaDaSemana:
        VendasPerdidas = VendasPerdidas + VP * (DemandaDaSemana - Estoque[t])

CTotal = CEstoque + CFrete + VendasPerdidas
print('Custo de Estoque = ',CEstoque)
print('Custo de Frete = ',CFrete)
print('Vendas Perdidas = ',VendasPerdidas)
print('Custo Total = ',CTotal)
plt.bar(Semana,Estoque,color='green')

#%% Questão 3 A

# Importação de bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Vetor demanda. Em cestas básicas por semana.
Demanda = np.array([20,25,22,45])

# Frete.Em R$ (preço do combustível da caminhonete).
Frete = 45

# Custo unitário de estocagem. Em R$ por semana.
CustoUniEst = 0.5

# Definição do vetor Semana.
Semana = np.arange(1,53)

# "Venda Perdida" por cesta básica não entregue.
VP = 60

# Simulação do estoque por semana e cálculo dos custos.
# Definição da função custo total.
def fCTotal(q):
    Estoque = np.zeros(len(Semana))
    Estoque[0] = q
    CFrete = Frete
    VendasPerdidas = 0
    CEstoque = q * CustoUniEst
    DemandaDaSemana = 0
    for t in range(1,len(Semana)):
        if t%4 == 1:
            DemandaDaSemana = Demanda[0]
        elif t%4 == 2:
            DemandaDaSemana = Demanda[1]
        elif t%4 == 3:
            DemandaDaSemana = Demanda[2]
        elif t%4 == 0:
            DemandaDaSemana = Demanda[3]
        Estoque[t] = Estoque[t-1] - DemandaDaSemana
        if t%4 == 0:
            Estoque[t] = Estoque[t] + q
            CFrete = CFrete + Frete
        if Estoque[t] >= 0:
            CEstoque = CEstoque + Estoque[t] * CustoUniEst
        else:
            Estoque[t] = 0
        if Estoque[t] < DemandaDaSemana:
            VendasPerdidas = VendasPerdidas + VP * (DemandaDaSemana - Estoque[t])
    CTotal = CEstoque + CFrete + VendasPerdidas
    return CTotal

vLote = np.arange(100,151)
vCTotal = np.zeros(len(vLote))

for i in range(0,len(vLote)):
    q = vLote[i]
    vCTotal[i] = fCTotal(q)
plt.plot(vLote,vCTotal)

print('Custo Total Mínimo = ',np.min(vCTotal))
print('Lote Econômico = ',vLote[np.argmin(vCTotal)])
print('Média do Vetor Custo Total = ',np.mean(vCTotal))
print('Desvio-padrão do Vetor Custo Total = ',np.std(vCTotal))
print('Média do Vetor Lote Econômico = ',np.mean(vLote))
print('Desvio-padrão do Vetor Lote Econômico = ',np.std(vLote))

#%% Questão 3 B

# Importação de bibliotecas.
import numpy as np
import matplotlib.pyplot as plt

# Vetor demanda. Em cestas básicas por semana.
Demanda = np.array([20,25,22,45])

# Frete.Em R$ (preço do combustível da caminhonete).
Frete = 45

# Custo unitário de estocagem. Em R$ por semana.
CustoUniEst = 0.5

# Definição do vetor Semana.
Semana = np.arange(1,53)

# "Venda Perdida" por cesta básica não entregue.# Simulação do estoque por semana e cálculo dos custos.
VP = 60
# Simulação do estoque por semana e cálculo dos custos.
# Definição da função custo total.
def fCTotal(q):
    Estoque = np.zeros(len(Semana))
    Estoque[0] = q
    CFrete = Frete
    VendasPerdidas = 0
    CEstoque = q * CustoUniEst
    DemandaDaSemana = 0
    for t in range(1,len(Semana)):
        if t%4 == 1:
            DemandaDaSemana = Demanda[0]
        elif t%4 == 2:
            DemandaDaSemana = Demanda[1]
        elif t%4 == 3:
            DemandaDaSemana = Demanda[2]
        elif t%4 == 0:
            DemandaDaSemana = Demanda[3]
        Estoque[t] = Estoque[t-1] - DemandaDaSemana
        if t%4 == 0:
            Estoque[t] = Estoque[t] + q
            CFrete = CFrete + Frete
        if Estoque[t] >= 0:
            CEstoque = CEstoque + Estoque[t] * CustoUniEst
        else:
            Estoque[t] = 0
        if Estoque[t] < DemandaDaSemana:
            VendasPerdidas = VendasPerdidas + VP * (DemandaDaSemana - Estoque[t])
    CTotal = CEstoque + CFrete + VendasPerdidas
    return CTotal

# Função custo mínimo e lote econômico
def fCustoMin(n):
    CustoMínimo = np.zeros(n)
    LoteEconômico = np.zeros(n)
    for s in range(0,n):
        vLote = np.arange(100,151)
        vCTotal = np.zeros(len(vLote))
        for i in range(0,len(vLote)):
            q = vLote[i]
            vCTotal[i] = fCTotal(q)
            CustoMínimo[s] = np.min(vCTotal)
    return CustoMínimo

# Função custo mínimo e lote econômico

def fLoteEcon(n):
    CustoMínimo = np.zeros(n)
    LoteEconômico = np.zeros(n)
    for s in range(0,n):
        vLote = np.arange(100,151)
        vCTotal = np.zeros(len(vLote))
        for i in range(0,len(vLote)):
            q = vLote[i]
            vCTotal[i] = fCTotal(q)
            LoteEconômico[s] = vLote[np.argmin(vCTotal)]
    return LoteEconômico

# Simulação.

Num = 100
vCustoMínimo = fCustoMin(Num)
vLoteEconômico = fLoteEcon(Num)

print('Média do Custo Mínimo Simulado = ',np.mean(vCustoMínimo))
print('Desvio-padrão do Custo Mínimo Simulado = ',np.std(vCustoMínimo))
print('Média do Lote Econômico Simulado = ',np.mean(vLoteEconômico))
print('Desvio-padrão do Lote Econômico Simulado = ',np.std(vLoteEconômico))

