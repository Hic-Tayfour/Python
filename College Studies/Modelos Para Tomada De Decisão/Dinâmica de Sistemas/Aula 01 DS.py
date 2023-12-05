"Problema da Empresa : O fim da picada"
"""
P      Qd      Qs
0,5    10       8
0,7     8      11

Qd = Quantidade demandada
Qs = Quantidade ofertada(supply)
P = Preço
"""
#a) 
"""
Escreva as equações da quantidade demandada(Qd) e da quantidade ofertada(Qs) em função do preço(P) do produto.  
Considere as quantidades demandas e ofertadas em termos de milhares de unidades.
Por simplicidade, considere que a quantidade demandada e ofertada sejam funções do primeiro grau do preço.
Qd=a1 - P*b1
Qs=a2 + P*b2

10=a1-0,5*b1 (L1)
8=a1-0,7*b1  (L2)

L1-L2 -> 2=0,2*b1 -> b1=10
10=a1-0,5*10 -> a1=15

Qd=15-10*P

8=a2+0,5*b2 (L3)
11=a2+0,7*b2 (L4)

L4-L3 -> 3=0,2*b2 -> b2=15
8=a2+0,5*15 -> a2=0,5

Qs=0,5+15*P

Qd=Qs

15-10*P=0,5+15*P
15=0,5+25*P
14,5=25*P
P=0,58

Qd=15-10*0,58
Qd=9,2

Qs=0,5+15*0,58
Qs=9,2
"""

#Vamos usar as ideias de equações diferenciais para realizar o estudo do preços

"""
dP/dt = 𝛾*(Qd-Qs)
Sendo 𝛾 uma constante a ser fixada por estimativas feitas pela empresa.
"""
"""
Nesse caso, vamos considerar que 𝛾=0,01
dP/dt = 0,01*(15-10*P-0,5-15*P)
dP/dt = 0,01*(14,5-25*P)
"""
"""
t   P    dP/dt
0  0,5   0,02
1  0,52  0,015
"""
#Vamos usar bibliotecas para resolver esse problema
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Definação das constantes
gama = 0.01

#Equação diferencial "É dificil mas é sempre igual"
def EqDif(Y,t):
    P = Y[0]
    Qd=15-10*P
    Qs=0.5+15*P  
    dPdt = gama*(Qd-Qs)
    return dPdt

#Rodando o odeint

t=np.arange(0,30,0.0001)

Y0= 0.5

Y05=odeint(EqDif,Y0,t)

# Gráfico.

plt.plot(t,Y05,'r')
plt.ylabel('Preço (R$)')
plt.xlabel('Tempo (dias)')
plt.title('Dinâmica de preços')
plt.show()


plt.figure()
Y0= 0.8

Y08=odeint(EqDif,Y0,t)

# Gráfico.

plt.plot(t,Y08,'r')
plt.ylabel('Preço (R$)')
plt.xlabel('Tempo (dias)')
plt.title('Dinâmica de preços')
plt.show()


