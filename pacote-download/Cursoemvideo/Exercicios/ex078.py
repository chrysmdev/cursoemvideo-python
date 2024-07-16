# DESAFIO 078
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = ''
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a {cont + 1}° posição: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if maior < valores[cont]:
            maior = valores[cont]
        if menor > valores[cont]:
            menor = valores[cont]
        
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor foi {maior} e ficou na: ', end = '')
for c, n in enumerate(valores):
    if n ==  maior:
        print(f'{c + 1}° posição; ', end = '')

print(f'\nO menor valor foi {menor} e ficou na: ', end = '')
for c, n in enumerate(valores):
    if n ==  menor:
        print(f'{c + 1}° posição; ', end = '')