# DESAFIO 084
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = list()                         
dado = list()
maior = menor = 0

while True:
    print(f'{"ADICIONANDO PESSOA":-^30}')
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if maior < dado[1]:
            maior = dado[1]
        if menor > dado[1]:
            menor = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja adicionar mais pessoas? [S/N] ')).strip() .upper() [0]
    if r in 'N':
        break  
          
print('-=' * 30)
print(f'{len(pessoas)} pessoas foram cadastradas.')

print(f'Com {maior:.2f} Kg a pessoa mais pesada foi: ', end = '')
for m in pessoas:
    if maior in m:
        print(f'• {m[0]}  ', end = '')
        
print(f'\nCom {menor:.2f} Kg a pessoa mais leve foi: ', end = '')
for m in pessoas:
    if menor in m:
        print(f'• {m[0]}  ', end = '')

