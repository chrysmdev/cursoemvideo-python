# DESAFIO 029
# Escreve um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre a mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade do veiculo? '))
if velocidade > 80:
    acima = velocidade - 80
    multa = acima * 7
    print(f'MULTA!!! O veiculo está {acima}km/h acima da velocidade maxima permitida, a multa é de RS {multa},00')
print('Tenha um bom dia! Dirija com segurança!')