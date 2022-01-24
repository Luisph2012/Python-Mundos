#(Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite o seu Nome: '))

nomearrumado = nome.upper()
print('No seu nome tem "Silva": {}'.format('SILVA' in nomearrumado))
