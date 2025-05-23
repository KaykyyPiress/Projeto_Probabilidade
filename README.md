
# Análise Estatística de Idade e Salário

Este projeto em Python realiza uma análise estatística das variáveis `idade_anos (x)` e `salario (y)` a partir de um conjunto de dados previamente pré-processado. A seguir, explicamos detalhadamente cada resultado obtido.

## Estatísticas Descritivas

| Variável        | Média  | Variância | Desvio Padrão | Mediana |
|-----------------|--------|-----------|---------------|---------|
| idade_anos (x)  | 35.15  | 33.03     | 5.75          | 34.50   |
| salario (y)     | 12.12  | 22.92     | 4.79          | 11.93   |

- **Média**: valor médio das variáveis.  
- **Variância**: mede a dispersão dos valores ao redor da média.  
- **Desvio padrão**: raiz quadrada da variância, em unidades originais.  
- **Mediana**: valor central dos dados ordenados, resistente a outliers.  

## Histogramas

- **Histograma de idade (x)**: mostra a distribuição das idades, com maior frequência entre 30 e 35 anos.
- **Histograma de salário (y)**: exibe a distribuição salarial, concentrada entre R$7,50 e R$12,50.  

Os histogramas ajudam a visualizar a forma geral da distribuição e identificar possíveis assimetrias.

## Boxplots

- **Boxplot de idade (x)**: mediana próxima a 35 anos, sem outliers significativos.
- **Boxplot de salário (y)**: mediana próxima a R$12, sem outliers evidentes.  

Os boxplots evidenciam dispersão, quartis e possíveis valores extremos.

## Correlação

- **Coeficiente de correlação de Pearson** entre idade e salário: **0.482**  

Indica correlação moderada e positiva: idades maiores tendem a associar-se a salários maiores.

## Teste de Normalidade (Shapiro–Wilk)

| Variável        | Estatística | p-valor |
|-----------------|-------------|---------|
| idade_anos (x)  | 0.9603      | 0.5496  |
| salario (y)     | 0.9726      | 0.8088  |

Como ambos os p-valores são maiores que 0.05, não rejeitamos a hipótese de normalidade para nenhuma das variáveis.

## Histogramas com Densidade

- **Idade (x)**: sobrepõe curva KDE ao histograma, reforçando a concentração na faixa intermediária.
- **Salário (y)**: curva de densidade confirma a distribuição observada no histograma.  

Combinando histograma e densidade, obtemos uma visão mais suave da forma da distribuição.

---

## 🧠 Código-Fonte Completo da Análise

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro
from scipy.stats import gaussian_kde  # <— aqui!

df = pd.read_csv('CompanhiaMB_limpo.csv')

x = df['idade_anos']
y = df['salario']

stats = pd.DataFrame({
    'média':      [x.mean(),      y.mean()],
    'variância':  [x.var(ddof=0), y.var(ddof=0)],
    'desvio std': [x.std(ddof=0), y.std(ddof=0)],
    'mediana':    [x.median(),    y.median()]
}, index=['idade_anos (x)','salario (y)'])

print(stats)

plt.figure(figsize=(8, 5))
plt.hist(x, bins=10, edgecolor='black')
plt.title('Histograma de x (idade_anos)')
plt.xlabel('idade_anos')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(y, bins=10, edgecolor='black')
plt.title('Histograma de y (salario)')
plt.xlabel('salario')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

plt.figure(figsize=(8, 5))
plt.boxplot(x)
plt.title('Boxplot de x (idade_anos)')
plt.ylabel('idade_anos')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

plt.figure(figsize=(8, 5))
plt.boxplot(y)
plt.title('Boxplot de y (salario)')
plt.ylabel('salario')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

corr = x.corr(y)
print(f'Coeficiente de correlação de Pearson entre idade_anos (x) e salario (y): {corr:.3f}')

stat_x, p_x = shapiro(x)
stat_y, p_y = shapiro(y)

print("Teste de normalidade (Shapiro-Wilk):")
print(f"x (idade_anos): estatística = {stat_x:.4f}, p-valor = {p_x:.4f}")
print(f"y (salario):     estatística = {stat_y:.4f}, p-valor = {p_y:.4f}")

def plot_hist_with_density(values, label):
    kde = gaussian_kde(values)
    xs = np.linspace(values.min(), values.max(), 200)

    plt.figure(figsize=(8, 5))
    plt.hist(values, bins=10, density=True, edgecolor='black')
    plt.plot(xs, kde(xs))
    plt.title(f'Histograma e Densidade de {label}')
    plt.xlabel(label)
    plt.ylabel('Densidade')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

plot_hist_with_density(x, 'idade_anos')
plot_hist_with_density(y, 'salario')
```
