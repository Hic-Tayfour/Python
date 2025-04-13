## 📘 Trabalho de Finanças I — Avaliação de Projeto com Simulação de Monte Carlo (Finanças I | 2023.2)

### 🎯 Objetivo do Trabalho

Avaliar a viabilidade econômica de um projeto hipotético para a empresa **CAMIL (CAML3.SA)** por meio da técnica de **Simulação de Monte Carlo**, utilizando linguagem **Python**.

Este trabalho integra a **APS 2 – Parte B** da disciplina **Finanças I**, e teve como foco o uso de simulações para a tomada de decisão sob incerteza, com o cálculo de **VPL (Valor Presente Líquido)** e **TIR (Taxa Interna de Retorno)** em múltiplos cenários.

---

### 📊 Descrição da Simulação

Foram realizadas **100.000 simulações** utilizando distribuições de probabilidade para as variáveis-chave do projeto. A cada iteração, foi gerado um fluxo de caixa de 5 anos, do qual se calculou o VPL e a TIR.

A modelagem seguiu as seguintes premissas:

- **Horizonte de Análise:** 5 anos
- **Taxa Mínima de Atratividade (TMA):** 20% a.a.
- **Custo da Mercadoria Vendida (CMV):** 79% da Receita
- **Taxa de Depreciação:** 20% do Investimento
- **Imposto (IR):** 34%
- **Capital de Giro (CCL):** 5% do Investimento

---

### 🎲 Variáveis Aleatórias Simuladas

| Variável              | Distribuição | Média        | Desvio Padrão |
|-----------------------|--------------|--------------|----------------|
| Investimento Inicial  | Normal       | R$ 113.669.650 | R$ 2.500.000   |
| Quantidade Vendida    | Normal       | 25.360.000 unidades | 50.000 unidades |
| Preço Unitário        | Normal       | R$ 7,70       | R$ 1,50        |

---

### 🧮 Etapas da Simulação

1. Geração dos valores aleatórios de **investimento**, **quantidade** e **preço**
2. Cálculo da **receita**, **CMV**, **depreciação**, **LAJIR**, **NOPAT** e **FCO**
3. Construção do fluxo de caixa:  
   \[
   FC = [- (Investimento + CCL), FCO, FCO, FCO, FCO, FCO + CCL]
   \]
4. Cálculo do **VPL** (`numpy_financial.npv`) e **TIR** (`numpy_financial.irr`)
5. Armazenamento de resultados e análise de frequência

---

### 📈 Resultados Gerados

- **Probabilidade do projeto ser viável** (VPL > 0):  
  Impressa no console após as simulações

- **Distribuições dos resultados**:
  - Histograma do VPL com curva ajustada (Normal)
  - Histograma da TIR com densidade estimada

- **Interpretação esperada**:
  - Variação esperada do retorno do projeto
  - Análise de risco com base na dispersão dos VPLs e TIRs
  - Decisão de aprovação ou não com base na probabilidade de sucesso

---

### 💻 Tecnologias Utilizadas

- **Python 3.x**
- **Bibliotecas**:
  - `numpy_financial`: Cálculo do VPL e TIR
  - `numpy`: Geração de amostras aleatórias
  - `matplotlib.pyplot`: Visualização de gráficos
  - `scipy.stats.norm`: Ajuste de distribuição normal

---

### ▶️ Como Reproduzir

1. Instale as dependências:
   ```bash
   pip install numpy matplotlib scipy numpy-financial
   ```

2. Execute o script:
   ```bash
   python APS\ Finanças\ Monte\ Carlo.py
   ```

3. Resultados:
   - Histogramas com curvas ajustadas
   - Probabilidade do projeto ser viável (print no console)

---


Atenciosamente,  
**Hicham Munir Tayfour**
