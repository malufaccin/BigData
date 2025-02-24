import pandas as pd

# Lendo os dados do arquivo CSV
dados = pd.read_csv('produtos.csv')
print('\nDados lidos de arquivo:\n', dados)

# Ordenando os dados pelo estoque (do maior para o menor)
dados.sort_values(by='Estoque', ascending=False, inplace=True)
print('\nProdutos ordenados pelo estoque:\n', dados)

# Resetando o índice e removendo a coluna antiga de índice
dados.reset_index(inplace=True)
dados.drop(columns='index', inplace=True)
print('\nProdutos ordenados com índice atualizado:\n', dados)

# Exibindo o terceiro produto (índice 2)
print('\nTerceiro produto:\n', dados.loc[2])

# Verificando posições com estoque maior que 100
print('\nPosições com estoque maior que 100:\n', dados['Estoque'] > 100)

# Exibindo os produtos com estoque alto (> 100)
print('\nProdutos com estoque alto:\n', dados[dados['Estoque'] > 100])

# Exibindo os produtos com estoque alto (> 100) e preço alto (> 20)
print('\nProdutos com estoque e preço altos:\n', dados[(dados['Estoque'] > 100) & (dados['Preço'] > 20)])
