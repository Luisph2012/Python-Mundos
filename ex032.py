# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Escreva um ano (Coloque 0 Para o Ano atual): '))

if ano == 0:
    ano = date.today().year
print('{} É um ano Bissexto!'.format(ano) if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else '{} NÃO É um ano Bissexto!'.format(ano))
