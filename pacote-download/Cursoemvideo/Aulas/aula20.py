# AULA 20
# FUNÇÕES PART 1
'''
def soma(a, b):
    print(f'A = {a} e B ={b}')
    s = a + b
    print(f'A soma de A + B = {s}')
    
    
# Programa Principal
soma(4, 5)     # O '4, 5' é chamado de parâmetro
soma(a = 4, b = 5)
soma(b = 4, a = 5)     # É possível mudar a ordem dos parâmetros explicitando eles
'''
'''
def contador(* núm):
    tam = len(núm)
    print(f'Recebi {tam} valores: ', end = '')
    for n in núm:
        print(f'{n} ', end = '')
    print()
    


# Programa Principal
contador(2, 1 ,7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# Programa Principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)