"Questão 1 " 
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
r=0.2
S0=200000
k=500000
tfinal=100
a=0.01
p=0.5
nu=0.0004
w=1200
E0=10

# Definição das equações diferenciais.
def SisEqDif(Y,t,H):
    S=Y[0]
    E=Y[1]
    dSdt=r*S-(r/k)*(S**2)-H
    dEdt=nu*p*a*E*S-nu*w*E
    return[dSdt,dEdt]

# Definição do intervalo de tempo.
t=np.arange(0,tfinal,1e-4)

# Definição do vetor de esforço de pesca.
H=np.array([0,10000,20000,25000])

# Condições iniciais do problema.
Y0=[S0,E0]

# Rodando o odeint.
Y=odeint(SisEqDif,Y0,t,args=(H[0],))

# Gráfico da população de peixes no tempo.
plt.figure()
plt.plot(t,Y[:,0],'g')
plt.axis([0, max(t),min(Y[:,0]),max(Y[:,0])])
plt.show()

# Gráfico do esforço por pescar no tempo.
plt.figure()
plt.plot(t,Y[:,1],'r')
plt.axis([0, max(t),min(Y[:,1]),max(Y[:,1])])
plt.show()

#Calculo dos peixeis em 24 meses.
for i in range(len(H)):
    Y = odeint(SisEqDif, Y0, t, args=(H[i],))
    idx = np.abs(t - 24).argmin()  # Encontra o índice mais próximo de 24
    pop = np.round(Y[idx, 0])  # Arredonda Y[idx]
    print(f'População de peixes em 24 meses com H = {H[i]}: {pop}')

# Determinação das constantes.
r=0.2
S0=200000
k=500000
tfinal=100
a=0.01
p=0.5
nu=0.0004
w=1200
E0=10

#Definindo as novas equações diferenciais.
def SisEqDif(Y,t):
    S=Y[0]
    E=Y[1]
    dSdt=r*S-(r/k)*(S**2)-a*E*S
    dEdt=nu*p*a*E*S-nu*w*E
    return[dSdt,dEdt]

t = np.linspace(0, 100, 1000)  # Simula por 100 meses

Y = odeint(SisEqDif, Y0, t)

# População de peixes ao final de 100 meses
pop_final = np.round(Y[-1, 0])
print(f'População de peixes ao final de 100 meses: {pop_final}')

# Esforço em pescar ao final de 100 meses
esforco_final = np.round(Y[-1, 1], 2)
print(f'Esforço em pescar ao final de 100 meses: {esforco_final}')

# População máxima de peixes ao longo dos 100 meses
pop_max = np.round(np.max(Y[:, 0]))
print(f'População máxima de peixes ao longo dos 100 meses: {pop_max}')

# População mínima de peixes ao longo dos 100 meses
pop_min = np.round(np.min(Y[:, 0]))
print(f'População mínima de peixes ao longo dos 100 meses: {pop_min}')

# Esforço máximo em pescar ao final de 100 meses
esforco_max = np.round(np.max(Y[:, 1]), 2)
print(f'Esforço máximo em pescar ao final de 100 meses: {esforco_max}')

# Esforço mínimo em pescar ao final de 100 meses
esforco_min = np.round(np.min(Y[:, 1]), 2)
print(f'Esforço mínimo em pescar ao final de 100 meses: {esforco_min}')

# Alterar o esforço inicial em pescar para 20
Y0 = [200000, 20]  # [população inicial de peixes, esforço inicial em pescar]

Y = odeint(SisEqDif, Y0, t)

# População de peixes ao final de 100 meses
pop_final = np.round(Y[-1, 0])
print(f'População de peixes ao final de 100 meses: {pop_final:}')

# Esforço em pescar ao final de 100 meses
esforco_final = np.round(Y[-1, 1], 2)
print(f'Esforço em pescar ao final de 100 meses: {esforco_final:.2f}')

"Questão 2"
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
a1=1.01
a2=1.03
b1=5.03
b2=5.02
gama=120
delta=110
RA0=100
RB0=150
tfinal=100

# Definição das equações diferenciais.
def SisEqDif(Y,t):
    RA=Y[0]
    RB=Y[1]
    dRAdt=gama*(a2-a1+b2*np.arctan(RB)-b1*np.arctan(RA))
    dRBdt=delta*(a1-a2+b1*np.arctan(RA)-b2*np.arctan(RB))
    return[dRAdt,dRBdt]

# Rodando o odeint.
t=np.arange(0,tfinal,1e-4)
Y0=[RA0,RB0]
Y=odeint(SisEqDif,Y0,t)

# Gráfico.
plt.plot(t,Y[:,0],'r')
plt.plot(t,Y[:,1],'b')
plt.axis([0, max(t),75,175])
plt.show()

# Obtenção dos valores finais de RA e RB.
# Obtenção dos valores finais de RA e RB.
RA_final = round(Y[-1, 0])
RB_final = round(Y[-1, 1])

print(f"Investimento da SpaceX ao final de 100 meses: {RA_final}")
print(f"Investimento da Blue Origins ao final de 100 meses: {RB_final}")