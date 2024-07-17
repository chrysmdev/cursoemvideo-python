# DESAFIO 082
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

valores = list()
pergunta = ' '
while True:
    valores.append(int(input('Digite um valor: ')))
    while pergunta not in 'SN':
        pergunta = str(input('Deseja continuar? [S/N] ')).strip() .upper() [0]
    if pergunta == 'N':
        break
    pergunta = ' '
par = list()
impar = list()

for c in valores:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Você digitou os valores: {valores}')
print(f'Dos valores digitados, os pares são: {par}')
print(f'Dos valores digitados, os impares são: {impar}')
