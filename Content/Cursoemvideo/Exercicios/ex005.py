# DESAFIO 005
# Faça um programa que leia um número inteiro e mostre a tela o seu sucessor e seu antecessor

num1 = int(input('Escolha um número inteiro: '))
suc = num1 + 1
ant = num1 - 1
print(f'O valor {num1} tem como antecessor {ant} e como sucessor {suc}.')