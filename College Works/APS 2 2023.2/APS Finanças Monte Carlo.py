#%%Sobre este Trabalho
"""
Este trabalho se trata do APS de Finanças I, em que simularemos o
VPL de um projeto, mas usaremos do Python para realizar a Simulação de
Monte Carlo para avaliar a viabilidade da realização do projeto.
"""

#Integrantes
"""
Beatriz Emi Ueda (beatrizeu@al.insper.edu.br),  
Beatriz Fernandes da Silva (beatrizfs1@al.insper.edu.br),  
Gabriela Abib (gabrielaa6@al.insper.edu.br),  
Hicham Munir Tayfour (hichamt@al.insper.edu.br),  
Júlia de Aquino Rocha (juliaar1@al.insper.edu.br),  
Raynnara Silva de Freitas Gurgel (raynnarasf@al.insper.edu.br).  
"""

#Empresa escolhida: Camil (CAML3.SA)

#%% Bilbliotecas à serem usadas para a simulação de Monte Carlo
import numpy_financial as fin
import numpy as np
import matplotlib.pyplot as fig
from scipy.stats import norm

#%% Simulação de Monte Carlo

#Premissas
"""
Vamos adotar a distribuição normal e uniforme como padrão da simulação, onde a normal será usada 
para grande parte da simulação.
Projeto Terá uma Duração de 5 anos
"""

#Variaveis e Simulção
Simulações=int(100000)
VPL=np.zeros(Simulações)
TIR=np.zeros(Simulações)

"Variáveis Fixas"
Taxa_Depreciação=float(0.2)
Taxa_CMV=float(0.79)
TMA=float(0.2)
Taxa_CCL=float(0.05)
IR=float(0.34)

"Variáveis a Serem Simuladas"
MediaInvestimento=int(113669650)
DesvioInvestimento=int(2500000)
MediaQuantidade=int(25360000)
DesvioQuantidade=int(50000)
MediaPrecoUnitario=float(7.70)
DesvioPrecoUnitario=float(1.50)

"Simulação"
for i in range(Simulações):
    #Distribuição das Variáveis Aleatórias 
    Investimento=round(np.random.normal(MediaInvestimento,DesvioInvestimento),2)
    Quantidade=round(np.random.normal(MediaQuantidade,DesvioQuantidade),2)
    Preco=round(np.random.normal(MediaPrecoUnitario,DesvioPrecoUnitario),2)
    #Montagem do Fluxo De Caixa 
    Receita=Quantidade*Preco
    CMV=Taxa_CMV*Receita
    Depreciação=Taxa_Depreciação*Investimento
    LAJIR=Receita-(CMV+Depreciação)
    Imposto=LAJIR*IR
    NOPAT=LAJIR-Imposto
    FCO=NOPAT+Depreciação
    CCL=Investimento*Taxa_CCL
    FxCx0=-(Investimento+CCL)
    FxCx5=FCO+CCL
    FxCxProjeto=np.array([FxCx0,FCO,FCO,FCO,FCO,FxCx5])
    VPL[i]=fin.npv(TMA,FxCxProjeto)
    TIR[i]=fin.irr(FxCxProjeto)

#Quais os Projetos Viáveis (VPL>0)
Realizavel=VPL[VPL>0]
NumRealizaveis=len(Realizavel)

ProbabilidadeRealizável=round(100*(NumRealizaveis/Simulações),2)
print("A probabilidade da empresa realizar o projeto ,ou seja, o projeto possuir um VPL maior que zero é de  ",ProbabilidadeRealizável,"%")


#Representções Gráficas do VPL e da TIR
# Histograma dos VPL's
fig.figure()
fig.hist(VPL, bins=1000, color='green', density=True)
mu, std = norm.fit(VPL)
xmin, xmax = fig.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
fig.plot(x, p, 'k', linewidth=2)
fig.title("Histograma dos VPL's")
fig.xlabel("Valores do VPL")
fig.ylabel("Densidade")

# Histograma das TIR's
fig.figure()
fig.hist(TIR, bins=1000, color='green', density=True)
mu, std = norm.fit(TIR)
xmin, xmax = fig.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
fig.plot(x, p, 'k', linewidth=2)
fig.title("Histograma das TIR's")
fig.xlabel("Valores do TIR's")
fig.ylabel("Densidade")

    
    