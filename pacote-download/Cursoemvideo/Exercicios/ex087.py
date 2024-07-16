# DESAFIO 087
# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somap = somat = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l] [c] % 2 == 0:
            somap += matriz[l] [c]
        if c == 2:
            somat += matriz [l] [c]

print('-=' * 20)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end = '')
    print()
print('-=' * 20)

print(f'A soma de todos os valores pares é: {somap}')
    
print(f'A soma de todos os valores da terceira coluna é: {somat}')

print(f'O maior valor da segunda linha é: {max(matriz[1])}')

