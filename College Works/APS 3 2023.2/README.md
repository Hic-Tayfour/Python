## 📘 Trabalho de Modelos para Tomada de Decisão — Simulação de Estoque e Dinâmica de Sistemas (Modelos para Tomada de Decisão | 2023.2)

### 🎯 Objetivo do Trabalho

Desenvolver um modelo computacional utilizando Python para aplicar conceitos de **simulação de estoque** e **dinâmica de sistemas** em um cenário hipotético baseado em um restaurante italiano localizado na cidade de **Natal/RN**.

Este projeto integra a **APS 3** da disciplina **Modelos para Tomada de Decisão** e teve como objetivos principais:
- Simular a demanda por ingredientes essenciais (semolina, leite e farinha)
- Calcular o **lote econômico** e o **lote de segurança**
- Estimar a evolução da clientela com base no **Modelo de Bass**
- Aplicar técnicas aprendidas em aula a um contexto interdisciplinar com enfoque prático

---

### 📂 Estrutura do Modelo

O script está dividido em duas partes principais:

#### 🥫 Simulação de Estoque

- **Contexto**: estoque de ingredientes perecíveis e não perecíveis para massas frescas.
- **Horizonte**: 30 dias (mês)
- **Ingredientes analisados**:
  - Semolinas (normal, média = 1000g, desvio = 250g)
  - Leite (normal, média = 2000ml, desvio = 250ml)
  - Farinha (uniforme, entre 2000g e 5000g)

##### Variáveis-chave:

| Parâmetro                | Valor                |
|--------------------------|----------------------|
| Custo de estocagem médio | R$ 4,33              |
| Custo de frete           | R$ 100,00            |
| Lote econômico (Wilson)  | ≈ calculado via fórmula |
| Lote com segurança       | ≈ ajustado pelo desvio da demanda |

---

#### 👥 Dinâmica de Sistemas (Modelo de Bass)

- Estimativa de crescimento da **clientela** ao longo de 30 dias e por semana
- Uso de **equações diferenciais ordinárias (EDO)** com `odeint` do `scipy.integrate`
- Parâmetros ajustados para o contexto urbano de Natal/RN:

| Parâmetro                  | Valor                     |
|----------------------------|---------------------------|
| População potencial (N)    | 751.300 pessoas           |
| Clientes iniciais (C₀)     | 10.000                    |
| Coef. de inovação (a)      | 0.001                     |
| Coef. de imitação (i)      | 0.02                      |
| Coef. de saturação (c)     | 10                        |

- Resultados gerados:
  - Gráfico com evolução de adotantes e adotantes potenciais
  - Gráfico com crescimento de clientes a cada semana
  - Impressão dos valores semanais de clientes estimados

---

### 📊 Resultados Esperados

- Estimativas robustas para a demanda mensal
- Cálculo preciso do lote econômico e do lote de segurança
- Curvas de crescimento da base de clientes que ajudam o restaurante a planejar produção e estoque
- Integração clara entre modelos estatísticos, logísticos e dinâmicos

---

### 💻 Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas:
  - `numpy`
  - `matplotlib.pyplot`
  - `scipy.integrate`

---

### ▶️ Como Reproduzir

1. Instale as dependências:
   ```bash
   pip install numpy matplotlib scipy
   ```

2. Execute o script:
   ```bash
   python "APS Modelos .py"
   ```

3. O script irá:
   - Simular demandas
   - Calcular os lotes econômicos
   - Resolver o modelo de Bass
   - Gerar gráficos e imprimir as métricas de decisão

---

### 🔗 Links Úteis (Material de Aula)

- [Dinâmica de Sistemas](https://github.com/Hic-Tayfour/Python/tree/4ed5bb83c9ad6108b2dcc5829df79e11e61dc72c/College%20Studies/Modelos%20Para%20Tomada%20De%20Decis%C3%A3o/Din%C3%A2mica%20de%20Sistemas)
- [Simulação de Estoque](https://github.com/Hic-Tayfour/Python/tree/ee380ecfe57f2117a03bd177c922552b26be57e3/College%20Studies/Modelos%20Para%20Tomada%20De%20Decis%C3%A3o/Simula%C3%A7%C3%A3o%20de%20Estoque)

---


Atenciosamente,  
**Hicham Munir Tayfour**
