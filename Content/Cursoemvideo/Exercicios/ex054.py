# DESAFIO 054
# Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (maioridade >= 21)

from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    ano = date.today().year
    idade = ano - nasc
    if idade >= 21:
        maior = c
    elif idade < 21:
        menor = c


print(f'{maior} são maiores de idade e {menor} são menores de idade.')
        
