# DESAFIO 049
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

'''
num = float(input('Digite um número para ver a sua tabuada: '))
lim = int(input('Digite até que valor você deseja multiplicar o número solicitado: '))
valor = 0
for c in range(0, lim):
    valor += 1
    resul = num * valor
    print(f'{num:.0f} x {valor} = {resul:.1f}')
'''
    
num = float(input('Digite um número para ver a sua tabuada: '))
lim = int(input('Digite até que valor você deseja multiplicar o número solicitado: '))
for c in range(0, lim):
    resul = num * c
    print(f'{num:.0f} x {c} = {resul:.1f}')