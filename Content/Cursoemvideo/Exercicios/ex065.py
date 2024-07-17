# DESAFIO 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = c = maior = menor = 0
resposta = ''
while resposta != 'n':
    c += 1
    num = int(input(f'Digite um {c}° valor: '))
    soma += num
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar colocando mais valores[S/N]? ')).strip() .lower() [0]
media = soma / c
print(f'A média dos valores foi {media:.2f}\nO total de números somados foi {soma}\nTendo o número maior como {maior} e o menor como {menor}')