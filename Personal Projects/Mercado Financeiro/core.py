import datetime as dt

def definir_periodo_tempo():
    """
    Solicita ao usuário as datas de início e fim para a análise.
    Retorna:
    começo (str): Data de início no formato 'yyyy-mm-dd'.
    fim (str): Data de fim no formato 'yyyy-mm-dd' ou a data atual se não especificada.
    """
    começo = input("Inicio dos dados (yyyy-mm-dd): ")
    t = input("Você deseja inserir uma data diferente da última cotação (responda sim ou não)? ")
    
    if t.lower() == "sim":
        fim = input("Final dos dados (yyyy-mm-dd): ")
    else:
        fim = dt.datetime.now().strftime('%Y-%m-%d')  # Converte a data atual para string no formato 'yyyy-mm-dd'
    
    return começo, fim


def coletar_simbolos_acoes():
    """
    Solicita ao usuário o número de ações que deseja inserir e, em seguida, coleta os símbolos de cada ação.
    
    Retorna:
    acoes (list): Lista contendo os símbolos de todas as ações inseridas pelo usuário.
    """
    acoes = []  # Inicializa uma lista vazia para armazenar os símbolos das ações
    n = int(input("Quantas ações você deseja analisar? Insira um número: "))
    
    for i in range(n):
        acao = input(f"Entre com o símbolo da ação {i+1} (exemplo: abcd4.sa): ")
        acoes.append(acao.upper())  # Adiciona o símbolo da ação à lista, convertendo para maiúsculas
    
    return acoes

import yfinance as yf
import pandas as pd

def baixar_dados_mercado(acoes, começo, fim):
    """
    Baixa os dados do mercado financeiro para uma lista de ações dentro de um período especificado.
    
    Parâmetros:
    acoes (list): Lista contendo os símbolos de ações para baixar os dados.
    começo (str): Data de início no formato 'yyyy-mm-dd'.
    fim (str): Data de fim no formato 'yyyy-mm-dd'.
    
    Retorna:
    dados (DataFrame): DataFrame do Pandas contendo os dados baixados para todas as ações.
    """
    dados = pd.DataFrame()
    for acao in acoes:
        dados_acao = yf.download(acao, start=começo, end=fim)
        dados_acao['Symbol'] = acao  # Adiciona uma coluna com o símbolo da ação para identificação
        if dados.empty:
            dados = dados_acao
        else:
            dados = pd.concat([dados, dados_acao], axis=0)
    
    return dados

import pandas as pd

def calcular_indicadores(dados):
    """
    Calcula indicadores financeiros para um DataFrame de ações.
    
    Parâmetros:
    dados (DataFrame): DataFrame contendo as colunas 'Close' e 'Volume' para cada ação.
    
    Retorna:
    DataFrame: O mesmo DataFrame com colunas adicionais para 'Retorno', 'OBV' e 'MedMovS'.
    """
    # Calcula o retorno diário das ações
    dados['Retorno'] = dados['Close'].pct_change(1)
    
    # Calcula o On-Balance Volume (OBV)
    obv = [0]
    for i in range(1, len(dados['Close'])):
        if dados['Close'][i] > dados['Close'][i-1]:
            obv.append(obv[-1] + dados['Volume'][i])
        elif dados['Close'][i] < dados['Close'][i-1]:
            obv.append(obv[-1] - dados['Volume'][i])
        else:
            obv.append(obv[-1])
    dados['OBV'] = obv
    
    # Calcula a média móvel simples de 7 dias para o preço de fechamento
    dados['MedMovS'] = dados['Close'].rolling(window=7).mean()
    
    return dados

import matplotlib.pyplot as plt
import scipy.stats as stats

def gerar_graficos(dados, simbolo):
    """
    Cria e exibe gráficos para análise de dados financeiros de uma ação específica.
    
    Parâmetros:
    dados (DataFrame): DataFrame contendo dados da ação, incluindo preço de fechamento ('Close'),
                       volume ('Volume'), retorno ('Retorno') e indicadores como OBV e médias móveis.
    simbolo (str): Símbolo da ação para título dos gráficos.
    """
    # Configuração para exibir múltiplos gráficos
    plt.figure(figsize=(14, 7))

    # Gráfico de linha para preços de fechamento
    plt.subplot(2, 2, 1)
    plt.plot(dados['Close'], label='Preço de Fechamento')
    plt.title(f'Preço de Fechamento - {simbolo}')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.legend()

    # Gráfico de barras para volume
    plt.subplot(2, 2, 2)
    plt.bar(dados.index, dados['Volume'], color='orange')
    plt.title(f'Volume - {simbolo}')
    plt.xlabel('Data')
    plt.ylabel('Volume')

    # Histograma dos retornos
    plt.subplot(2, 2, 3)
    plt.hist(dados['Retorno'].dropna(), bins=50, color='green', alpha=0.7)
    plt.title(f'Histograma de Retornos - {simbolo}')
    plt.xlabel('Retorno')
    plt.ylabel('Frequência')

    # Gráfico de probabilidade (QQ plot) para os retornos
    plt.subplot(2, 2, 4)
    stats.probplot(dados['Retorno'].dropna(), dist="norm", plot=plt)
    plt.title(f'QQ Plot - {simbolo}')

    plt.tight_layout()
    plt.show()

import pandas as pd

def calcular_estatisticas_descritivas(dados):
    """
    Calcula estatísticas descritivas para os retornos de cada ação no DataFrame.
    
    Parâmetros:
    dados (DataFrame): DataFrame contendo as colunas de retornos para cada ação.
    
    Retorna:
    estatisticas_df (DataFrame): DataFrame com as estatísticas descritivas de cada ação.
    """
    estatisticas = {
        'Ação': [],
        'Média': [],
        'Mediana': [],
        'Desvio Padrão': [],
        'Quartil 25%': [],
        'Quartil 75%': [],
        'Mínimo': [],
        'Máximo': [],
        'Variância': [],
        'Coef. de Variação (%)': []
    }

    for coluna in dados.columns:
        # Ignora colunas que não sejam de retornos
        if 'Retorno' not in coluna:
            continue
        
        estatisticas['Ação'].append(coluna)
        estatisticas['Média'].append(dados[coluna].mean())
        estatisticas['Mediana'].append(dados[coluna].median())
        estatisticas['Desvio Padrão'].append(dados[coluna].std())
        estatisticas['Quartil 25%'].append(dados[coluna].quantile(0.25))
        estatisticas['Quartil 75%'].append(dados[coluna].quantile(0.75))
        estatisticas['Mínimo'].append(dados[coluna].min())
        estatisticas['Máximo'].append(dados[coluna].max())
        estatisticas['Variância'].append(dados[coluna].var())
        coef_var = (dados[coluna].std() / dados[coluna].mean()) * 100 if dados[coluna].mean() != 0 else None
        estatisticas['Coef. de Variação (%)'].append(coef_var)
    
    estatisticas_df = pd.DataFrame(estatisticas)
    return estatisticas_df

def salvar_em_excel(dados, nome_arquivo, nome_aba='Sheet1'):
    """
    Salva o DataFrame em uma planilha do Excel.
    
    Parâmetros:
    dados (DataFrame): O DataFrame que você deseja salvar em uma planilha do Excel.
    nome_arquivo (str): O nome do arquivo (com caminho, se necessário) para salvar a planilha.
    nome_aba (str): Opcional. O nome da aba na planilha do Excel. Padrão é 'Sheet1'.
    """
    # Verifica se o nome do arquivo termina com a extensão .xlsx, se não, adiciona
    if not nome_arquivo.endswith('.xlsx'):
        nome_arquivo += '.xlsx'
    
    try:
        dados.to_excel(nome_arquivo, sheet_name=nome_aba)
        print(f'Dados salvos com sucesso em {nome_arquivo} na aba {nome_aba}.')
    except Exception as e:
        print(f'Ocorreu um erro ao salvar os dados: {e}')
