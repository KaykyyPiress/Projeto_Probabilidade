import pandas as pd
import numpy as np

# 1) Carregar o arquivo
# Se for CSV:
# df = pd.read_csv('CompanhiaMB.csv', header=0, na_values=['?'])
# Se for Excel:
# df = pd.read_excel('seu_arquivo.xlsx', header=0, na_values=['?'])

df = pd.read_csv('CompanhiaMB.csv', header=0, na_values=['?'])

print("Shape original:", df.shape)
print(df.head())

# 2) Substituir explicitamente “?” e strings vazias por NaN (caso haja outras)
df = df.replace('?', np.nan).replace('', np.nan)

# 3) Remover linhas que ainda tenham qualquer NaN
df = df.dropna()
print("Após dropna:", df.shape)

# 4) Remover linhas duplicadas
df = df.drop_duplicates()
print("Após drop_duplicates:", df.shape)

# 5) (Opcional) Resetar índice
df = df.reset_index(drop=True)

# 6) Salvar resultado limpo
df.to_csv('CompanhiaMB_limpo.csv', index=False)
# ou para Excel:
# df.to_excel('CompanhiaMB_clean.xlsx', index=False)

print("Arquivo salvo em 'CompanhiaMB_clean.csv'.")
