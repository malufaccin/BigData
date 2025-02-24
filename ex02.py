import pandas as pd
from seaborn import load_dataset

def amostragem_classes(dados, atributo_classe, quantidade):
    '''Amostragem com quantidade por classe'''

    # Contagem das classes
    contagem_classes = dados[atributo_classe].value_counts()

    # DataFrame vazio para guardar amostras
    amostras = pd.DataFrame()

    # Para cada classe na contagem
    for classe in contagem_classes.index:
        # Filtra os dados pela classe
        dados_classe = dados[dados[atributo_classe] == classe]

        # Se a quantidade de dados disponíveis for maior que a quantidade desejada
        if len(dados_classe) > quantidade:
            # Amostragem sem substituição
            amostras_classe = dados_classe.sample(n=quantidade, replace=False)
        else:
            # Amostragem com substituição
            amostras_classe = dados_classe.sample(n=quantidade, replace=True)

        # Inclui amostras da classe no resultado usando pd.concat
        amostras = pd.concat([amostras, amostras_classe])

    return amostras

# Teste com a base de dados penguins
dados = load_dataset('penguins')
atributo_classe = 'species'

# Exibindo a contagem original das classes
print('Dados originais:\n', dados[atributo_classe].value_counts(), sep='')

# Realizando a amostragem
amostra = amostragem_classes(dados, atributo_classe, 100)

# Exibindo a contagem das classes na amostra
print('\nAmostra:\n', amostra[atributo_classe].value_counts(), sep='')
