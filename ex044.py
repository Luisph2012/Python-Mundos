#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal

#– 3x ou mais no cartão: 20% de juros


valor_produto = float(input('Qual é o valor BASE do produto: '))
print('-=-' * 20)
frase = """Qual é a Forma de Pagamento:
[ 1 ] - à vista dinheiro/cheque: 10% de desconto
[ 2 ] - à vista no cartão: 5% de desconto
[ 3 ] - 2x no cartão: preço formal
[ 4 ] - 3x ou mais no cartão: 20% de juros
"""
forma_de_pagamento = int(input('{}\nEscolha uma dessas Opções: '.format(frase)))

if forma_de_pagamento == 1:
    print('O Valor da Compra é: {:.2f}'.format(valor_produto - (valor_produto * 0.10)))
elif forma_de_pagamento == 2:
    print('O Valor da Compra é: {:.2f}'.format(valor_produto - (valor_produto * 0.05)))
elif forma_de_pagamento == 3:
    print('O Valor da Compra é: {:.2f}. {:.2f} por mês'.format(valor_produto, valor_produto/2))
elif forma_de_pagamento == 4:
    valorfinal = valor_produto + (valor_produto * 0.20)
    print('O Valor da Compra é: {:.2f}. {:.2f} por mês'.format(valorfinal, valorfinal / 3 ))
else:
    print('Opção Invalida!')




