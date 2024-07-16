# DESAFIO 046
# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('Os fogos já irão estourar!!! se prepare para a contagem regressiva!')
for c in range(10, -1 , -1):
    print(c)
    sleep(1)
print('OS FOGOS ESTOURARAM!!!')