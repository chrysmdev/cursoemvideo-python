# AULA 17
# LISTAS (part 1)
# listas são mutaveis

# ADICIONAR ELEMENTOS
'''
lanche = ['hamburguer']
lanche.append('cookie') # acrescenta ao final um elemento
lanche.insert(0,'pizza') # insere um elemento na posição desejada (movendo os proximos elementos para direita)
'''

# APAGAR ELEMENTOS
'''
lanche = ['hamburguer', 'suco', 'pizza', 'picole', 'cookie']
del lanche[3] # mais basico
lanche.pop(3) # geralmente usado para eliminar o ultimo elemento, mas pode ser usado em outros usando o indice
lanche.remove('pizza') # elimina usando o valor (em caso de 2 ou mais elementos iguais, remove apenas o primeiro elemento)

if 'pizza' in lanche:        # usado para remover um valor, evitando erros no codigo
    lanche.remove('pizza')
'''

# CRIAR LISTA ATRAVÉS DE RANGE
'''
valores = list(range(4,11)) # cria elementos de forma coerente (crescente, decrescente, pulando x valores)
'''

# ORGANIZANDO ELEMENTOS EM LISTA
'''
valores = [8, 2, 5, 4, 9, 3, 0] # elementos de forma fora de ordem 
sorted(valores) # organiza os elementos em ordem crescente
sorted(valores, reverse = True) # organiza os elementos em ordem decrescente
len(valores) # lê quantos elementos tem na variavel
'''

# LISTA VAZIA
'''
valores = []
valores = list()
'''

# AULA PRATICA
'''
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}')
print('Cheguei ao final da lista')
'''
'''
a = [2, 3, 4, 7]
b = a            # b não recebe a, as listas são ligadas e ambas sofrem alteração se uma for alterada
b[2] = 8
print(f'LIsta A: {a}')
print(f'Lista B: {b}')
'''
'''
a = [2, 3, 4, 7]
b = a[:]            # b é uma copia de a
b[2] = 8
print(f'LIsta A: {a}')
print(f'Lista B: {b}')
'''