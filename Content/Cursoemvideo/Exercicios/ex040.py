# DESAFIO 040
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
nome = str(input('Olá, qual nome do(a) aluno(a) que deseja verificar? ')).strip()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'{nome} teve uma péssima média {media} e está REPROVADO!')
elif media >= 5 or media < 7:
    print(f'{nome} teve uma média {media} e está de RECUPERAÇÃO')
else:
    print(f'{nome} teve uma ótima média {media} e está APROVADO!!!')