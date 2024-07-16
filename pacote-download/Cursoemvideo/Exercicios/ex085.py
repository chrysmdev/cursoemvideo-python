# DESAFIO 085
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.

total = [[], []]
for n in range(1, 8):
    num = int(input(f'Digite um {n}° valor: '))
    if num % 2 == 0:
        total[0].append(num)
    else:
        total[1].append(num)
        
print('-=' * 30)        
print(f'O valores pares são : {sorted(total[0])}')
print(f'Os valores ímpares são: {sorted(total[1])}')
