#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
#o aumento é de 15%.

salario = float(input('Informe o seu salário: '))

if salario > 1250.00:
    salario_atualizado = salario * 0.1
else:
    salario_atualizado = salario * 0.15

print('O seu salário atualizado é {}'.format(salario_atualizado+salario))