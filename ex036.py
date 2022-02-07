# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

valor_casa = float(input('\033[1;33mQual é o Valor da Casa: \033[m'))
print('-=-' * 20)
salario = float(input('\033[1;33mQual é o salário Atual do Comprador: \033[m'))
print('-=-' * 20)
anos_pagamento = int(input('\033[1;33mO valor vai ser dividido em Quantos Anos: \033[m'))
print('-=-' * 20)
print ('\n')

meses_pagamento = anos_pagamento * 12
prestacao_casa = valor_casa / meses_pagamento

salario_porcentagem = salario * 0.30

if salario_porcentagem < prestacao_casa:
    print('\033[1;31mEMPRESTIMO NEGADO!!!')
    print('\033[1;31mInfelizmente o salário não é suficiente!')
else:
    print('\033[1;32mEMPRESTIMO APROVADO!!!')
    print('\033[1;32mDepositaremos o Dinheiro Na sua conta!')

print('\n\n\033[1;33;40mTenha um bom dia!\033[m')