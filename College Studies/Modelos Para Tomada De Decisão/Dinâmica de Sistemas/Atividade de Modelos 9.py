"Questão 1"
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
S0=200000000
I0=1
R0=0
ti=0.2
tc=6
tr=0.7
N=200000000

# Definição do sistema de equações diferenciais.
def SisEqDif(Y,t):
    S=Y[0]
    I=Y[1]
    R=Y[2]
    dSdt=-1*(ti*tc/N)*S*I
    dIdt=(ti*tc/N)*S*I-tr*I
    dRdt=tr*I
    return[dSdt,dIdt,dRdt]

# Determinação do intervalo de tempo.
t=np.arange(0,100,1e-4)

# Estabelecendo as condições iniciais.
Y0=[S0,I0,R0]

# Rodando o odeint.
Y=odeint(SisEqDif,Y0,t)

# Gráfico.
plt.plot(t,Y[:,0],'g',label='População Suscetível (S)')
plt.plot(t,Y[:,1],'r',label='População Infectada (I)')
plt.plot(t,Y[:,2],'b',label='População Recuperada (R)')
plt.axis([0, max(t), 0, max(Y[0])])
plt.ylabel('População')
plt.xlabel('Tempo (dias)')
plt.title(r'Modelo SIR')
plt.legend(labelspacing=0.8)
plt.show()

# Respostas:
pop_suscetivel_100_dias = int(Y[-1, 0] / 1e6)
pop_recuperada_100_dias = int(Y[-1, 2] / 1e6)
pop_max_infectados = int(max(Y[:, 1]) / 1e6)
dia_pico_infectados = int(t[np.argmax(Y[:, 1])])

# Imprimindo as respostas
print("População suscetível após 100 dias:", pop_suscetivel_100_dias, "milhões")
print("População recuperada após 100 dias:", pop_recuperada_100_dias, "milhões")
print("População máxima de infectados:", pop_max_infectados, "milhões")
print("Dia do pico de infectados:", dia_pico_infectados)

"Questão 1 Parte A"
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
S0=200000000
I0=1
R0=0
ti=0.2
tc=8 #Nova Taxa de Infectados
tr=0.7
N=200000000

# Definição do sistema de equações diferenciais.
def SisEqDif(Y,t):
    S=Y[0]
    I=Y[1]
    R=Y[2]
    dSdt=-1*(ti*tc/N)*S*I
    dIdt=(ti*tc/N)*S*I-tr*I
    dRdt=tr*I
    return[dSdt,dIdt,dRdt]

# Determinação do intervalo de tempo.
t=np.arange(0,100,1e-4)

# Estabelecendo as condições iniciais.
Y0=[S0,I0,R0]

# Rodando o odeint.
Y=odeint(SisEqDif,Y0,t)

# Gráfico.
plt.plot(t,Y[:,0],'g',label='População Suscetível (S)')
plt.plot(t,Y[:,1],'r',label='População Infectada (I)')
plt.plot(t,Y[:,2],'b',label='População Recuperada (R)')
plt.axis([0, max(t), 0, max(Y[0])])
plt.ylabel('População')
plt.xlabel('Tempo (dias)')
plt.title(r'Modelo SIR')
plt.legend(labelspacing=0.8)
plt.show()

# Respostas:
pop_suscetivel_100_dias = int(Y[-1, 0] / 1e6)
pop_recuperada_100_dias = int(Y[-1, 2] / 1e6)
pop_max_infectados = int(max(Y[:, 1]) / 1e6)
dia_pico_infectados = int(t[np.argmax(Y[:, 1])])

# Imprimindo as respostas
print("População suscetível após 100 dias:", pop_suscetivel_100_dias, "milhões")
print("População recuperada após 100 dias:", pop_recuperada_100_dias, "milhões")
print("População máxima de infectados:", pop_max_infectados, "milhões")
print("Dia do pico de infectados:", dia_pico_infectados)

"Questão 1 Parte B"
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
N=200000000
S0=0.8*N
I0=1
R0=0
ti=0.2
tc=6
tr=0.7

# Definição do sistema de equações diferenciais.
def SisEqDif(Y,t):
    S=Y[0]
    I=Y[1]
    R=Y[2]
    dSdt=-1*(ti*tc/N)*S*I
    dIdt=(ti*tc/N)*S*I-tr*I
    dRdt=tr*I
    return[dSdt,dIdt,dRdt]

# Determinação do intervalo de tempo.
t=np.arange(0,100,1e-4)

# Estabelecendo as condições iniciais.
Y0=[S0,I0,R0]

# Rodando o odeint.
Y=odeint(SisEqDif,Y0,t)

# Gráfico.
plt.plot(t,Y[:,0],'g',label='População Suscetível (S)')
plt.plot(t,Y[:,1],'r',label='População Infectada (I)')
plt.plot(t,Y[:,2],'b',label='População Recuperada (R)')
plt.axis([0, max(t), 0, max(Y[0])])
plt.ylabel('População')
plt.xlabel('Tempo (dias)')
plt.title(r'Modelo SIR')
plt.legend(labelspacing=0.8)
plt.show()

# Respostas:
pop_suscetivel_100_dias = int(Y[-1, 0] / 1e6)
pop_recuperada_100_dias = int(Y[-1, 2] / 1e6)
pop_max_infectados = int(max(Y[:, 1]) / 1e6)
dia_pico_infectados = int(t[np.argmax(Y[:, 1])])

# Imprimindo as respostas
print("População suscetível após 100 dias:", pop_suscetivel_100_dias, "milhões")
print("População recuperada após 100 dias:", pop_recuperada_100_dias, "milhões")
print("População máxima de infectados:", pop_max_infectados, "milhões")
print("Dia do pico de infectados:", dia_pico_infectados)

"Questão 1 Parte C"
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
N=200000000
S0=0.3*N
I0=1
R0=0
ti=0.2
tc=6
tr=0.7

# Definição do sistema de equações diferenciais.
def SisEqDif(Y,t):
    S=Y[0]
    I=Y[1]
    R=Y[2]
    dSdt=-1*(ti*tc/N)*S*I
    dIdt=(ti*tc/N)*S*I-tr*I
    dRdt=tr*I
    return[dSdt,dIdt,dRdt]

# Determinação do intervalo de tempo.
t=np.arange(0,100,1e-4)

# Estabelecendo as condições iniciais.
Y0=[S0,I0,R0]

# Rodando o odeint.
Y=odeint(SisEqDif,Y0,t)

# Calculando a população suscetível após 100 dias e a população máxima de infectados.
pop_suscetivel_100_dias = int(Y[-1, 0] / 1e6)
pop_max_infectados = int(max(Y[:, 1]) / 1e6)

# Imprimindo as respostas.
print("Questão 1 Parte C")
print("População (milhões) suscetível ao final de 100 dias:", pop_suscetivel_100_dias)
print("População (milhões) máxima de infectados:", pop_max_infectados)

"Questão 2"
# Importação das bibliotecas.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Determinação das constantes.
S0=200000000
I0=1
R0=0
ti=0.2
tc=6
tr=0.7
tp=0.02
N=200000000

# Definição do sistema de equações diferenciais.
def SisEqDif(Y,t):
    S=Y[0]
    I=Y[1]
    R=Y[2]
    dSdt=-1*(ti*tc/N)*S*I+tp*R
    dIdt=(ti*tc/N)*S*I-tr*I
    dRdt=tr*I-tp*R
    return[dSdt,dIdt,dRdt]

# Determinação do intervalo de tempo.
t=np.arange(0,300,1e-4)

# Estabelecendo as condições iniciais.
Y0=[S0,I0,R0]

# Rodando o odeint.
Y=odeint(SisEqDif,Y0,t)

# Gráfico.
plt.plot(t,Y[:,0],'g',label='População Suscetível (S)')
plt.plot(t,Y[:,1],'r',label='População Infectada (I)')
plt.plot(t,Y[:,2],'b',label='População Recuperada (R)')
plt.axis([0, max(t), 0, max(Y[0])])
plt.ylabel('População')
plt.xlabel('Tempo (dias)')
plt.title(r'Modelo SIR')
plt.legend(labelspacing=0.8)
plt.show()

# Para os valores finais de S e R.
print('S final = {}'.format(int(np.round(Y[-1,0],-6) / 1e6)))
print('I final = {}'.format(int(np.round(Y[-1,1],-6) / 1e6)))
print('R final = {}'.format(int(np.round(Y[-1,2],-6) / 1e6)))

# Valor mínimo da população suscetível.
print('Mínimo da População Suscetível = {}'.format(int(np.round(np.min(Y[:,0]),-6) / 1e6)))
# Valor máximo da população infectada.
print('Máximo da População Infectada = {}'.format(int(np.round(np.max(Y[:,1]),-6) / 1e6)))
# Valor máximo da população recuperada.
print('Máximo da População recuperada = {}'.format(int(np.round(np.max(Y[:,2]),-6) / 1e6)))

# Dia do pico de infectados.
print('Dia do Pico de Infectados = ',np.round(t[np.argmax(Y[:,1])],0))

