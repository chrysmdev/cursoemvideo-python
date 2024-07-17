# DESAFIO 090
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

escola = {}

escola['nome'] = str(input('Nome: ')).strip() .capitalize()
nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))
escola['media'] = (nota1 + nota2) / 2
if escola['media'] >= 7 :
    escola['situação'] = 'APROVADO'
elif 5 <= escola['media'] < 7:
    escola['situação'] = 'RECUPERAÇÃO'
else:
    escola['situação'] = 'REPROVADO'

print('-=' * 30)
for c, v in escola.items():
    print(f' - {c} é igual a{v}')