# DESAFIO 026

# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip()
frase = frase.lower()
A = frase.count('a')
primeiro = frase.find('a') + 1
ultimo = frase.rfind('a') + 1
print(f'A letra "a" aparece {A} vezes na sua frase.')
print(f'O primeiro "a" aparece na {primeiro} posição.')
print(f'O ultimo "a" aparece na {ultimo} posição.')
