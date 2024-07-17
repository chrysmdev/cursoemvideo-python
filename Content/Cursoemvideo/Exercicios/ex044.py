# DESAFIO 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto 
# - À vista no cartão: 5% de desconto 
# - em até 2x no cartão: preço normal 
# - 3x ou mais no cartão: 20% de juros

print ('{:=^40}'.format(' LOJAS MENEZES '))
preço = float(input('Digite o valor da sua compra: R$'))
pagamento = int(input('OPÇÕES DE PAGAMENTO: \n[ 1 ] À vista dinheiro/cheque; \n[ 2 ] À vista no cartão; \n[ 3 ] até 2x no cartão \n[ 4 ] 3x ou mais no cartão. \nEscolha e digite o número da opção de pagamento: '))

if pagamento == 1:
    desconto10 = preço * 10 / 100
    novo = preço - desconto10
    print(f'Quando pago por dinheiro/cheque à vista, você recebe um DESCONTO de 10% do valor. Seu novo preço com DESCONTO é R$ {novo:.2f}')
elif pagamento == 2:
    desconto5 = preço * 5 / 100
    novo = preço - desconto5
    print(f'Quando pago no cartão à vista, você recebe um DESCONTO de 5%. Seu novo preço com DESCONTO é R$ {novo:.2f}')
elif pagamento == 3:
    novo = preço / 2
    print(f'O valor do produto foi R$ {preço:.2f} e será pago em 2 parcelas de R$ {novo} cada.')
elif pagamento == 4:
    acrescimo = preço * 20 / 100
    novo = preço + acrescimo
    vezes = int(input('Em quantas vezes deseja parcelar: '))
    parcela = novo / vezes
    print(f'Quando pago no cartão em 3x ou mais, o valor sofre um acrescimo de 20%. Seu novo preço é R$ {novo:.2f} e será pago em {vezes}x no valor de R$ {parcela:.2f} ')
else:
    print('Você não digitou uma opção valida.')
