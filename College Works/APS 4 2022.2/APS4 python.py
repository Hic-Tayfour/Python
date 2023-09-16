#Programa da aps4 
#Grupo 6
# Hicham Tayfour , João Jorge , Julia Aquino , Lucca Brinckmann
import yfinance as web
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as fig
dados=web.download("PETR4.SA","yahoo",start="2020-01-01",end="2022-12-31")

dados=dados.drop(['Adj Close'], axis=1)
dados['Retorno']=dados['Close'].pct_change(1)
dados.plot(y=['Close','Retorno'],style=['-o'],title=['Fechamento','Retorno'],subplots=True,grid=True)

x=np.arange(0,len(dados),1) 

dados['OBV']=0
dados['OBV'][1]=dados['Volume'][1]
for i in range(len(dados)):
    if dados['Close'][i+1]>dados['Close'][i]:
        dados['OBV'][i+1]=dados['OBV'][i]+dados['Volume'][i]
    elif dados['Close'][i+1]==dados['Close'][i]:
        dados['OBV'][i+1]=dados['OBV'][i]
    else:
        dados['OBV'][i+1]=dados['OBV'][i]-dados['Volume'][i]

print(dados)

coef_lin_Fec=np.polyfit(x,dados['Close'],1)
Ret_Fec=coef_lin_Fec[0]*x+coef_lin_Fec[1]
dados['Ret_Fec']=Ret_Fec.tolist()
coef_lin_OBV=np.polyfit(x,dados['OBV'],1)
Ret_OBV=coef_lin_OBV[0]*x+coef_lin_OBV[1]
dados['Ret_OBV']=Ret_OBV.tolist()
Grafico=fig.figure()
ax1=Grafico.add_subplot(211)
ax2=Grafico.add_subplot(212)
dados.plot(y=['Close','Ret_Fec'],grid=False,ax=ax1,title='Fechamento e tendência')
dados.plot(y=['OBV','Ret_OBV'],grid=False,ax=ax2,title='OBV e tendência')


dados['MedMov']=dados['Close'].rolling(window=7).mean()
dados.plot(y=['Close','MedMov'],style=['','--'],title='Fechamento e Média Móvel',grid=False)

fig.figure()
ax1=fig.subplot(121)
dados.plot(y=['Retorno'],grid=False,ax=ax1,title='Gráfico dos retornos')
fig.subplot(122)
sbn.distplot(dados['Retorno'],color='gray').set(title='Histograma')

print('############Estatísticas da Ação#############')
UltFec=dados['Close'].values[-1]
FecMax=dados['Close'].max()
FecMin=dados['Close'].min()
FecMed=dados['Close'].mean()
RetMax=(dados['Retorno'].max())*100
Dia_Ret_Max=dados['Retorno'].idxmax()
RetMin=(dados['Retorno'].min())*100
Dia_Ret_Min=dados['Retorno'].idxmin()
VolatFec=(dados['Close'].std(ddof=0))
VolatRet=(dados['Retorno'].std(ddof=0))*100
print('O ultimo fechamento foi ', UltFec )
print('O fechamento máximo foi de ', FecMax)
print('O fechamento mínimo foi de ', FecMin)
print('A média dos fechamentos foi de ', FecMed)
print('O retorno máximo foi de ', RetMax,'%')
print('O dia de retorno máximo foi de ',Dia_Ret_Max)
print('O retorno mínimo foi de ',RetMin,'%')
print('O dia de retorno mínimo foi de ',Dia_Ret_Min)
print('A volatilidade dos fechamentos deu',VolatFec)
print('A volatilidade dos retornos deu',VolatRet,'%')
print('#################################################')

dados=dados.drop(['Volume','Retorno','OBV','Ret_Fec','Ret_OBV','MedMov'], axis=1)
Graf_Duo,graf=fig.subplots()
ax2=dados.T.boxplot(color='Black')
graf.plot(dados['Close'].values)
ax2=fig.title('Boxplot dos fechamentos')
dados=fig.xticks(range(0,30,5))