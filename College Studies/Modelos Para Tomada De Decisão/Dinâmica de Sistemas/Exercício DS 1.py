"Questão 1"
#Importação das Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Fixação dos parâmetros

#Taxa de fertilidade líquida
k=0.013166

#População incial em 2020
P0=7795

#Definição da função com a equação diferencial
def EqDif(Y,t):
    P=Y[0] #5
    dPdt=k*P  #3
    return dPdt #14

#Definição do vetor de tempo
T=np.arange(2020,2050,1e-4) #8

#Resolução da equação diferencial
Y=odeint(EqDif,P0,T) #10

#Gráfico dos resultados
plt.plot(T,Y,'r')
plt.ylabel('População humana (milhões)')
plt.xlabel('Tempo (anos)')
plt.title('População humana no tempo')
plt.show()

anos = [2025, 2030, 2040, 2050]

for ano in anos:
    idx = np.abs(T - ano).argmin()
    pop = np.round(Y[idx])  # arredonda Y[idx]
    print(f'População em {ano}: {pop}')

"Questão 2"
#Importação das Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Fixação dos parâmetros

#Taxa de fertilidade líquida
k=0.013166

#População incial em 2020
P0=7795

#Definição da função com a equação diferencial
def EqDif(Y,t,beta):
    P=Y[0] 
    dPdt=k*P - beta*(P**2) 
    return dPdt 

#Definição do vetor de tempo
T=np.arange(2020,2050,1e-4) 

beta=np.array([0.0000001,0.0000005,0.0000015,0.0000020])

for i in range(len(beta)):
    Y=odeint(EqDif,P0,T,args=(beta[i],))
    idx = np.abs(T - 2050).argmin()
    pop = np.round(Y[idx])  # arredonda Y[idx]
    print(f'População em {ano}: {pop}')

plt.figure()    
plt.plot(T,Y,'r')
plt.ylabel('População humana (milhões)')
plt.xlabel('Tempo (anos)')
plt.title('População humana no tempo')
plt.show()



