###Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salarioAtual = float(input('Fale o seu salário atual: R$'))

salarioAumento = salarioAtual * 1.15

print('O seu salário de R$ {:.2f} com aumento é de R$ {:.2f}!'.format(salarioAtual, salarioAumento))