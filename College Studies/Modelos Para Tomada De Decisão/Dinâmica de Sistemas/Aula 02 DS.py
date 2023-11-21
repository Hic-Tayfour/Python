"""
O Modelo Bass é um modelo matemático que descreve a difusão de inovações em um mercado. 
Ele foi proposto por Frank Bass em 1969 e é amplamente utilizado em estudos de marketing e previsão de vendas.

O modelo é baseado em duas componentes principais: a inovação externa e a inovação interna. 
A inovação externa representa a influência de fatores externos, como publicidade, 
mídia e recomendações de outras pessoas, na adoção de uma nova ideia ou produto. 
A inovação interna representa a influência de fatores internos, como a predisposição dos indivíduos para adotar uma nova ideia ou produto.

O modelo Bass é representado por duas equações diferenciais, uma para a taxa de adoção inicial e outra para a taxa de adoção cumulativa. 
A taxa de adoção inicial descreve a velocidade com que os indivíduos adotam a inovação em um determinado período de tempo, 
enquanto a taxa de adoção cumulativa descreve a proporção total de indivíduos que adotaram a inovação até o momento.

O modelo leva em consideração três parâmetros principais: o coeficiente de inovação externa, que mede a influência dos fatores 
externos na taxa de adoção; o coeficiente de inovação interna, que mede a influência dos fatores internos na taxa de adoção; 
e o tamanho do mercado potencial, que representa o número total de indivíduos que podem adotar a inovação.

O Modelo Bass é amplamente utilizado para prever a adoção de novos produtos ou ideias em um mercado, permitindo que as empresas ajustem suas 
estratégias de marketing e previsão de vendas com base nas características do mercado e nos parâmetros do modelo. 
Ele fornece uma estrutura teórica sólida para entender e prever a dinâmica de sistemas complexos de adoção de inovações.
"""
#Equações diferenciais 
"""
dP/dt=-AdProp-Abb ;(P=adotantes em potencial ;AdProp=adoção via propaganda, Abb=adoção via boca a boca)
dP/dt=-(a*P)-((i*c/N)*P*A) ;(a=Eficácia da propaganda; P=adotantes em potencial; i=Fração de adoção; c=taxa de contato; N=População Total; A=Adotantes) 
AdProp=a*P ;(a=Eficácia da propaganda; P=adotantes em potencial)
Abb=(i*c/N)*P*A ;(i=Fração de adoção; c=taxa de contato; N=População Total; A=Adotantes)

dA/dt=AdProp+Abb ;(A=Adotantes)
dA/dt=(a*P)+((i*c/N)*P*A)
AdProp=a*P
Abb=(i*c/N)*P*A

"""
# Importando as bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Deteminação das constantes
P0 = 4000000
A0 = 0 #Ninguém adotou o produto no início 
a = 0.01
i = 0.02
c = 10
N = 10000000

#Definição do sistema de equações diferenciais
def SisEqDif(Y,t):
    P=Y[0]
    A=Y[1] 
    dPdt = -a*P-(i*c/N)*P*A #Equação diferencial dos adotantes em potencial
    dAdt = a*P+(i*c/N)*P*A #Equação diferencial dos adotantes
    return [dPdt,dAdt]

#Definição do intervalo de tempo
T = np.arange(0,100,0.0001)

#Definição das condições iniciais
Y0=[P0,A0]

#Rodando o OdeInt
Y=odeint(SisEqDif,Y0,T)

#Plotando o gráfico
plt.plot(T,Y[:,0],'g',label='Adotantes em Potencial (P)')
plt.plot(T,Y[:,1],'r',label='Adotantes (A)')
plt.axis([0, max(T), 0, max(Y[0])])
plt.ylabel('População')
plt.xlabel('Tempo (dias)')
plt.title('Modelo de Bass')
plt.legend(labelspacing=0.8)
plt.show()

#Modelo Dinâmico do Duopólio 
"""
Duas firmas que fabricam o mesmo produto: pastilhas de freio para skates. 
Assumimos, neste modelo, que as duas firmas são as únicas que fabricam esse produto, 
de modo que pode ser utilizado o modelo dinâmico de duopólio.
O preço do produto é deixado regular pelo mercado e ele cai conforme a quantidade produzida de pastilhas de 
freio aumenta. Pesquisas de mercado indicam que o preço atual das pastilhas de freio é de 20 reais para uma
quantidade de 4 milhares de pastilhas fabricadas por mês e que, caso a produção dobrasse, o preço cairia para 15 reais.
"""

# Importação das bibliotecas.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definição do sistema de equações diferenciais.

def SisEqDif(Y,t):
    Q1=Y[0]
    Q2=Y[1]
    dQ1dt=-1*Q1-0.5*Q2+6
    dQ2dt=-0.5*Q1-1*Q2+6.4
    return [dQ1dt,dQ2dt]

# Rodando o odeint.

t=np.arange(0,12,1e-4)
Y0=[7,0]

Y=odeint(SisEqDif,Y0,t)

# Gráfico

plt.plot(t,Y[:,0],'g',label='Quantidade fabricada pela firma 1 (Q1)')
plt.plot(t,Y[:,1],'r',label='Quantidade fabricada pela firma 2 (Q2)')
plt.axis([0, max(t), 0, max(Y[0])])
plt.ylabel('Quantidade (milhares)')
plt.xlabel('Tempo (meses)')
plt.title(r'Modelo dinâmico de duopólio')
plt.legend(labelspacing=0.8)
plt.show()

# Quantidade de equilíbrio fabricada pela firma 1.
Q1eq=Y[-1,0]

# Quantidade de equilíbrio fabricada pela firma 2.
Q2eq= Y[-1,1]

# Preço de equilíbrio do produto.
P=25-1.25*(Q1eq+Q2eq)

