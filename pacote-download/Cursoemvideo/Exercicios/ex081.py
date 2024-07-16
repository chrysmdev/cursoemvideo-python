# DESAFIO 081
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = list()
pergunta = ' '
while True:
    valores.append(int(input('Digite um valor: ')))
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N] ')).strip() .upper() [0]
    if pergunta == 'N':
        break
    pergunta = ' '

print(f'A lista: {valores}')
print(f'Você digitou {len(valores)} valores')
print(f'A lista em forma decrescente é: {sorted(valores, reverse = True)}')
if 5 in valores:
    print(f'O valor 5 está na lista na {valores.index(5) + 1}° posição')
else:
    print('O valor 5 não está na lista')