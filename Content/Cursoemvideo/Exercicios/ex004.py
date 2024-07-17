# DESAFIO 004
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(x))
print('É composto apenas por espaços? ', x.isspace())
print('É composto apenas por números? ', x.isnumeric())
print('É composto apenas por letras? ', x.isalpha())
print('É composto por letras e/ou números? ', x.isalnum())
print('É composto apenas por letras maiúsculas? ', x.isupper())
print('É composto apenas por letras minúsculas? ', x.islower())
print('É uma palavra capitalizada(composta pela primeira letra maiúscula)? ', x.istitle())
