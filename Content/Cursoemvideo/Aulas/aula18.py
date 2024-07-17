# AULA 18
# VARIÁVEIS COMPOSTAS
# Listas (part 2)

# LISTA DENTRO DE LISTA
'''
dados = 'pedro', 25
pessoas = list()
pessoas.append(dados[:])

pessoas = [['Pedro',25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0])  # Pedro
print(pessoas[1][1])  # 19
print(pessoas[2][0])  # João
print(pessoas[1])     # ['Maria', 19] 
'''
# AULA PRATICA
'''
teste = list()
teste.append('Gustavo')
teste.append(40)
# print(teste)       #['Gustavo', 40]
galera = list()
galera.append(teste) #[['Gustavo', 40]]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)        #[['Maria', 22], ['Maria', 22]]

galera = list()
galera.append(teste[:]) #[['Gustavo', 40]]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)         #[['Gustavo', 40], ['Maria', 22]]
'''
'''
galera = [['João, 19'], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p)     # printa todas as listas
    
for p in galera:
    print(p[0])  # printa os nomes 
    
for p in galera:
    print(p[1])  # printa as idades
'''
'''
galera = list()                         # adiciona nome e idade para uma lista
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()                        

for p in galera:                        # analisa quem é maior e menor, diz quantos são.
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
'''