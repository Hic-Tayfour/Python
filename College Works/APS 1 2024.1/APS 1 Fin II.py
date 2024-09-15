import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import numpy_financial as fin

# Importando Dados 
dados = pd.read_excel("carteira.xlsx", sheet_name = "Aba 2 - Tabela de Retorno")
Ret_IBOV = pd.read_excel("carteira.xlsx", sheet_name = "Aba 3 - Carteira de Mercado")

#Separando os Ativos 
Ret_IBOV = dados.iloc[:, 2]
Ret_Dolar= dados['Retorno Dólar']
Ret_BitCoin = dados['Retorno Bitcoin']
Ret_HGLG11 = dados['Retorno HGLG11']
Ret_MRFG3 = dados['Retorno  MRFG3']
Ret_JNJB34 = dados['Retorno JNJB34']
Ret_KLBN3 = dados['Retorno KLBN3']

#Tabela de Média e Desvio Padrão Dos Ret_Estat de Cada Ativo
Ret_Estat = pd.DataFrame()
Ret_Estat['Ret_IBOV'] = [Ret_IBOV.mean(), Ret_IBOV.std()]
Ret_Estat['Dolar'] = [Ret_Dolar.mean(), Ret_Dolar.std()]
Ret_Estat['Bitcoin'] = [Ret_BitCoin.mean(), Ret_BitCoin.std()]
Ret_Estat['HGLG11'] = [Ret_HGLG11.mean(), Ret_HGLG11.std()]
Ret_Estat['MRFG3'] = [Ret_MRFG3.mean(), Ret_MRFG3.std()]
Ret_Estat['JNJB34'] = [Ret_JNJB34.mean(), Ret_JNJB34.std()]
Ret_Estat.rename(index={0: 'Média', 1: 'Desvio Padrão'}, inplace=True)

#Tabela dos Ret_Estat por Ativo
Retornos = pd.DataFrame()
Retornos['IBOV'] = Ret_IBOV
Retornos['Dolar'] = Ret_Dolar
Retornos['Bitcoin'] = Ret_BitCoin
Retornos['HGLG11'] = Ret_HGLG11
Retornos['MRFG3'] = Ret_MRFG3
Retornos['JNJB34'] = Ret_JNJB34
Retornos['KLBN3'] = Ret_KLBN3
rf=0.009226

#Matriz de Covariância
Cov = Retornos.cov()

# Número de carteiras aleatórias para gerar
num_portfolios = 100000

# Número de dias 
dias = 21

# Lista para armazenar os pesos, retornos e volatilidades de cada carteira
resultados = np.zeros((2, num_portfolios))

# Remover IBOV dos retornos
Retornos = Retornos.drop(columns=['IBOV'])

pesos_otimos = None
sharpe_otimo = None

for i in range(num_portfolios):
    # Gerar pesos aleatórios
    pesos = np.random.random(len(Retornos.columns))
    pesos /= np.sum(pesos)
    
    # Calcular retorno e volatilidade
    retorno_carteira = np.sum(Retornos.mean() * pesos) * dias
    volatilidade_carteira = np.sqrt(np.dot(pesos.T, np.dot(Retornos.cov() * dias, pesos)))
    
    # Calcular o índice de Sharpe
    indice_sharpe = (retorno_carteira - rf) / volatilidade_carteira
    
    # Verificar se este índice de Sharpe é o maior até agora
    if sharpe_otimo is None or indice_sharpe > sharpe_otimo:
        sharpe_otimo = indice_sharpe
        pesos_otimos = pesos
    
    # Armazenar resultados
    resultados[0,i] = retorno_carteira
    resultados[1,i] = volatilidade_carteira

# Converter resultados em um DataFrame
resultados_frame = pd.DataFrame(resultados.T, columns=['retorno', 'volatilidade'])

# Plotar os dados em um gráfico de dispersão
plt.scatter(resultados_frame.volatilidade, resultados_frame.retorno, c=resultados_frame.volatilidade, cmap='RdYlGn')
plt.xlabel('Volatilidade (Desvio Padrão)')
plt.ylabel('Retorno Esperado (%)')
plt.title('Carteiras de Markowitz')

# Carteira Ótima
retorno_otimo = np.sum(Retornos.mean() * pesos_otimos) * dias
volatilidade_otima = np.sqrt(np.dot(pesos_otimos.T, np.dot(Retornos.cov() * dias, pesos_otimos)))

plt.scatter(volatilidade_otima, retorno_otimo, marker='.',color='black',s=100, label='Carteira Ótima')

# LAC
x = np.linspace(0, max(resultados_frame.volatilidade), 1000)
y = rf + x * (retorno_otimo - rf) / volatilidade_otima
plt.plot(x, y, color='black', linestyle='-', label = 'LAC')

plt.xlim([0, max(resultados_frame.volatilidade)])
plt.ylim([0, max(resultados_frame.retorno)])

plt.legend(labelspacing=0.8)
plt.colorbar(label='Volatilidade')
plt.show()

# Composição da Carteira Ótima
composicao_otima = pd.DataFrame({'Ativo': Retornos.columns, 'Peso': pesos_otimos})
print(composicao_otima)

# Cálculo do índice de Sharpe na carteira ótima
sharpe_otimo = (retorno_otimo - rf) / volatilidade_otima

print("Índice de Sharpe na carteira ótima:", sharpe_otimo)
