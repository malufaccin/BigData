import pandas as pd
from seaborn import load_dataset

# Carregando o dataset 'penguins'
dados = load_dataset('penguins')

# 1. Amostragem sem substituição
print('Amostragem sem substituição')
amostra = dados.sample(frac=0.1)  # Seleciona 10% dos dados sem substituição
print(amostra.index.value_counts().head())

# 2. Amostragem com substituição
print('\nAmostragem com substituição')
amostra = dados.sample(n=50, replace=True)  # Seleciona 50 amostras com substituição
print(amostra.index.value_counts().head())

# 3. Amostragem estratificada
print('\nAmostragem estratificada')

# Contagem das espécies na base de dados original
print('Contagem da base de dados original:')
contagem = dados['species'].value_counts()
print(contagem)

# Criando amostra estratificada
amostra = pd.DataFrame()

for especie, quantidade_total in contagem.items():
    quantidade = int(quantidade_total * 0.1)  # 10% de cada espécie
    amostra_especie = dados[dados['species'] == especie].sample(n=quantidade)
    amostra = pd.concat([amostra, amostra_especie])  # Substituição do append (deprecated)

# Contagem das espécies na amostra estratificada
print('\nContagem da amostra:')
print(amostra['species'].value_counts())
