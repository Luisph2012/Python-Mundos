#Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

randnumber = choice(['pedra', 'papel', 'tesoura'])
#print(randnumber)

frase = """----------JOKENPÔ----------

[ 1 ] - PEDRA
[ 2 ] - PAPEL
[ 3 ] - TESOURA
"""
userchoice = str(input('{}\nEscolha uma Opção: '.format(frase)))

userchoicelower = userchoice.lower()
print('JO')
sleep(0.5)
print('JEN')
sleep(0.5)
print('PÕ')
print('-=-' * 20)

if randnumber == userchoicelower:
    print('Empate!')
else:
    if userchoicelower == 'pedra':
        if randnumber == 'papel':
            print ('Você PERDEU')
            print('Sou escolha [{}] vs Escolha do Computador [{}]'.format(userchoicelower.title(), randnumber.title()))
        else:
            print ('Você GANHOU')
            print('Sou escolha [{}] vs Escolha do Computador [{}]'.format(userchoicelower.title(), randnumber.title()))
    elif userchoicelower == 'papel':
        if randnumber == 'tesoura':
            print ('Você PERDEU')
            print('Sou escolha [{}] vs Escolha do Computador [{}]'.format(userchoicelower.title(), randnumber.title()))
        else:
            print ('Você GANHOU')
            print('Sou escolha [{}] vs Escolha do Computador [{}]'.format(userchoicelower.title(), randnumber.title()))
    else:
        if randnumber == 'pedra':
            print ('Você PERDEU')
            print('Sou escolha [{}] vs Escolha do Computador [{}]'.format(userchoicelower.title(), randnumber.title()))
        else:
            print ('Você GANHOU')
            print('Sou escolha [{}] vs Escolha do Computador [{}]'.format(userchoicelower.title(), randnumber.title()))