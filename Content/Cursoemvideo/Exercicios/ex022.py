# DESAFIO 022

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# >>> O nome com todas as letras maiúsculas
# >>> O nome com todas as letras minúsculas
# >>> Quantas letras ao todo (sem considerar espaços)
# >>> Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: ')).strip()
dividir = nome.split()
juntar = ''.join(dividir)

print(f'Seu nome completo em maiúsculo: {nome.upper()}.')
print(f'Seu nome completo em minúsculo: {nome.lower()}.')
print(f'Seu nome completo possui {len(juntar)} letras ao todo.')
print(f'Seu nome possui {len(dividir[0])} letras')
