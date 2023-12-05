"Questão 1"

# Importação de bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constantes.
S0=2000000
I0=100
ti=0.1
tc=6
tr=0.2
N=2000000

# Sistema de equações diferenciais.
def SisEqDif(Y,t):
    S=Y[0]
    I=Y[1]
    dSdt=-1*(ti*tc/N)*S*I+tr*I
    dIdt=(ti*tc/N)*S*I-tr*I
    return[dSdt,dIdt]

# Rodando o odeint.
t=np.arange(0,60,1e-4)
Y0=[S0,I0]
Y=odeint(SisEqDif,Y0,t)

# Gráfico.
plt.plot(t,Y[:,0],'g',label='População Suscetível (S)')
plt.plot(t,Y[:,1],'r',label='População Infectada (I)')
plt.axis([0, max(t), 0, max(Y[0])])
plt.ylabel('População')
plt.xlabel('Tempo (dias)')

plt.title(r'Modelo SIS')
plt.legend(labelspacing=0.8)
plt.show()

idx = np.abs(t - 60).argmin()
pop = np.round(Y[idx]) 
print(f'População em {60}: {pop}')

# Calculando o módulo da diferença entre a população suscetível e a população infectada.
Z=abs(Y[:,0]-Y[:,1])

# Tempo em que esse módulo de diferenças atinge o valor mínimo. (A igualdade entre a População Suscetível e a População Infectada)
t[np.argmin(Z)]

print(np.round(t[np.argmin(Z)],0))

"Questão 2"
# Importação das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
lambida=0.013382
delta=0.1
s=0.15
A=0.3
alfa=0.6

# Condições iniciais.
L0=3386
K0=0.05*91

# Definiçãos das equações diferenciais.

def SisEqDif(Y,t):
    L=Y[0]
    K=Y[1]
    dLdt=lambida*L
    dKdt=-delta*K+s*A*(K**alfa)*(L**(1-alfa))
    return[dLdt,dKdt]

# Determinação do tempo.
t=np.arange(2020,2100,1e-4)

# Determinação das condições iniciais.
Y0=[L0,K0]

# Rodando o odeint.
Y=odeint(SisEqDif,Y0,t)

# Gráfico.
plt.plot(t,Y[:,0],'g',label='Trabalho (L)')
plt.plot(t,Y[:,1],'r',label='Capital (K)')

#plt.axis([0, max(t), 0, max(Y[0])])
plt.ylabel('L e K')
plt.xlabel('Tempo (anos)')
plt.title(r'Modelo de Solow-Swan')
plt.legend(labelspacing=0.8)
plt.show()

idx = np.abs(t - 2100).argmin()
pop = np.round(Y[idx]) 
print(f'População em {2100}: {pop}')

print(f'Trabalho (L) previsto para 2100 (milhões): {int(round(pop[0]))}')
print(f'Capital (K) previsto para 2100 (trilhões): {int(round(pop[1]))}')

capital_per_capita = pop[1] / pop[0]
print(f'Capital per capita previsto para 2100: {capital_per_capita:.3f}'.replace('.', ','))

# Para s = 0.1
s = 0.1
Y = odeint(SisEqDif, Y0, t)
idx = np.abs(t - 2100).argmin()
pop = Y[idx]
capital_per_capita = pop[1] / pop[0]
print(f'Capital per capita previsto para 2100 (para s=0,1): {capital_per_capita:.3f}'.replace('.', ','))

# Para s = 0.2
s = 0.2
Y = odeint(SisEqDif, Y0, t)
idx = np.abs(t - 2100).argmin()
pop = Y[idx]
capital_per_capita = pop[1] / pop[0]
print(f'Capital per capita previsto para 2100 (para s=0,2): {capital_per_capita:.3f}'.replace('.', ','))
