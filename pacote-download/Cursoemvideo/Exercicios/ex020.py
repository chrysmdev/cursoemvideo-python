# DESAFIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle 
a1 = str(input('Digite o nome do(a) primeiro(a) aluno(a): '))
a2 = str(input('Digite o nome do(a) segundo(a) aluno(a): '))
a3 = str(input('Digite o nome do(a) terceiro(a) aluno(a): '))
a4 = str(input('Digite o nome do(a) quarto(a) aluno(a): '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
