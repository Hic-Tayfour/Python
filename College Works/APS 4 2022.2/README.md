## 📘 Trabalho de SI — Sensor On Balance Volume em Python (Sistemas de Informação | 2022.2)

### 🎯 Objetivo do Trabalho

Desenvolver uma plataforma de análise quantitativa para avaliação do desempenho de ações, com foco na ação **PETR4.SA**, utilizando programação em **Python**. A proposta se insere no contexto da APS-4, integrando conhecimentos dos checkpoints anteriores da disciplina de Sistemas de Informação.

A análise envolveu:
- Coleta automatizada de dados do Yahoo Finance
- Cálculo de retornos com `pct_change`
- Construção do indicador **On Balance Volume (OBV)**
- Estimativa de tendências com `numpy.polyfit`
- Geração de **média móvel de 7 dias** com `rolling`
- Visualizações com `matplotlib` e `seaborn`
- Geração de estatísticas descritivas e Boxplot

---

### 📂 Estrutura dos Dados

- `Close`: Preço de fechamento da ação
- `Retorno`: Variação percentual diária dos preços
- `OBV`: Sensor On Balance Volume construído manualmente
- `Ret_Fec`: Tendência linear dos preços de fechamento
- `Ret_OBV`: Tendência linear do OBV
- `MedMov`: Média móvel de 7 dias aplicada ao `Close`

---

### 🧼 Limpeza e Padronização

- Remoção da coluna `Adj Close` do DataFrame original
- Criação da coluna `Retorno` com base no `Close` via `pct_change()`
- Construção do OBV com base em estrutura `for` e lógica condicional
- Aplicação de `numpy.polyfit()` para ajustar retas de tendência
- Cálculo da média móvel com `rolling(window=7)`
- Remoção das colunas auxiliares para gerar o boxplot final

---

### 📊 Análises Descritivas

#### 📌 Evolução dos Preços e Retornos
- Subplot com dois gráficos: 
  - Fechamento da ação (`Close`) com marcadores
  - Retorno percentual diário (`Retorno`)
- Apresentação clara dos comportamentos de preço ao longo do tempo

#### 📌 OBV e Tendência Linear
- Cálculo do OBV com base na variação diária do preço e volume
- Gráfico com linha de tendência linear ajustada com `polyfit` tanto para `Close` quanto para `OBV`

#### 📌 Média Móvel de 7 Dias
- Gráfico com a curva do `Close` sobreposta à sua média móvel (`MedMov`)
- Análise visual de quando os preços cruzam a média móvel

#### 📌 Retornos e Histograma
- Subplot com:
  - Gráfico de linha dos retornos
  - Histograma com curva de densidade estimada (`seaborn.distplot`)
- Permite avaliar a simetria da distribuição de retornos e presença de outliers

#### 📌 Estatísticas da Ação (Impressas no Console)
- Último preço de fechamento (`Close`)
- Valor máximo, mínimo e médio
- Retorno máximo e mínimo com as datas correspondentes
- Volatilidade dos preços e dos retornos em termos percentuais

#### 📌 Boxplot Transposto
- Geração de boxplot com a transposição (`.T`) do DataFrame
- Análise visual da dispersão diária dos preços de fechamento

---

### 💻 Tecnologias Utilizadas

- Linguagem: **Python 3.x**
- Bibliotecas utilizadas:
  - `yfinance`: Coleta de dados financeiros
  - `numpy`: Cálculo de regressões e vetores
  - `pandas`: Manipulação e organização de dados
  - `matplotlib.pyplot`: Visualizações estáticas
  - `seaborn`: Distribuições estatísticas

---

### ▶️ Como Reproduzir

1. Instale as bibliotecas necessárias (se ainda não tiver):
   ```bash
   pip install yfinance pandas numpy matplotlib seaborn
   ```

2. Execute o script `aps4_obv.py` em um ambiente Python (como VS Code, Spyder ou Jupyter)

3. Os seguintes resultados serão produzidos:
   - Gráficos salvos ou exibidos automaticamente
   - Estatísticas impressas no console
   - Análise completa da ação PETR4 no período de 2020 a 2022

---

Atenciosamente,  
**Hicham Munir Tayfour**

