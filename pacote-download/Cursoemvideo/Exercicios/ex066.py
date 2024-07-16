# DESAFIO 066
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('Escolha valores para serem somados, caso deseje parar de somar digite 999.')
num = int(input('Digite um valor inicial: '))
escolha = 0
vezes = 1
while True:
    escolha = int(input('Digite mais um valor: '))
    resultado = num + escolha
    if escolha == 999:
        break
    else:
        vezes += 1
        print(f'A soma de {num} + {escolha} é: {resultado}')
        num = resultado
print(f'Você digitou {vezes} valores no total.')
