# AULA 16
# TUPLAS
# TUPLAS SÃO IMUTÁVEIS
'''
lanche  = ('hamburguer', 'suco', 'pizza', 'pudim')
for c in lanche:
    print(c)
'''    

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
    
for comida in lanche: 
    print(f'Eu vou comer {comida}!')

print('Comi pra caramba!')
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
    
for pos, comida in enumerate(lanche): 
    print(f'Eu vou comer {comida}na posição {pos}')

print('Comi pra caramba!')
'''

'''
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(sorted(lanche))  # sorted  =  organizado em ordem alfabetica
'''

'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) # len(c) = lê o número de elementos de c        # c.count(5) = lê quantas vezes o número 5 se repete  #c.index(8) = mostra a primeira posição do elemento
'''

'''
pessoa = ('Gustavo', 39, 'M', 99.88) # permite tipos diferentes
del(pessoa) # del = apaga a variável da mémoria
print(pessoa)
'''