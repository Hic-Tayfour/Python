<<<<<<< HEAD
#%% Importações
import numpy as np 
import pandas as pd
from plotnine import *

#%% Simulação de Dados das Opções
df_opcoes_euro = pd.DataFrame({
    'Tipo de Opção': ["call", "call", "put"],
    'Opção': ["Call VOW 11 C95", "Call VOW 12 C98", "Put VOW 12 P94"],
    'Data de Vencimento': ["15-11-2024", "20-12-2024", "20-12-2024"],
    'Strike': [95, 98, 94],
    'Prêmio': [5.10, 4.80, 3.9],
    'Vencimento (em dias)': [43, 78, 78]
})

E_ue = 1.1036
PVOW_euro = 96.55
PVOW_dolar = PVOW_euro / E_ue

df_opcoes_dolar = pd.DataFrame({
    'Tipo de Opção': ["call", "call", "put"],
    'Opção': ["Call VOW 11 C95", "Call VOW 12 C98", "Put VOW 12 P94"],
    'Data de Vencimento': ["15-11-2024", "20-12-2024", "20-12-2024"],
    'Strike': df_opcoes_euro['Strike'] / E_ue,
    'Prêmio': df_opcoes_euro['Prêmio'] / E_ue,
    'Vencimento (em dias)': [43, 78, 78]
})

df_opcoes_euro  
df_opcoes_dolar
#%% Letra B

preco_exercicio_put = 1.1000  
valor_put_eur = 0.030  
exposicao_vendas_eur = 40529  

exposicao_vendas_usd = exposicao_vendas_eur / E_ue

numero_opcoes = exposicao_vendas_usd / preco_exercicio_put 

print(f"A Porsche precisaria comprar {numero_opcoes:.2f} opções de venda (puts) para realizar o hedge completo em dólares.")
#%% Letra C

option_type = input("Digite o tipo de opção (call/put): ").lower()
strike_price = float(input("Digite o preço de exercício: "))
option_price = float(input("Digite o valor da opção: "))
contracts = int(input("Digite o número de contratos: "))

prices = np.linspace(0.8 * strike_price, 1.2 * strike_price, 100)

if option_type == 'put':
    payoff = np.maximum(prices - strike_price, 0)
elif option_type == 'call':
    payoff = np.maximum(strike_price - prices, 0)
else:
    raise ValueError("Tipo de opção inválido. Use 'call' ou 'put'.")

resultado = (payoff - option_price) * contracts
ret = resultado/PVOW_euro

df = pd.DataFrame({
    'Payoff' : payoff * contracts,
    'Preço_Ativo': prices,
    'Resultado': resultado,
    'Retorno' : ret

})

df

plot = (
    ggplot(df, aes(x='Preço_Ativo')) +
        geom_line(aes(y='Resultado'), color="blue", size=1.2, linetype="dotted") +  
        geom_line(aes(y='Payoff'), color="red", size=1.2) +  
        geom_hline(yintercept=0, linetype="dashed", color="black") +
    labs(
        title="Resultado e Payoff da Estratégia de Opções",
        subtitle="Análise de Calls e Puts em USD Ponderada pelos Contratos",
        x="Preço do Ativo Subjacente (St)",
        y="Resultado e Payoff",
        caption="Fonte: Bloomberg"
    ) +
    theme_minimal() +
    theme(
        plot_title=element_text(size=16, weight='bold', ha='center'),
        plot_subtitle=element_text(size=12, ha='center'),
        axis_title_x=element_text(size=10),
        axis_title_y=element_text(size=10),
        axis_text=element_text(size=9),
        plot_caption=element_text(size=8, ha='right', style='italic'),
        figure_size=(8, 5)
    )
)

print(plot)


#%% Letra D1

for index, row in df_opcoes_dolar.iterrows():
    tipo = row['Tipo de Opção']
    strike_price = row['Strike']
    option_price = row['Prêmio']
    nome_opcao = row['Opção']

    prices = np.linspace(0.8 * strike_price, 1.2 * strike_price, 100)

    if tipo == 'put':
        payoff = np.maximum(prices - strike_price, 0)
    elif tipo == 'call':
        payoff = np.maximum(strike_price - prices, 0)
    else:
        raise ValueError("Tipo de opção inválido. Use 'call' ou 'put'.")

    resultado = (payoff - option_price)

    
    df_resultado = pd.DataFrame({
        'Payoff': payoff,
        'Preço_Ativo': prices,
        'Resultado': resultado
    })


    plot = (
        ggplot(df_resultado, aes(x='Preço_Ativo')) +
        geom_line(aes(y='Resultado'), color="red", size=1.2, linetype="dotted") +  
        geom_line(aes(y='Payoff'), color="blue", size=1.2) +  
        geom_hline(yintercept=0, linetype="dashed", color="black") +
        labs(
            title="Payoff da Estratégia de Opções",
            subtitle=f"Análise de {nome_opcao}",
            x="Preço do Ativo Subjacente (St)",
            y="Payoff e Resultado",
            caption="Fonte: Bloomberg"
        ) +
        theme_minimal() +
        theme(
            plot_title=element_text(size=16, weight='bold', ha='center'),
            plot_subtitle=element_text(size=12, ha='center'),
            axis_title_x=element_text(size=10),
            axis_title_y=element_text(size=10),
            axis_text=element_text(size=9),
            plot_caption=element_text(size=8, ha='right', style='italic'),
            figure_size=(8, 5)
        )
    )

    print(plot)
    print(df_resultado)

#%% Letra D2

prices = np.linspace(0.8 * preco_exercicio_put, 1.2 * preco_exercicio_put, 100)

payoff = np.maximum(preco_exercicio_put - prices, 0)

resultado = (payoff - valor_put_eur) * numero_opcoes

df_resultado = pd.DataFrame({
    'Payoff' : payoff * numero_opcoes,
    'Preço do Ativo (St)': prices,
    'Payoff da Estratégia': resultado
})

plot = (
    ggplot(df, aes(x='Preço_Ativo')) +
        geom_line(aes(y='Resultado'), color="blue", size=1.2, linetype="dotted") +  
        geom_line(aes(y='Payoff'), color="red", size=1.2) +  
    geom_hline(yintercept=0, linetype="dashed", color="black") +
    labs(
        title="Payoff e Resultado da Estratégia de Opções FX",
        subtitle="Put de Dólar OTC (1 ano, Strike: 1.1000 EUR/USD)",
        x="Preço do Dólar no Vencimento (St)",
        y="Resultado (€)",
        caption="Fonte: Bloomberg"
    ) +
    theme_minimal() +
    theme(
        plot_title=element_text(size=16, weight='bold', ha='center'),
        plot_subtitle=element_text(size=12, ha='center'),
        axis_title_x=element_text(size=10),
        axis_title_y=element_text(size=10),
        axis_text=element_text(size=9),
        plot_caption=element_text(size=8, ha='right', style='italic'),
        figure_size=(8, 5)
    )
)

print(f"Exposição em dólares: USD {exposicao_vendas_usd}")
print(df_resultado)
print(plot)
# %%
=======
#%% Importações
import numpy as np 
import pandas as pd
from plotnine import *

#%% Simulação de Dados das Opções
df_opcoes_euro = pd.DataFrame({
    'Tipo de Opção': ["call", "call", "put"],
    'Opção': ["Call VOW 11 C95", "Call VOW 12 C98", "Put VOW 12 P94"],
    'Data de Vencimento': ["15-11-2024", "20-12-2024", "20-12-2024"],
    'Strike': [95, 98, 94],
    'Prêmio': [5.10, 4.80, 3.9],
    'Vencimento (em dias)': [43, 78, 78]
})

E_ue = 1.1036
PVOW_euro = 96.55
PVOW_dolar = PVOW_euro / E_ue

df_opcoes_dolar = pd.DataFrame({
    'Tipo de Opção': ["call", "call", "put"],
    'Opção': ["Call VOW 11 C95", "Call VOW 12 C98", "Put VOW 12 P94"],
    'Data de Vencimento': ["15-11-2024", "20-12-2024", "20-12-2024"],
    'Strike': df_opcoes_euro['Strike'] / E_ue,
    'Prêmio': df_opcoes_euro['Prêmio'] / E_ue,
    'Vencimento (em dias)': [43, 78, 78]
})

df_opcoes_euro  
df_opcoes_dolar
#%% Letra B

preco_exercicio_put = 1.1000  
valor_put_eur = 0.030  
exposicao_vendas_eur = 40529  

exposicao_vendas_usd = exposicao_vendas_eur / E_ue

numero_opcoes = exposicao_vendas_usd / preco_exercicio_put 

print(f"A Porsche precisaria comprar {numero_opcoes:.2f} opções de venda (puts) para realizar o hedge completo em dólares.")
#%% Letra C

option_type = input("Digite o tipo de opção (call/put): ").lower()
strike_price = float(input("Digite o preço de exercício: "))
option_price = float(input("Digite o valor da opção: "))
contracts = int(input("Digite o número de contratos: "))

prices = np.linspace(0.8 * strike_price, 1.2 * strike_price, 100)

if option_type == 'put':
    payoff = np.maximum(prices - strike_price, 0)
elif option_type == 'call':
    payoff = np.maximum(strike_price - prices, 0)
else:
    raise ValueError("Tipo de opção inválido. Use 'call' ou 'put'.")

resultado = (payoff - option_price) * contracts
ret = resultado/PVOW_euro

df = pd.DataFrame({
    'Payoff' : payoff * contracts,
    'Preço_Ativo': prices,
    'Resultado': resultado,
    'Retorno' : ret

})

df

plot = (
    ggplot(df, aes(x='Preço_Ativo')) +
        geom_line(aes(y='Resultado'), color="blue", size=1.2, linetype="dotted") +  
        geom_line(aes(y='Payoff'), color="red", size=1.2) +  
        geom_hline(yintercept=0, linetype="dashed", color="black") +
    labs(
        title="Resultado e Payoff da Estratégia de Opções",
        subtitle="Análise de Calls e Puts em USD Ponderada pelos Contratos",
        x="Preço do Ativo Subjacente (St)",
        y="Resultado e Payoff",
        caption="Fonte: Bloomberg"
    ) +
    theme_minimal() +
    theme(
        plot_title=element_text(size=16, weight='bold', ha='center'),
        plot_subtitle=element_text(size=12, ha='center'),
        axis_title_x=element_text(size=10),
        axis_title_y=element_text(size=10),
        axis_text=element_text(size=9),
        plot_caption=element_text(size=8, ha='right', style='italic'),
        figure_size=(8, 5)
    )
)

print(plot)


#%% Letra D1

for index, row in df_opcoes_dolar.iterrows():
    tipo = row['Tipo de Opção']
    strike_price = row['Strike']
    option_price = row['Prêmio']
    nome_opcao = row['Opção']

    prices = np.linspace(0.8 * strike_price, 1.2 * strike_price, 100)

    if tipo == 'put':
        payoff = np.maximum(prices - strike_price, 0)
    elif tipo == 'call':
        payoff = np.maximum(strike_price - prices, 0)
    else:
        raise ValueError("Tipo de opção inválido. Use 'call' ou 'put'.")

    resultado = (payoff - option_price)

    
    df_resultado = pd.DataFrame({
        'Payoff': payoff,
        'Preço_Ativo': prices,
        'Resultado': resultado
    })


    plot = (
        ggplot(df_resultado, aes(x='Preço_Ativo')) +
        geom_line(aes(y='Resultado'), color="red", size=1.2, linetype="dotted") +  
        geom_line(aes(y='Payoff'), color="blue", size=1.2) +  
        geom_hline(yintercept=0, linetype="dashed", color="black") +
        labs(
            title="Payoff da Estratégia de Opções",
            subtitle=f"Análise de {nome_opcao}",
            x="Preço do Ativo Subjacente (St)",
            y="Payoff e Resultado",
            caption="Fonte: Bloomberg"
        ) +
        theme_minimal() +
        theme(
            plot_title=element_text(size=16, weight='bold', ha='center'),
            plot_subtitle=element_text(size=12, ha='center'),
            axis_title_x=element_text(size=10),
            axis_title_y=element_text(size=10),
            axis_text=element_text(size=9),
            plot_caption=element_text(size=8, ha='right', style='italic'),
            figure_size=(8, 5)
        )
    )

    print(plot)
    print(df_resultado)

#%% Letra D2

prices = np.linspace(0.8 * preco_exercicio_put, 1.2 * preco_exercicio_put, 100)

payoff = np.maximum(preco_exercicio_put - prices, 0)

resultado = (payoff - valor_put_eur) * numero_opcoes

df_resultado = pd.DataFrame({
    'Payoff' : payoff * numero_opcoes,
    'Preço do Ativo (St)': prices,
    'Payoff da Estratégia': resultado
})

plot = (
    ggplot(df, aes(x='Preço_Ativo')) +
        geom_line(aes(y='Resultado'), color="blue", size=1.2, linetype="dotted") +  
        geom_line(aes(y='Payoff'), color="red", size=1.2) +  
    geom_hline(yintercept=0, linetype="dashed", color="black") +
    labs(
        title="Payoff e Resultado da Estratégia de Opções FX",
        subtitle="Put de Dólar OTC (1 ano, Strike: 1.1000 EUR/USD)",
        x="Preço do Dólar no Vencimento (St)",
        y="Resultado (€)",
        caption="Fonte: Bloomberg"
    ) +
    theme_minimal() +
    theme(
        plot_title=element_text(size=16, weight='bold', ha='center'),
        plot_subtitle=element_text(size=12, ha='center'),
        axis_title_x=element_text(size=10),
        axis_title_y=element_text(size=10),
        axis_text=element_text(size=9),
        plot_caption=element_text(size=8, ha='right', style='italic'),
        figure_size=(8, 5)
    )
)

print(f"Exposição em dólares: USD {exposicao_vendas_usd}")
print(df_resultado)
print(plot)
# %%
>>>>>>> 77bc682 (Atualiza dos README.md)
