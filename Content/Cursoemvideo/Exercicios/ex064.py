# DESAFIO 064
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostra quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print('Escolha valores para serem somados, caso deseje parar de somar digite 999.')
num = int(input('Digite um valor inicial: '))
continuar = ''
escolha = 0
vezes = 1
while continuar != 'n':
    escolha = int(input('Digite mais um valor: '))
    resultado = num + escolha
    if escolha == 999:
        continuar = 'n'
    else:
        vezes += 1
        print(f'A soma de {num} + {escolha} é: {resultado}')
        num = resultado
print(f'Você realizou a soma de valores {vezes} vezes no total.')
