from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier

# Carrega base de dados
dados = load_wine()
X, Y = dados.data, dados.target

# Cria classificador de árvore de decisão com profundidade máxima de 2
arvore = DecisionTreeClassifier(max_depth=2, random_state=42)

# Classificação com validação cruzada (10-fold)
previsoes = cross_val_predict(arvore, X, Y, cv=10)

# Matriz de confusão
matriz = confusion_matrix(Y, previsoes)

# Exibe a matriz de confusão com os nomes das classes
for cont, linha in enumerate(matriz):
    print(linha, ':', dados.target_names[cont])
