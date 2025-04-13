## 📘 Trabalho de Finanças III — Aplicações com Opções e Value at Risk (APS I | 2024.2)

### 🎯 Objetivo do Trabalho

Este projeto tem como objetivo aplicar conceitos de **gestão de riscos com derivativos** em um caso real baseado no estudo “Hedging at Porsche”, utilizando **Python** para simular, visualizar e interpretar operações com **opções financeiras** e estimativas de **Value at Risk (VaR)**.

A atividade integra a **APS I da disciplina Finanças III**, e contempla:

- Construção de estratégias com calls e puts
- Simulação de hedge cambial com opções OTC
- Cálculo do VaR histórico e via Monte Carlo
- Visualizações gráficas de payoff, resultado e risco

---

### 🛠️ Estrutura dos Scripts

#### 🧾 `APS Fin III FX.py` — Aplicação 1

Simula operações com **opções de compra e venda** sobre ações da **Volkswagen (VOW3)** e um hedge cambial com **put de USD** em operação OTC.

Inclui:
- Conversão de preços entre **euro e dólar**
- Cálculo da quantidade de contratos para hedge completo
- Geração automática de gráficos de **payoff e resultado**
- Simulação interativa via `input()` de estratégias manuais
- Análises individuais das opções da Porsche

---

#### 📉 `APS Fin III V@R.py` — Aplicação 2

Implementa o cálculo do **Value at Risk (VaR)** para a exposição cambial da Porsche:

- Coleta de dados históricos do EUR/USD via `yfinance`
- Cálculo do VaR histórico com 95% de confiança
- Simulação de Monte Carlo com 10.000 cenários
- Cálculo do VaR simulado para as receitas em EUR
- Gráficos:
  - Histograma dos retornos
  - Histograma das perdas simuladas
  - Curva de distribuição acumulada (CDF)

---

### 📊 Dados Utilizados

- **Ticker de câmbio:** EURUSD=X (Yahoo Finance)
- **Período de análise:** 2018 até agosto de 2024
- **Receita de referência (exposição):** € 40.529 (Porsche, 2023)
- **Paridade FX estimada:** EUR/USD ≈ 1.1036

---

### 📈 Variáveis-Chave e Premissas

| Variável                     | Valor                    |
|-----------------------------|--------------------------|
| Vendas em EUR               | € 40.529                 |
| Strike da put OTC (USD)     | 1.1000                   |
| Prêmio da put OTC (EUR)     | 0,030                    |
| Simulações Monte Carlo      | 10.000                   |
| Horizonte para VaR          | 252 dias úteis (1 ano)   |
| Nível de Confiança (VaR)    | 95%                      |

---

### 💻 Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas:
  - `numpy`, `pandas`
  - `matplotlib`, `plotnine`
  - `yfinance`
  - `scipy.stats`

---

### ▶️ Como Executar

1. Instale as dependências:
   ```bash
   pip install numpy pandas matplotlib plotnine scipy yfinance
   ```

2. Execute separadamente os scripts:
   ```bash
   python "APS Fin III FX.py"
   python "APS Fin III V@R.py"
   ```

3. Os gráficos serão exibidos automaticamente, e os principais resultados impressos no console.

---

### 🧠 Aplicações e Resultados Esperados

- **Aplicação 1**: Modelagem e análise de estratégias com opções, incluindo hedge da exposição cambial da Porsche com derivativos de balcão.
- **Aplicação 2**: Avaliação do risco de mercado usando distribuições reais e simuladas para quantificar perdas esperadas.

---


Atenciosamente,  
**Hicham Munir Tayfour**
