import matplotlib.pyplot as plt
from seaborn import load_dataset

# Carregando o dataset 'tips'
dados = load_dataset('tips')

# 1. Gráfico de linha da coluna 'total_bill'
dados['total_bill'].plot()
plt.title('Conta Total (total_bill) - Gráfico de Linha')
plt.xlabel('Índice')
plt.ylabel('Conta Total ($)')
plt.show()

# Limpa a figura atual para o próximo gráfico
plt.clf()

# 2. Histograma da coluna 'total_bill'
dados['total_bill'].plot.hist(bins=20, edgecolor='black')
plt.title('Distribuição da Conta Total (total_bill)')
plt.xlabel('Conta Total ($)')
plt.ylabel('Frequência')
plt.show()

# Limpa a figura atual para o próximo gráfico
plt.clf()

# 3. Gráfico de dispersão entre 'total_bill' e 'tip'
dados.plot.scatter(x='total_bill', y='tip', alpha=0.7, c='red', edgecolor='black')
plt.title('Relação entre Conta Total e Gorjeta')
plt.xlabel('Conta Total ($)')
plt.ylabel('Gorjeta ($)')
plt.show()
