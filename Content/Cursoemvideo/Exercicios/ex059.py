# DESAFIO 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep

print('=-==-==-= Calculador =-==-==-=')
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print('-=' * 20)
    print('''Escolha uma das opções abaixo:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opção = int(input('Qual é a sua opção: '))
    print('-=' * 20)
    if opção == 1:
        somar = valor1 + valor2
        print(f'A soma de {valor1} + {valor2} é igual a {somar}')
    elif opção == 2:
        multi = valor1 * valor2
        print(f'O produto de {valor1} x {valor2} é {multi}')
    elif opção == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior que {valor2}')
        elif valor1 < valor2:
            print(f'{valor2} é maior que {valor1}')
        else:
            print(f'{valor1} e {valor2} possuem o mesmo valor, ou seja, são iguais.')
    elif opção == 4:
        valor1 = float(input('Digite um novo primeiro valor: '))
        valor2 = float(input('Digite um novo segundo valor: '))
    else:
        print(f'A opção [{opção}] não está disponível, tente uma opção valida.')
print('Finalizando...')
sleep(2)
print('Obrigado por utilizar o Calculador.')