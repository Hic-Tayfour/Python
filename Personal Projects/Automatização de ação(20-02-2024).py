#Bibliotecas
import pandas as pd
import yfinance as web
import datetime as dt
import matplotlib.pyplot as fig
import statistics as st 
from math import log10
import scipy.stats as scy
import numpy as np


#Paramerização das Variáveis 
i=0
ações=[]
começo=input("inicio dos dados(yyyy-mm-dd) : ")
t=input("você deseja inserir uma data diferente da ultima cotação(responda sim ou não) ?")
if t=="sim" :
	fim=input("final dos dados(yyyy-mm-dd) : ")
else:
	fim=dt.datetime.now()
n=int(input("você deseja entrar com quantas ações ? : "))

#Uma Ação
if n==1:
    ações=input("entre com sua ação formato abcd1.sa : ")
    dados=web.download(ações,começo,fim)
    dados=dados.drop(['Adj Close','High','Low',], axis=1)
    dados['Retorno']=dados['Close'].pct_change(1)
    dados['OBV'] = (dados['Close'] - dados['Close'].shift(1)) * dados['Volume']
    dados['OBV'] = dados['OBV'].cumsum()
    dados['MedMovS']=dados['Close'].rolling(window=7).mean()

    
    #Gráficos 
    c=np.array(round(1+3.3*log10(len(dados)),0))
    fig.subplot(1,2,1)
    fig.hist(dados['Retorno'],bins=int(c),color='green',density=True)
    media=st.mean(dados['Retorno'][1:])
    desv_p=st.pstdev(dados['Retorno'][1:])
    xmin,xmax=fig.xlim()
    eixo_x=np.linspace(xmin,xmax,100)
    eixo_y=scy.norm.pdf(eixo_x,media,desv_p)
    fig.plot(eixo_x,eixo_y,color='black')    
    fig.subplot(1,2,2)
    fig.boxplot(dados['Retorno'][1:])
    fig.figure()
    scy.probplot(dados['Retorno'][1:],dist='norm',plot=fig)
else:
    dados = pd.DataFrame() 
    for i in range(n):
        ação = input("Entre com suas ações no padrão abcd1.sa : ")
        ações.append(ação.upper())
        dados_ação = web.download(ação, começo, fim)
        dados_ação = dados_ação.drop(['Adj Close', 'High', 'Low', 'Open'], axis=1)
        dados_ação['Retorno'] = dados_ação['Close'].pct_change(1)
        dados_ação['MedMovS'] = dados_ação['Close'].rolling(window=7).mean()
        dados_ação['OBV'] = (dados_ação['Close'] - dados_ação['Close'].shift(1)) * dados_ação['Volume']
        dados_ação['OBV'] = dados_ação['OBV'].cumsum()
        dados_ação.columns = pd.MultiIndex.from_tuples([(ação, 'Close'), (ação, 'Volume'), (ação, 'Retorno'), (ação, 'MedMovS'), (ação, 'OBV')])
        dados = pd.concat([dados, dados_ação], axis=1)

        # Gerar gráficos para cada ação após processá-los
        fig.figure(figsize=(14, 7))

        # Gráfico de linha para preços de fechamento
        fig.subplot(2, 2, 1)
        fig.plot(dados_ação[(ação, 'Close')], label='Preço de Fechamento')
        fig.title(f'Preço de Fechamento - {ação}')
        fig.xlabel('Data')
        fig.ylabel('Preço')
        fig.legend()

        # Gráfico de barras para volume
        fig.subplot(2, 2, 2)
        fig.bar(dados_ação.index, dados_ação[(ação, 'Volume')], color='orange')
        fig.title(f'Volume - {ação}')
        fig.xlabel('Data')
        fig.ylabel('Volume')

        # Histograma dos retornos
        fig.subplot(2, 2, 3)
        fig.hist(dados_ação[(ação, 'Retorno')].dropna(), bins=50, color='green', alpha=0.7)
        fig.title(f'Histograma de Retornos - {ação}')
        fig.xlabel('Retorno')
        fig.ylabel('Frequência')

        # Gráfico de probabilidade (QQ plot) para os retornos
        fig.subplot(2, 2, 4)
        scy.probplot(dados_ação[(ação, 'Retorno')].dropna(), dist="norm", plot=fig)
        fig.title(f'QQ Plot - {ação}')

        fig.tight_layout()
        fig.show()

    
#Salvar em Excel
p=input("você quer salvar essa esses dados em uma planilha de excel(responda sim ou não) ?")
if p=="sim":
    nome=input("Qual o nome da Planilha ?")
    dados.to_excel(nome+'.xlsx')

