# Desenvolver um algoritmo que construa uma lista de tuplas com nome e salário de
#  funcionários. Em seguida, o código deve recalcular os salários considerando os seguintes
#  aumentos:
#  • 20% para salários de até R$2.000,00;
#  • 15% para salários entre R$2.000,00 e R$5.000,00;
#  • 5% para salários maiores que R$5.000,00;
#  Por fim, o código deve exibir o total de aumento (total dos salários novos menos o total de
#  salários antigos e os nomes dos funcionários com salários menores que R$2.000,00.

def le_salario():
    while True:
        try:
            return float(input('Salário: '))
        except:
            print('Valor inválido! Informe novamente.')

def le_funcionario():
    nome = input('Nome: ')
    salario = le_salario()
    return (nome, salario)

def aumenta_salarios(lista_funcionarios):
    for cont, funcionario in enumerate(lista_funcionarios):
        nome, salario = funcionario
        if salario <= 1500:
            salario *= 1.20 
        elif salario <= 1800:
            salario *= 1.15 
        else:
            salario *= 1.08 
        lista_funcionarios[cont] = (nome, salario)
    return lista_funcionarios

def principal():
    lista_funcionarios = []
    total_funcionarios = 0
    total_aumento = 0

    while True:
        funcionario = le_funcionario()
        lista_funcionarios.append(funcionario)
        total_funcionarios += 1

        resp = input('Continuar (S/N)? ').lower().strip()
        if resp == 'n':
            break

    lista_funcionarios = aumenta_salarios(lista_funcionarios)

    print(f'\nTotal de funcionários: {total_funcionarios}')
    print(f'Total com aumento dos salários: R$ {sum([salario for _, salario in lista_funcionarios]):.2f}')

    print('\nFuncionários com salário acima de R$ 2.800,00:')
    for nome, salario in lista_funcionarios:
        if salario > 2800:
            print(nome)

if __name__ == '__main__':
    principal()
