## 📘 Trabalho de Finanças I — Projeção da NAF para a empresa CAMIL (Finanças I | 2023.2)

### 🎯 Objetivo do Trabalho

Desenvolver um modelo em Python para calcular a **Necessidade de Aporte Financeiro (NAF)** da empresa **CAMIL (CAML3.SA)** ao longo de um período de 5 anos, com base nos demonstrativos financeiros extraídos da plataforma **Economatica®**.

Este projeto integra a primeira APS da disciplina **Finanças I**, e tem como objetivo aplicar os conceitos de fluxo de caixa, retorno sobre ativos e patrimônio, política de dividendos, e projeções financeiras com base em dados reais.  
Todas as análises e gráficos foram desenvolvidos em Python, conforme instruções da atividade.

---

### 📂 Estrutura dos Dados

As bases foram organizadas em um arquivo `.xlsx` com quatro planilhas:

- `BP`: Balanço Patrimonial
- `DRE`: Demonstração do Resultado do Exercício
- `DFC`: Demonstração dos Fluxos de Caixa
- `FCx`: Planilha auxiliar de Fluxos de Caixa (estrutura adaptada)

As colunas utilizadas para projeção incluem:

- Receita líquida e lucro líquido (DRE)
- Ativos, passivos e PL (BP)
- Dividendos pagos (DFC)
- FC(A), FC(S), FC(B) (FCx)
- NAF (cálculo final no BP)

---

### 🧼 Limpeza e Padronização

- Padronização das planilhas para leitura por `pandas`
- Exclusão de linhas sem dados relevantes
- Conversão de valores contábeis para arrays NumPy
- Cálculo de variações e taxas médias com tratamento de valores extremos
- Organização das variáveis por ano para facilitar projeções e visualizações

---

### 📊 Análises e Gráficos

#### 📌 Variação da Receita (2018–2022)
- Cálculo da taxa de variação anual da receita
- Média de crescimento ajustada, com exclusão de outliers

#### 📌 Indicadores de Rentabilidade
- **Payout** médio com base nos dividendos pagos
- **ROA** (Return on Assets) e **ROE** (Return on Equity)
- Cálculo dos índices de crescimento **G Interno** e **G Sustentável**

#### 📌 Projeções (2023–2027)
- **Balanço Patrimonial projetado** (Ativos, Passivos e PL)
- **DRE projetada** (Receita e Lucro)
- **Fluxo de Caixa** projetado: FC(A), FC(S), FC(B)
- **Projeção da NAF** (Necessidade de Aporte Financeiro)
- Comparação entre receitas históricas e projetadas

Todos os gráficos foram gerados com `matplotlib` e apresentados em escala temporal, com títulos, eixos e legendas configurados.

---

### 💻 Tecnologias Utilizadas

- **Python 3.x**
- **Bibliotecas**:
  - `pandas` — manipulação de planilhas
  - `numpy` — cálculos vetoriais e estatísticos
  - `matplotlib.pyplot` — visualização dos gráficos

---

### ▶️ Como Reproduzir

1. Certifique-se de ter o arquivo `CAML3.xlsx` na mesma pasta do script.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install pandas numpy matplotlib openpyxl
   ```

3. Execute o script:
   ```bash
   python APS\ Finanças.py
   ```

4. O programa irá:
   - Ler os dados da planilha
   - Calcular as métricas e projeções
   - Gerar os gráficos exigidos pela APS
   - Imprimir a média de crescimento, indicadores financeiros e estrutura da NAF

---

### 📝 Observações

- O cenário é **hipotético** e os dados foram utilizados **exclusivamente para fins educacionais**.
- O programa é compatível com versões recentes do Excel e requer a biblioteca `openpyxl` para leitura dos arquivos `.xlsx`.

---

Atenciosamente,  
**Hicham Munir Tayfour**


