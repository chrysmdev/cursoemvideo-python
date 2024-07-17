# DESAFIO 038
# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior  
# - O segundo valor é maior  
# - Não existe valor maior, os dois são iguais.

print('Quer descobrir qual número inteiro tem valor maior?')

num1 = int(input('Digite o valor do primeiro número: '))
num2 = int(input('Digite o valor do segundo número: '))

if num1 > num2:
    print(f'O número {num1} é maior que {num2}, logo o primeiro valor é maior.')
elif num1 < num2:
    print(f'O número {num2} é maior que {num1}, logo o segundo valor é maior.')
else:
    print(f'O número {num1} e o número {num2} são iguais, logo não existe valor maior.')
