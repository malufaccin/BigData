import math

print('Informe os termos da equação Ax² + Bx + C')
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a == 0:
    print('Não é uma equação de segundo grau.')
else:
    delta = b**2 - 4*a*c  # Correção da fórmula do delta
    if delta < 0:
        print('A equação não tem raízes reais.')
    elif delta == 0:
        x1 = -b / (2 * a)  # Correção da fórmula da raiz única
        print(f'A equação possui uma raiz real: x = {x1}')
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2 * a)  # Correção da fórmula da primeira raiz
        x2 = (-b - raiz_delta) / (2 * a)  # Correção da fórmula da segunda raiz
        print('A equação possui duas raízes reais:')
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
