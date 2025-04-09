#%% Importando as bibliotecas necessárias
import numpy as np
import pandas as pd
import yfinance as yf
from plotnine import *

#%% Obtendo dados históricos da taxa de câmbio EUR/USD
data = yf.download('EURUSD=X', start='2018-01-01', end='2024-08-31')

# Calculando os retornos diários da taxa de câmbio
data['Return'] = data['Adj Close'].pct_change().dropna()

# Calculando o VaR com nível de confiança de 95% para os retornos históricos
var_5 = np.percentile(data['Return'], 5)

#%% Visualizando o histograma dos retornos e o VaR histórico
hist_plot = (
    ggplot(data, aes(x='Return', y="stat(density)")) +
    geom_histogram(bins=100, fill="blue", color="black", alpha=0.7) +
    geom_vline(xintercept=var_5, linetype='dashed', color='red', size=1) +
    geom_density(alpha=0.2, fill="gray") +
    labs(
        title="Histograma dos Retornos Diários da Taxa de Câmbio EUR/USD",
        subtitle="Análise de 2018 a agosto de 2024",
        x="Retorno Diário",
        y="Densidade",
        caption="Fonte: Yahoo Finance"
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

print(hist_plot)

#%% Calculando as estatísticas dos retornos históricos para a simulação de Monte Carlo
mean_return = data['Return'].mean()
std_dev_return = data['Return'].std()

# Definindo os parâmetros da simulação de Monte Carlo
num_simulacoes = 10000  
dias = 252  

# Simulação de retornos futuros usando Monte Carlo
simulated_returns = np.random.normal(mean_return, std_dev_return, (num_simulacoes, dias))

# Calculando a exposição cambial da Porsche (exemplo fictício)
vendas_porsche = 40529   # Receita de 2023 em EUR
simulated_losses = vendas_porsche * simulated_returns

# Calculando o VaR com nível de confiança de 95% para as perdas simuladas
var_5_mc = np.percentile(simulated_losses, 5)

print(f"VaR Histórico (95%): {var_5_mc:.4f}")
#%% Plotando o histograma das perdas simuladas
losses_flat = simulated_losses.flatten()
histogram_plot = (
    ggplot(pd.DataFrame(losses_flat, columns=['Loss']), aes(x='Loss')) +
    geom_histogram(bins=100, fill="blue", color="black", alpha=0.7) +
    geom_vline(xintercept=var_5_mc, linetype='dashed', color='red', size=1) +
    labs(
        title="Histograma das Perdas Simuladas (Monte Carlo)",
        subtitle="Simulação de Monte Carlo para o VaR com 95% de confiança",
        x="Perda Simulada (EUR)",
        y="Frequência",
        caption="Simulação de Monte Carlo para exposição cambial"
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

print(histogram_plot)

#%% Plotando a Curva de Distribuição Cumulativa (CDF) das perdas simuladas
sorted_losses = np.sort(losses_flat)
cdf = np.arange(len(sorted_losses)) / float(len(sorted_losses))
cdf_df = pd.DataFrame({'Loss': sorted_losses, 'CDF': cdf})

cdf_plot = (
    ggplot(cdf_df, aes(x='Loss', y='CDF')) +
    geom_line(color="blue", size=1.2) +
    geom_vline(xintercept=var_5_mc, linetype='dashed', color='red', size=1) +
    labs(
        title="Curva de Distribuição Cumulativa das Perdas Simuladas (Monte Carlo)",
        subtitle="Simulação de Monte Carlo para o VaR com 95% de confiança",
        x="Perda Simulada (EUR)",
        y="CDF",
        caption="Simulação de Monte Carlo para exposição cambial"
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

print(cdf_plot)
