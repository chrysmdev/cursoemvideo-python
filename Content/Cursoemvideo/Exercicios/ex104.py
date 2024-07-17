# DESAFIO 104
# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# ex:  n = leiaInt('Digite um n')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!!! Não é um número inteiro válido, digite novamente.\033[m')
        if ok:
            break
    return valor


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')
    