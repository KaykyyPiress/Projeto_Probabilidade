#a) Média, variância, desvio padrão e mediana para x e y.
# x = idade_anos
# y = salario
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro
from scipy.stats import gaussian_kde  # <— aqui!


# 1) Carrega o CSV (já pré-processado)
df = pd.read_csv('CompanhiaMB_limpo.csv')

# 2) Define x e y
x = df['idade_anos']
y = df['salario']

# 3) Calcula estatísticas
stats = pd.DataFrame({
    'média':      [x.mean(),      y.mean()],
    'variância':  [x.var(ddof=0), y.var(ddof=0)],   # ddof=0 para variância populacional
    'desvio std': [x.std(ddof=0), y.std(ddof=0)],
    'mediana':    [x.median(),    y.median()]
}, index=['idade_anos (x)','salario (y)'])

print(stats)

# b) O histograma de x e y
# Histograma de x (idade_anos)
plt.figure(figsize=(8, 5))
plt.hist(x, bins=10, edgecolor='black')
plt.title('Histograma de x (idade_anos)')
plt.xlabel('idade_anos')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Histograma de y (salario)
plt.figure(figsize=(8, 5))
plt.hist(y, bins=10, edgecolor='black')
plt.title('Histograma de y (salario)')
plt.xlabel('salario')
plt.ylabel('Frequência')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

## c) O Bloxplot de x e y
# Boxplot de x (idade_anos)
plt.figure(figsize=(8, 5))
plt.boxplot(x)
plt.title('Boxplot de x (idade_anos)')
plt.ylabel('idade_anos')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Boxplot de y (salario)
plt.figure(figsize=(8, 5))
plt.boxplot(y)
plt.title('Boxplot de y (salario)')
plt.ylabel('salario')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

## d) Calcula coeficiente de correlação de Pearson
corr = x.corr(y)

print(f'Coeficiente de correlação de Pearson entre idade_anos (x) e salario (y): {corr:.3f}')

## e) Fazer o teste de normalidade para  y e x.
# Teste de Shapiro-Wilk
stat_x, p_x = shapiro(x)
stat_y, p_y = shapiro(y)

print("Teste de normalidade (Shapiro-Wilk):")
print(f"x (idade_anos): estatística = {stat_x:.4f}, p-valor = {p_x:.4f}")
print(f"y (salario):     estatística = {stat_y:.4f}, p-valor = {p_y:.4f}")


## f) Fazer o gráfico de densidade junto com o histograma para as variáveis x e y.
def plot_hist_with_density(values, label):
    # Calcula KDE
    kde = gaussian_kde(values)
    xs = np.linspace(values.min(), values.max(), 200)
    
    plt.figure(figsize=(8, 5))
    # Histograma em densidade
    plt.hist(values, bins=10, density=True, edgecolor='black')
    # Curva de densidade
    plt.plot(xs, kde(xs))
    plt.title(f'Histograma e Densidade de {label}')
    plt.xlabel(label)
    plt.ylabel('Densidade')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Plota para x
plot_hist_with_density(x, 'idade_anos')

# Plota para y
plot_hist_with_density(y, 'salario')