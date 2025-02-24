import pandas as pd

# Criação do DataFrame
dados = pd.DataFrame(
    {
        'Produto': ['A', 'B', 'C', 'D', 'E'],
        'Preço': [10.5, 5.8, 9, 15.3, 21],
        'Estoque': [120, 100, 50, 150, 204]
    }
)
print('Produtos:\n', dados)
print('\nTipos de dados:\n', dados.dtypes)
print('\nColunas:', dados.columns)
print('\nEstoque:\n', dados['Estoque'])

print('\nSalvando dados em arquivo...')
dados.to_csv('produtos.csv', index=False)
print('Arquivo "produtos.csv" salvo com sucesso!')
