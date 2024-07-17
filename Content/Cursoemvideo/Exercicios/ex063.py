# DESAFIO 063
# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# ex: 0 → 1 → 1 → 2 → 3 → 5 → 8 


final = int(input('Quantos elementos deseja ver? '))
vezes = 2
t1 = 0
t2 = 1
print(f'{t1} → {t2} → ', end = '')
while final != vezes:
    t3 = t1 + t2
    print(f'{t3} → ', end = '')
    vezes += 1
    t1 = t2
    t2 = t3
print('FIM')    
