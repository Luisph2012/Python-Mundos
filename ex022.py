#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas minusculas
# Quantas letras tem total (sem considerar espacoes)
# Quantas letras tem o primeiro nome

nome_completo = str(input('Informe seu nome completo: '))

print('O seu nome é em maiúsculo {}'.format(nome_completo.upper()))
print('O seu nome é em minúsculo {}'.format(nome_completo.lower()))

nome_nospace = nome_completo.replace(' ','')
nome_separado = nome_completo.split()

print('O seu nome tem {} Letras'.format(len(nome_nospace)))
print('O primeiro nome tem {} Letras'.format(len(nome_separado[0])))