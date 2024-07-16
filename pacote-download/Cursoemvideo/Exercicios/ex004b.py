# DESAFIO 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# exercicio 4 porém usando .format(), mas do jeito a partir do python 3.7
# 'No Python 3.7, não precisa colocar o .format() no final, basta colocar "f" na frente das aspas e inserir os valores dentro dos colchetes, como está acima.' comentario do youtube

x = input('Digite algo: ')
print(f'Qual o tipo primitivo desse valor? {type(x)}')
print(f'É composto apenas por espaços? {x.isspace()}')
print(f'É composto apenas por números? {x.isnumeric()}')
print(f'É composto apenas por letras? {x.isalpha()}')
print(f'É composto por letras e/ou números? {x.isalnum()}')
print(f'É composto apenas por letras maiúsculas? {x.isupper()}')
print(f'É composto apenas por letras minúsculas? {x.islower()}')
print(f'É uma palavra capitalizada(composta pela primeira letra maiúscula)? {x.istitle()}')