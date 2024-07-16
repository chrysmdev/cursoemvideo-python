# DESAFIO 027

# Faça um programa que elia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = str(input('Digite o seu nome: ')).strip()
nome = nome.split()
pnome = nome[0]
unome = nome[len(nome) - 1]
print(f'Primeiro: {pnome}')
print(f'Último: {unome}')
