soma = 0
lista_produtos = []

print('Informe os dados dos produtos')
for cont in range(10):
    print('\nProduto', cont + 1)
    nome = input('Nome: ')
    preco = float(input('Preço: '))
    produto = (nome, preco)
    soma += preco
    lista_produtos.append(produto)

media = soma / 10
print('\nO preço médio é', media)
print('Os produtos com preço acima da média são:')
for produto in lista_produtos:
    nome, preco = produto
    if preco > media:
        print('Produto:', nome)
        print('Preço:', preco)
