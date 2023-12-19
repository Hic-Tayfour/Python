"""
Esse foi meu script de avaliação 4 do semestre 2 de 2023, ele não está completo, em especial na questão 1
, já em relação a questão 2, ele está completo é totalmente correto.
"""
"Questão 1"
#Importação de Bibliotecas 
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Calculo das Vazões
VRet=25.25
VRios=(1.98+2.55+35.65)
VInf=23.8
A=VRet+VRios+VInf
print("O volume total de vazão de abastecimento dos rios é de :",A,"m3/s")

#Calculo Abastecimento do Reservatório
Ta=VInf/A
Tb=VRet/A
Tc=VRios/A

# Arredondamento para duas casas decimais
Ta = round(Ta, 2)
Tb = round(Tb, 2)
Tc = round(Tc, 2)

# Impressão dos resultados
print("Ta =", Ta, ", Tb =", Tb, ", Tc =", Tc)

#Consumo de água
VTRAgr=11.25
VTRInd=10.90
VTRPop=23.38
RMSP=31.5
C=VTRAgr+VTRInd+VTRPop+RMSP
print("O volume total de consumo é de :",C,"m3/s")

Td=VTRAgr/A
Te=VTRInd/A
Tf=VTRPop/A
Tg=RMSP/A

# Arredondamento para duas casas decimais
Td = round(Td, 2)
Te = round(Te, 2)
Tf = round(Tf, 2)
Tg = round(Tg, 2)

# Impressão dos resultados
print("Td =", Td, ", Te =", Te, ", Tf =", Tf, ", Tg =", Tg)

#Dinâmica do Modelo

#Definição das constantes
V0=0.97*2.73
A=1*V0
C=0.85*V0

#Definição do sistema de equações diferenciais
def SisEqDif(Y,t):
    V=Y[0]
    dVdt=C-A
    return[dVdt]

#Determinação do intervalo de tempo
t=np.arange(0,10,0.0001)

#Estabelecendo as condições iniciais
Y=[V0]

#Rodando o odeint
Y=odeint(SisEqDif,V0,t)

# Encontrar o volume de água no reservatório ao final de 5 anos
V_5anos = Y[int(5/0.0001), 0]

# Arredondar para duas casas decimais
V_5anos = round(V_5anos, 2)

# Impressão do resultado
print("Volume de água no reservatório ao final de 5 anos: ", V_5anos, "bilhões de metros cúbicos.")

#Encontrar o volume de água no reservatório ao final de 10 anos
V_10anos = Y[int((10-0.0001)/0.0001), 0]

# Arredondar para duas casas decimais
V_10anos = round(V_10anos, 2)

# Impressão do resultado
print("Volume de água no reservatório ao final de 10 anos: ", V_10anos, "bilhões de metros cúbicos.")

# Definir o volume inicial do reservatório
V_inicial = 0.97*2.73

# Definir o volume crítico do reservatório
V_critico = 1500*5000000/1000000000


# Calcular o percentual do volume original que torna o abastecimento de água crítico
percentual_critico = (V_critico / V_inicial) * 100

# Arredondar para duas casas decimais
percentual_critico = round(percentual_critico, 2)

# Impressão do resultado
print("Percentual do volume original que torna o abastecimento de água crítico: ", percentual_critico, "%.")



"Questão 2"
#Modelo SIR para o mercado de ações

#Importação de Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Definição das constantes
N=110
Ic0=0.02*N
Iv0=0.02*N
Sc0=0.48*N
Sv0=0.48*N
P0=11
tmax=30
deltat=0.0001

a=3
b=1
alfa=1
beta=1
gama=0.03

#Definição do sistema de equações diferenciais
def SisEqDif(Y,t):
    Sc=Y[0]
    Sv=Y[1]
    Ic=Y[2]
    Iv=Y[3]
    P=Y[4]
    dIcdt=(a*Sc*Ic/N)-(b*Ic)
    dScdt=(beta*Iv)-(a*Sc*Ic/N)
    dIvdt=(alfa*Sv*Iv/N)-(beta*Iv)
    dSvdt=(b*Ic)-(alfa*Sv*Iv/N)
    dPdt=gama*(Ic-Iv)*P
    return[dScdt,dSvdt,dIcdt,dIvdt,dPdt]

#Determinação do intervalo de tempo
t=np.arange(0,tmax,deltat)

#Estabelecendo as condições iniciais
Y0=[Sc0,Sv0,Ic0,Iv0,P0]

#Rodando o odeint
Y=odeint(SisEqDif,Y0,t)

# Encontrar o preço do ativo após 5 e 10 dias de negociação
preco_5_dias = Y[int(5/deltat), 4]
preco_10_dias = Y[int(10/deltat), 4]
preco_30_dias = Y[int((tmax-deltat)/deltat), 4]

# Plotar o gráfico da dinâmica dos preços
plt.figure()
plt.plot(t, Y[:,4], label='P')
plt.legend()
plt.show()

# Encontrar a população máxima de infectados de compra
max_infectados_compra = int(max(Y[:,2]))

# Encontrar o dia em que ocorre o máximo de infectados de compra
dia_max_infectados_compra = int(t[np.argmax(Y[:,2])])

# Encontrar o número de pessoas suscetíveis à venda do ativo no final da simulação
pessoas_suscetiveis_venda_final = int(Y[-1,1])

# Imprimir os resultados
print(f"Preço do ativo após 5 dias de negociação: {preco_5_dias:.2f}")
print(f"Preço do ativo após 10 dias de negociação: {preco_10_dias:.2f}")
print(f"Preço do ativo após 30 dias de negociação: {preco_30_dias:.2f}")
print(f"População máxima de infectados de compra: {max_infectados_compra}")
print(f"Dia do máximo de infectados de compra: {dia_max_infectados_compra}")
print(f"Pessoas suscetíveis à venda do ativo no final da simulação: {pessoas_suscetiveis_venda_final}")




