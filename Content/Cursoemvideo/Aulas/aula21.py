# AULA 21
# FUNÇÕES PART 2

# interactive help

help()
'''quit para sair'''
print(input.__doc__)

# docstrings

def contador(i, f, p):
    '''
    → Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVideo.
    '''
    c = i
    while c <= f:
        print(f'{c} ', end = '')
        c += p
    print('FIM!')

help(contador)

# argumentos opcionais 

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')
    
somar(3, 2)

# escopo de variáveis

def teste(b):                                # escopo local
    a = 8                                    # a = 8
    b += 4                                   # b = 9
    c = 2                                    # c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5                                        # escopo global
print(f'A fora vale {a}')                    # a = 5


def teste(b):                                # escopo local
    global a
    a = 8                                    
    b += 4                                   # b = 9
    c = 2                                    # c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5                                        # escopo global
print(f'A fora vale {a}')                    # a = 8


# retorno de resultados

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')

# AULA PRATICA

def fatorial(num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')


def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
    