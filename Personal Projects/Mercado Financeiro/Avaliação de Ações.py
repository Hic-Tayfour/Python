from core import calcular_estatisticas_descritivas, salvar_em_excel, calcular_indicadores, gerar_graficos, baixar_dados_mercado, coletar_simbolos_acoes, definir_periodo_tempo

if __name__ == "__main__":
    # Definir o período de tempo
    começo, fim = definir_periodo_tempo()
    
    # Coletar símbolos das ações
    acoes = coletar_simbolos_acoes()
    
    # Baixar dados do mercado financeiro
    dados = baixar_dados_mercado(acoes, começo, fim)
    
    # Processar cada ação individualmente (exemplo para uma única ação)
    for acao in acoes:
        dados_acao = dados[dados['Symbol'] == acao]  # Filtra os dados para a ação atual
        
        # Calcular indicadores financeiros para a ação
        dados_indicadores = calcular_indicadores(dados_acao)
        
        # Gerar gráficos para a ação
        gerar_graficos(dados_indicadores, acao)
    
        # Calcular estatísticas descritivas (se aplicável a vários dados de ações, ajustar conforme necessário)
        estatisticas = calcular_estatisticas_descritivas(dados_indicadores[['Retorno']])
        print(estatisticas)
    
    # Opcional: Salvar os dados em uma planilha do Excel
    salvar_em_excel(dados, "dados_acoes.xlsx", "Dados Financeiros")
