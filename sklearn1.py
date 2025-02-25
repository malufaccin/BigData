from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Carrega a base de dados
X, Y = load_wine(return_X_y=True)

# Cria classificador de árvore de decisão
arvore = DecisionTreeClassifier(random_state=42)

# Calcula acurácia sem divisão da base de dados (overfitting possível aqui)
arvore.fit(X, Y)
acuracia = arvore.score(X, Y)
print('Acurácia sem divisão:', acuracia)

# Divisão da base de dados em treino (70%) e teste (30%)
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, train_size=0.7, random_state=42)

# Acurácia com divisão da base em treino e teste
arvore.fit(X_treino, Y_treino)
acuracia = arvore.score(X_teste, Y_teste)
print('Acurácia após divisão:', acuracia)
