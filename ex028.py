# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep
random_number = randrange(0, 6)
#print(random_number)

print('Jogo da Advinhação')
print('Escolha o numero certo\n')
print('-=-' * 20)
mychoice = int(input('Escolha um numero(De 0 - 5): '))
print('-=-' * 20)

print('Pensando...')
sleep(2)


if mychoice == random_number:
    print('Você Acertou!!')
    print('Sua escolha {}'.format(mychoice))
else:
    print('Escolha Errada!')
    print('A escolha certa era {}!'.format(random_number))
