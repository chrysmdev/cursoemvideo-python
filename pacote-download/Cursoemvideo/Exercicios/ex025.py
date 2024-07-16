# DESAFIO 025

# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input("Digite o nome: ")).strip()
nome = nome.lower()
teste = 'SILVA' in nome
print(f'O nome digitado possui Silva? {teste}')
