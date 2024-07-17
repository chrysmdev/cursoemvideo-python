# DESAFIO 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.

valor = ((int(input('Digite um primeiro valor: '))), int(input('Digite um próximo valor: ')), int(input('Digite mais um valor: ')), int(input('Digite um último valor: ')))
print(f'O valor 9 apareceu {valor.count(9)} vezes')
if 3  in valor:
    print(f'O valor 3 apareceu na {valor.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado.')
print('Os números pares foram: ', end = '')
for n in valor:
    if n % 2 == 0:
        print(n, end = ' ')

        