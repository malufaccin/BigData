HIST = ''

def calcula(expr):
    try:
        return eval(expr)
    except:
        print('Expressão inválida!')
        return None

def historico(expr, res):
    global HIST
    if res is not None:
        HIST += '\n' + expr
        HIST += '\n' + str(res)

def principal():
    while True:
        print('Informe a expressão matemática')
        print('(h para histórico, s para sair)')
        expr = input()
        
        if expr.lower() == 's':
            break
        elif expr.lower() == 'h':
            print(HIST, '\n')
        else:
            res = calcula(expr)
            historico(expr, res)
            print(res, '\n')

if __name__ == '__main__':
    principal()
