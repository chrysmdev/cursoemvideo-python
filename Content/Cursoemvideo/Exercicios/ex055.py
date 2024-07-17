# DESAFIO 055
# Faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}° pessoa em KG: '))  
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}KG e o menor é {menor}KG')
        
        
    

    