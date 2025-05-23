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
![image](https://github.com/user-attachments/assets/14c96fd7-0abd-4df9-b010-0a9ddd548cb8)
- **Histograma de idade (x)**: mostra a distribuição das idades, com maior frequência entre 30 e 35 anos.

![image](https://github.com/user-attachments/assets/1047de74-2299-4f4d-8e1e-ad00baad3e21)
- **Histograma de salário (y)**: exibe a distribuição salarial, concentrada entre R$7,50 e R$12,50.  

Os histogramas ajudam a visualizar a forma geral da distribuição e identificar possíveis assimetrias.

## Boxplots

![image](https://github.com/user-attachments/assets/4cef0a6c-eac0-4bb9-b93a-6983abd1814d)
- **Boxplot de idade (x)**: mediana próxima a 35 anos, sem outliers significativos.

  ![image](https://github.com/user-attachments/assets/ce34379d-5e1c-45a9-a250-bfb38e560c3c)
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
![image](https://github.com/user-attachments/assets/80a356a7-bc69-446c-8c68-969d12ba7370)
- **Idade (x)**: sobrepõe curva KDE ao histograma, reforçando a concentração na faixa intermediária.

  ![image](https://github.com/user-attachments/assets/cbcc97e1-fded-40d3-b7d2-00ece63ca5ef)
- **Salário (y)**: curva de densidade confirma a distribuição observada no histograma.  

Combinando histograma e densidade, obtemos uma visão mais suave da forma da distribuição.

---
