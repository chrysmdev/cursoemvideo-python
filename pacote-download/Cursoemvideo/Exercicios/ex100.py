# DESAFIO 100
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint

def sorteia(lista):
    for n in range(0, 5):
        lista.append(randint(0, 10))
    
    

def somaPar(lista):
    s = 0
    num = []
    for n in lista:
        if n % 2 == 0:
            num.append(n)
            s += n
    print(f'A soma dos números pares {num} é de {s}')
    
    
# PROGRAMA PRINCIPAL
numeros = []
sorteia(numeros)

print('Sorteando 5 valores: ', end = '')
for n in numeros:
    print(n, end = ' ')
print()

somaPar(numeros)
