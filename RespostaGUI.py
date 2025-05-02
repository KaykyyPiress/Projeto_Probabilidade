import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro, gaussian_kde
import tkinter as tk
from tkinter import messagebox

# Carrega e limpa dados
df = pd.read_csv('CompanhiaMB_limpo.csv')
x, y = df['idade_anos'], df['salario']

# Funções de análise e plot
def show_stats():
    stats = pd.DataFrame({
        'média':      [x.mean(),      y.mean()],
        'variância':  [x.var(ddof=0), y.var(ddof=0)],
        'desvio std': [x.std(ddof=0), y.std(ddof=0)],
        'mediana':    [x.median(),    y.median()]
    }, index=['idade_anos','salario'])
    messagebox.showinfo("Estatísticas", stats.to_string())

def plot_hist(var, title, xl):
    plt.figure(); plt.hist(var, bins=10, edgecolor='black')
    plt.title(title); plt.xlabel(xl); plt.ylabel('Frequência')
    plt.grid('--', alpha=0.5); plt.show()

def plot_box(var, title, yl):
    plt.figure(); plt.boxplot(var)
    plt.title(title); plt.ylabel(yl)
    plt.grid('--', alpha=0.5); plt.show()

def show_corr():
    c = x.corr(y)
    messagebox.showinfo("Correlação", f"Pearson: {c:.3f}")

def show_normal():
    sx, px = shapiro(x); sy, py = shapiro(y)
    txt = f"x: estat={sx:.4f}, p={px:.4f}\n" \
          f"y: estat={sy:.4f}, p={py:.4f}"
    messagebox.showinfo("Shapiro–Wilk", txt)

def plot_density(var, title, xl):
    kde = gaussian_kde(var)
    xs = np.linspace(var.min(), var.max(), 200)
    plt.figure()
    plt.hist(var, bins=10, density=True, edgecolor='black')
    plt.plot(xs, kde(xs), linewidth=2)
    plt.title(title); plt.xlabel(xl); plt.ylabel('Densidade')
    plt.grid('--', alpha=0.5); plt.show()

# Monta janela
root = tk.Tk()
root.title("Analisador Estatístico")

buttons = [
    ("Estatísticas", show_stats),
    ("Hist Idade",     lambda: plot_hist(x, "Hist Idade", "idade_anos")),
    ("Hist Salário",   lambda: plot_hist(y, "Hist Salário", "salario")),
    ("Box Idade",      lambda: plot_box(x, "Box Idade", "idade_anos")),
    ("Box Salário",    lambda: plot_box(y, "Box Salário", "salario")),
    ("Correlação",     show_corr),
    ("Normalidade",    show_normal),
    ("Dens Idade",     lambda: plot_density(x, "Hist+KDE Idade", "idade_anos")),
    ("Dens Salário",   lambda: plot_density(y, "Hist+KDE Salário", "salario")),
    ("Sair",           root.destroy)
]

for text, cmd in buttons:
    tk.Button(root, text=text, width=20, command=cmd).pack(pady=2)

root.mainloop()
