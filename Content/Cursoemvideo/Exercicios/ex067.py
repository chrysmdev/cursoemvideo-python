# DESAFIO 067
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
 
print('~~~~~~~~~~ Tabuada ~~~~~~~~~~')
num = int(input('Insira um valor para ver a sua tabuada:  '))
vezes = 1
while True:
    if num < 0:
        break
    print(f'{num} x {vezes} = {num * vezes}')
    if vezes == 10:
        print('-=' * 20)
        num = int(input('Insira um novo valor para ver a sua tabuada:  '))
        vezes = 1
    else:
        vezes += 1
print('Tabuada finalizada.')
'''
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
'''