# DESAFIO 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso 
# - Entre 18.5 e 25: Peso ideal 
# - 25 até 30: Sobrepeso 
# - 30 até 40: Obesidade 
# - Acima de 40: Obesidade mórbida

nome = str(input('Informe o nome da pessoa: ')).strip() .capitalize()
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'{nome} tem um IMC de {imc} e está Abaixo do peso')
elif imc < 25:
    print(f'{nome} tem um IMC de {imc} e está Peso ideal')
elif imc < 30:
    print(f'{nome} tem um IMC de {imc} e está Sobrepreso')
elif imc < 40:
    print(f'{nome} tem um IMC de {imc} e está Obesidade')
else:
    print(f'{nome} tem um IMC de {imc} e está Obesidade mórbida')