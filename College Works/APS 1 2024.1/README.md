## 📘 Trabalho de Finanças II — Seleção de Portfólio com Fronteira Eficiente (Finanças II | 2024.1)

### 🎯 Objetivo do Trabalho

Construir a **carteira ótima final** para três perfis distintos de investidores — **agressivo**, **moderado** e **conservador** — utilizando os conceitos de **seleção de portfólio**. Foram aplicadas técnicas clássicas de finanças como:

- Fronteira de mínima variância
- Fronteira eficiente
- Carteira de risco ótima
- Linha de alocação de capital (LAC)
- Índice de Sharpe

Este projeto integra a **APS 1** da disciplina **Finanças II**, e foi implementado em linguagem **Python** com base em dados reais de ativos financeiros, organizados em uma base de dados padronizada.

---

### 📂 Estrutura da Base de Dados

- **Fonte dos dados:** Economatica
- **Período:** Dezembro de 2013 a Dezembro de 2023
- **Periodicidade:** Mensal

#### 📊 Ativos analisados

| Tipo                  | Ativos utilizados                         |
|-----------------------|--------------------------------------------|
| Ações e BDRs          | MRFG3, KLBN3, JNJB34                      |
| Fundos Imobiliários   | HGLG11                                    |
| Ativo Cambial         | Dólar                                     |
| Ativo Digital         | Bitcoin                                   |
| Carteira de Mercado   | IBOVESPA                                  |
| Ativo Livre de Risco  | CDI mensal estimado: 0,9226%              |

---

### 🧠 Metodologia

#### 🔹 Preparação dos dados
- Importação e organização das séries de retornos mensais
- Cálculo das médias e desvios padrões
- Criação da matriz de covariância

#### 🔹 Simulação de carteiras
- Geração de **100.000 carteiras aleatórias**
- Cálculo do retorno e da volatilidade de cada carteira
- Armazenamento dos resultados e índice de Sharpe

#### 🔹 Identificação da carteira ótima
- Seleção da carteira com maior índice de Sharpe
- Cálculo da LAC (linha de alocação de capital)
- Plotagem da fronteira eficiente e marcação da carteira ótima

---

### 📊 Resultados Obtidos

- Gráfico da **fronteira eficiente** com distribuição de risco-retorno
- Ponto de máxima eficiência (carteira ótima) identificado
- **Composição da carteira ótima** apresentada em tabela
- Cálculo da LAC e do **índice de Sharpe** da carteira ótima

---

### 💻 Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas:
  - `pandas`, `numpy` — manipulação e cálculo estatístico
  - `matplotlib.pyplot` — visualização dos gráficos
  - `numpy_financial` — cálculo de TIR e VPL (caso necessário)
  - `scipy.optimize.minimize` — otimização de portfólio (opcional)

---

### ▶️ Como Reproduzir

1. Certifique-se de que o arquivo `carteira.xlsx` está na mesma pasta do script.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas numpy matplotlib numpy-financial openpyxl
   ```

3. Execute o script:
   ```bash
   python "APS 1 Fin II.py"
   ```

4. O programa irá:
   - Calcular a fronteira eficiente
   - Determinar a carteira de Sharpe ótimo
   - Gerar gráficos interativos e imprimir composição da carteira ideal

---


Atenciosamente,  
**Hicham Munir Tayfour**
